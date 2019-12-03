import sys
import os

sys.path.append(os.getcwd())
import pytest

from tool.read_yaml import read_yaml
from api.api_mis import ApiMis
from tool.tool import Tool
import api


class TestMis:
    # 初始化
    def setup_class(self):
        # 后去ApiMis对象
        self.mis = ApiMis()
        # 获取Tool对象
        self.tool = Tool()

    # 登录
    @pytest.mark.parametrize("account,password", read_yaml("mis_login.yaml"))
    def test01_mis_login(self, account, password):
        # 调用登录业务方法
        response = self.mis.api_mis_login(account, password)
        print("后台登录数据：", response.json())
        # 断言
        self.tool.assert_code_message(response)
        # 提取 token
        self.tool.get_token(response)
        print("提取的token值为：", api.headers)
        print("--" * 50)

    # 查询
    def test02_mis_search(self):
        # 调用查询业务方法
        response = self.mis.api_search_article()
        print("--" * 50)
        print("查询结果为：", response.json())
        # 断言
        self.tool.assert_code_message(response, code=200)

    # 审核
    def test03_mis_audit(self):
        # 调用审核业务方法
        response = self.mis.api_audit()
        print("--" * 50)
        print("审核结果为：", response.json())
        # 断言
        self.tool.assert_code_message(response)
