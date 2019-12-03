import time

import requests

import api


class ApiApp:
    # 初始化
    def __init__(self):
        # 登录 url
        self.url_login = api.url_app + "/v1_0/authorizations"
        # 查询 url
        self.url_article = api.url_app + "/v1_1/articles"

    # 登录
    def api_app_login(self, mobile, code):
        # 请求数据
        data = {"mobile": mobile, "code": code}
        # 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 查询文章
    def api_search_article(self):
        # 请求数据
        """
        :channel_id 频道id 7为数据库
        :timestamp 时间戳，毫秒数
        :with_top 是否包含置顶 取值范围(1:包含 0:不包含)
        :return:
        """
        data = {"channel_id": int(api.channel_id), "timestamp": int(time.time()), "with_top": 1}
        # 调用get方法
        return requests.get(url=self.url_article, params=data, headers=api.headers)
