import api
from tool.get_log import GetLog

log = GetLog.get_log()


class Tool:
    # 断言公共方法
    def assert_code_message(self, response, code=201, message="OK"):
        try:
            # 断言状态码
            assert response.status_code == code, "{} != {}".format(response.status_code, code)
            # 断言响应信息
            assert response.json().get("message") == message, "{} !- {}".format(response.json().get('message'), message)
        except Exception as e:
            log.error(e)
            # 抛异常
            raise

    # token提取
    def get_token(self, response):
        # 提取token
        token = response.json().get("data").get("token")
        # 将token附加到 headers
        api.headers['Authorization'] = "Bearer " + token
