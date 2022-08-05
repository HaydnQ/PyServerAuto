# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 15:00
# @Author  : Haydn
# @Email   : haydnqiu@qq.com
# @File    : Log.py
# @Software: PyCharm

# coding=utf-8
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


class Logger(object):
    """
    log class
    """
    def __init__(self, path: str, level=logging.DEBUG, file_level=logging.DEBUG):
        self.logger = logging.getLogger(path)

        # 如果...列表为空，则添加日志，否则直接写日志，避免log重复记录。
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
            # 设置console日志
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(fmt=fmt)
            stream_handler.setLevel(level=level)
            # 设置文件日志
            file_handler = TimedRotatingFileHandler(path, when='D', interval=1)
            # file_handler = logging.FileHandler(path)
            file_handler.setFormatter(fmt=fmt)
            file_handler.setLevel(level=file_level)

            self.logger.addHandler(stream_handler)
            self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message: str):
        if '\n' in message:
            for i in message.split('\n'):
                    self.logger.info(i.rstrip())
        else:
            self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def quit(self):
        self.logger.info(b"Test quits.")
        exit()
