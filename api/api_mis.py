import requests

import api
from tool.get_log import GetLog

log = GetLog.get_log()


class ApiMis:
    # 初始化
    def __init__(self):
        # 登录 url
        self.url_login = api.url_mis + "/authorizations"
        # 查询 url
        self.url_search = api.url_mis + "/articles"
        # 审核 url
        self.url_audit = api.url_mis + "/articles"

    # 登录
    def api_mis_login(self, account, password):
        """
        :param account: 登录账号
        :param password: 登录密码
        :return: 登录后的响应对象
        """
        # 定义 json数据
        data = {"account": account, "password": password}
        # 日志
        log.info("正在执行 后台管理登录接口，登录的数据 账号：{}, 密码：{}".format(account, password))
        # 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 查询文章
    def api_search_article(self):
        """
        :return: 查询后的响应对象
        """
        # 定义json数据
        data = {"title": api.title, "channel": api.channel}
        log.info("正在执行 后台管理查询文章接口，查询文章数据 title：{}, channel：{}".format(api.title, api.channel))
        # 调用get方法
        return requests.get(url=self.url_search, params=data, headers=api.headers)

    # 审核文章
    def api_audit(self):
        """
        :return: 审核后的响应对象
        """
        # 定义json数据 status 2为审核通过
        data = {"article_ids": [api.article_id], "status": 2}
        log.info("正在调用审核文章接口，审核的文章id为：{} ，状态为：{}".format(api.article_id, 2))
        # 调用put方法
        return requests.put(url=self.url_audit, json=data, headers=api.headers)
