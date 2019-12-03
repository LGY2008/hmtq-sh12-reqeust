# 导包
import logging.handlers


class GetLog:
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取 日志器
            cls.__log = logging.getLogger()
            # 设置 总入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取 处理器 TimeFile...
            ts = logging.handlers.TimedRotatingFileHandler(filename="./log/hmtq.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 获取 格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)
            # 将格式器添加到 处理器中
            ts.setFormatter(fmt)
            # 将处理器添加到 日志器
            cls.__log.addHandler(ts)
        # 返回日志
        return cls.__log
