'''py
 ' @Author: i-curve
 ' @Date: 2025-01-05 00:22:50
 ' @Last Modified by: i-curve
 ' @Name: 
'''
import unittest
from unimail_py_sdk.Client import Client, Result

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
        result: Result = client.send_email(
            "email1", "测试标题", "测试内容 in python")
        for key, val in result.__dict__.items():
            print(f"{key}: {val}")
        self.assertEqual(result.code, 0)

    def test_batch_send_email(self):
        result: Result = client.batch_send_email(
            ["email1", "email2"], "测试标题", "测试内容 in python")
        for key, val in result.__dict__.items():
            print(f"{key}: {val}")
        self.assertEqual(result.code, 0)
