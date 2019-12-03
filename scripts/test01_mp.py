import sys
import os
sys.path.append(os.getcwd())
import pytest

from tool.read_yaml import read_yaml


from tool.get_log import GetLog
import api
from tool.tool import Tool

from api.api_mp import APiMp

log = GetLog.get_log()


class TestMp:
    # 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.mp = APiMp()
        self.tool = Tool()

    # 调用业务测试方法
    @pytest.mark.parametrize("mobile,code", read_yaml("mp_login.yaml"))
    def test01_mp_login(self, mobile, code):
        # 调用登录业务方法
        response = self.mp.api_mp_login(mobile, code)
        # 断言
        self.tool.assert_code_message(response)
        print("公共的headers:", api.headers)
        # 提取token
        self.tool.get_token(response)
        print("公共的headers设置 token的值:", api.headers)

    # 调用发布文章
    @pytest.mark.parametrize("title,content,channel_id", read_yaml("mp_article.yaml"))
    def test02_mp_article(self, title, content, channel_id):
        api.channel_id = channel_id
        # 提取 title
        api.title = title
        response = self.mp.api_mp_article(title, content, channel_id)
        print("发布文章结果", response.json())
        # 断言
        self.tool.assert_code_message(response)
        # 提取id 保存 article_id变量
        api.article_id = response.json().get("data").get("id")

