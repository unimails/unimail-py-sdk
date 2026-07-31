# unimal-py-sdk

> 当前sdk的版本是v2, 如果你需要用以前的v1版本, 请切换v1分支

unimail 的 python 语言 sdk, 快速集成到你的项目

[github](https://github.com/unimails/unimail-py-sdk) [英文文档](README.md)

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [unimal-py-sdk](#unimal-py-sdk)
  - [使用](#使用)
  - [api docs](#api-docs)
  - [支持的语言](#支持的语言)

<!-- /code_chunk_output -->

## 使用

- pip 安装包

```shell
pip install unimail-py-sdk
```

- 初始化客户端

你需要申请一个 key

main.py

```python
from unimail_py_sdk import UnimailReq, Client, Result

# please input your key here
key: str = ""

client: Client = Client(key)

result = client.check_connect()
print(result)
```

- 发邮件

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

## 支持的语言

sdk 默认返回的 msg 为中文

- [x] english (en)
- [x] simple chinese (zh)
- [x] vietnamese (vi)
- [x] idonesian (id)
- [x] thai (th)
- [x] gujarati (gu)

如果你需要添加了更多语言，欢迎提 issue

- 提示

如果想要使用 unimail sdk, 请通过邮件联系作者 admin@allcloud.top
