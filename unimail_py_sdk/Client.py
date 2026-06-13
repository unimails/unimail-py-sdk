"""Unimail Python SDK client (v2-compatible)."""

from __future__ import annotations

import json
from dataclasses import dataclass, field

import requests


DOMAIN = "https://uniapi.allcloud.top"
TIMEOUT_SECONDS = 120


@dataclass
class EmailAttachment:
    name: str
    file_attachment: bytes | None = None
    url_attachment: str = ""


@dataclass
class UnimailReq:
    from_name: str = ""
    receivers: list[str] = field(default_factory=list)
    cc: str = ""
    bcc: str = ""
    subject: str = ""
    txt_content: str = ""
    html_content: str = ""
    attachments: list[EmailAttachment] = field(default_factory=list)

    def append_attachment(self, email_attachment: EmailAttachment) -> None:
        if email_attachment.file_attachment is None and not email_attachment.url_attachment:
            raise ValueError("unimail: attachment is empty")
        self.attachments.append(email_attachment)

    def append_file(self, name: str, path: str) -> None:
        with open(path, "rb") as file:
            content = file.read()
        self.append_attachment(EmailAttachment(name=name, file_attachment=content))

    def append_uri(self, name: str, url: str) -> None:
        self.append_attachment(EmailAttachment(name=name, url_attachment=url))


class Result:
    def __init__(self, code: int = 0, msg: str = "success", data=None, obj=None):
        self.code = code
        self.msg = msg
        self.data = data
        if isinstance(obj, dict):
            self.__dict__.update(obj)

    def is_success(self) -> bool:
        return self.code == 0

    def __str__(self) -> str:
        return self.to_str()

    def to_str(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False)

    @classmethod
    def HttpError(cls):
        return Result(500, "http error")


class Client:
    __support_lang = ["zh", "en", "vi", "th", "id", "gu"]

    def __init__(self, key: str, host: str = DOMAIN, timeout: int = TIMEOUT_SECONDS):
        self.__host = host.rstrip("/")
        self.__key = key
        self.__lang = "zh"
        self.__timeout = timeout

    def set_language(self, lang: str) -> bool:
        if lang not in Client.__support_lang:
            return False
        self.__lang = lang
        return True

    def check_connect(self) -> bool:
        try:
            result = requests.post(
                self.__host + "/v2/checkConnection",
                json={"authorization": self.__key},
                headers={"Content-Type": "application/json", "Accept-Language": self.__lang},
                timeout=self.__timeout,
            ).json()
            return result.get("code") == 0
        except Exception:
            return False

    def send_email(self, req: UnimailReq) -> Result:
        if len(req.receivers) == 0:
            return Result(400, "receivers is required")
        if not req.subject:
            return Result(400, "subject is required")
        if not req.txt_content and not req.html_content:
            return Result(400, "txt_content or html_content is required")

        form_data: list[tuple[str, str]] = [
            ("authorization", self.__key),
            ("receiver", ";".join(req.receivers)),
            ("from", req.from_name),
            ("subject", req.subject),
        ]
        if req.cc:
            form_data.append(("cc", req.cc))
        if req.bcc:
            form_data.append(("bcc", req.bcc))
        if req.txt_content:
            form_data.append(("txtContent", req.txt_content))
        if req.html_content:
            form_data.append(("htmlContent", req.html_content))

        files: list[tuple[str, tuple[str, bytes, str]]] = []
        for idx, attachment in enumerate(req.attachments):
            form_data.append((f"attachments[{idx}].name", attachment.name))
            if attachment.file_attachment is not None:
                files.append(
                    (
                        f"attachments[{idx}].fileAttachment",
                        (attachment.name, attachment.file_attachment, "application/octet-stream"),
                    )
                )
            elif attachment.url_attachment:
                form_data.append((f"attachments[{idx}].urlAttachment", attachment.url_attachment))

        try:
            response = requests.post(
                self.__host + "/v2/sendEmail",
                data=form_data,
                files=files if files else None,
                headers={"Accept-Language": self.__lang},
                timeout=self.__timeout,
            )
            payload = response.json()
            if isinstance(payload, dict):
                return Result(obj=payload)
            return Result.HttpError()
        except Exception:
            return Result.HttpError()
