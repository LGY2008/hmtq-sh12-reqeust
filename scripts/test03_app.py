import sys
import os

sys.path.append(os.getcwd())
import pytest

from tool.read_yaml import read_yaml
from api.api_app import ApiApp
from tool.tool import Tool
import api


class TestApp:
    # 初始化
    def setup_class(self):
        # 获取ApiApp对象
        self.app = ApiApp()
        # 获取Tool对象
        self.tool = Tool()

    # 登录测试方法
    @pytest.mark.parametrize("mobile,code", read_yaml("app_login.yaml"))
    def test01_app_login(self, mobile, code):
        # 调用登录业务方法
        response = self.app.api_app_login(mobile, code)
        print("App登录后的数据为：", response.json())
        # 断言
        self.tool.assert_code_message(response)
        # 提取token
        self.tool.get_token(response)
        print("App登录后提取的token信息：", api.headers)

    # 查询文章测试方法
    def test02_search_article(self):
        # 调用查询业务方法
        response = self.app.api_search_article()
        print("App搜文章的值为：", response.json())
        # 断言
        self.tool.assert_code_message(response, code=200)
