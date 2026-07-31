# unimal-py-sdk

> The current SDK version is v2. If you need to use the previous v1 version, please switch to the v1 branch.

This is a Python SDK for Unimail. Quickly integrate into your project

[github](https://github.com/unimails/unimail-py-sdk) [中文文档](README_zh.md)

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [unimal-py-sdk](#unimal-py-sdk)
  - [usage](#usage)
  - [api docs](#api-docs)
  - [support language](#support-language)

<!-- /code_chunk_output -->

## usage

- pip install

```shell
pip install unimail-py-sdk
```

- init a unimail client

you need a authorization key.

main.py

```python
from unimail_py_sdk import UnimailReq, Client, Result

# please input your key here
key: str = ""

client: Client = Client(key)

result = client.check_connect()
print(result)
```

- send email

```python
    req = UnimailReq(
        route = "route",
        # from_name= "",
        receivers=["email"],
        # cc=["email"],
        # bcc=["email"],
        subject="test",
        html_content="test",
    )
    req.append_file("att1.txt", path = "tests/attachment.txt")
    result: Result = client.send_email(req)
    for key, val in result.__dict__.items():
        print(f"{key}: {val}")
```

## api docs

1. Client(key: str, host: str, data: str, obj: json): Client

init a client by key

2. client.set_language(language :str) -> bool

set language for the client,default is zh

3. client.check_connect() -> bool

check the host and key is ok

4. client.send_email(req :UnimailReq) -> Result

please see usage

## support language

chinese is the default language for the sdk.

- [x] english (en)
- [x] simple chinese (zh)
- [x] vietnamese (vi)
- [x] idonesian (id)
- [x] thai (th)
- [x] gujarati (gu)

if you want to support other language, please open a issue.

- tips

If you want to use this SDK, please contact the author via admin@allcloud.top.
