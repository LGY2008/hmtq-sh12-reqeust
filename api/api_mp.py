import api
import requests
from tool.get_log import GetLog

log = GetLog.get_log()


class APiMp:
    # 初始化
    def __init__(self):
        # 登录url
        self.url_login = api.url_mp + "/authorizations"
        # 发布文章url
        self.url_article = api.url_mp + "/articles"

    # 登录
    def api_mp_login(self, mobile, code):
        """
        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        # 定义请求报文
        data = {"mobile": mobile, "code": code}
        # 调用post方法 并且 返回响应对象
        log.info("正在调用自媒体登录接口，url:{}, mobile:{}, code:{}".format(self.url_login,mobile, code))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 发布文章
    def api_mp_article(self, title, content, channel_id):
        """
        :param title: 文章标题
        :param content: 文章内容
        :param channel_id: 频道ID
        :return: 响应对象
        """
        # 定义 请求报文
        data = {"title": title,
                "content": content,
                "channel_id": channel_id,
                "cover": {"type": 0, "images": []}}
        # 调用post方法
        log.info("正在调用自媒体发布文章接口，url:{}, title:{}, conent:{}, channel_id:{} ,headers:{}".
                 format(self.url_article, title, content, channel_id, api.headers))
        return requests.post(url=self.url_article, json=data, headers=api.headers)
