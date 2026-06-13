'''py
 ' @Author: allcloud.top
 ' @Date: 2025-01-05 00:22:50
 ' @Last Modified by: allcloud.top
 ' @Name: 
'''
import unittest

from unimail_py_sdk import UnimailReq, Client, Result
# from unimail_py_sdk.Client import Client, Result

client: Client = Client("")


def setUpModule():
    print("into test")


class TestClient(unittest.TestCase):

    # def test_init(self):
    #     client.check_connect()
    def test_check_connect(self):
        print(client)
        result = client.check_connect()
        self.assertEqual(result, True)

    def test_send_email(self):
        req = UnimailReq(
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
        self.assertEqual(result.code, 0)
