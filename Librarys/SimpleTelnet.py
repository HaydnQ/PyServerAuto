# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 15:00
# @Author  : Haydn
# @Email   : haqiu@celestica.com haydnqiu@qq.com
# @File    : SimpleTelnet.py
# @Software: PyCharm
from carrera_lib.Log import *
from carrera_lib.libs import *


class STelnet(object):
    def __init__(self, hostname, port, username, password):
        self.telnet = telnetlib.Telnet()
        self.host_ip = hostname
        self.port = port
        self.user = username
        self.passwd = password

        self.log = Logger(set_log_path(f'_Telnet{self.host_ip}.log'))

    def login_host(self, timeout=10):
        """
        此函数telnet连接。
        :return:
        """
        try:
            self.telnet.open(self.host_ip, port=self.port)
        except Exception:
            # self.log.critical(f"[{self.host_ip} {self.port}] connect fail")
            return False

        self.telnet.read_until(b':', timeout=timeout)
        self.telnet.write(self.user.encode('ascii') + b'\n')
        self.telnet.read_until(b':', timeout=timeout)
        self.telnet.write(self.passwd.encode('ascii') + b'\n')
        time.sleep(3)
        # 获得登录结果
        # read_very_eager() 获得上次获得之后的全部输出
        connect_result = self.telnet.read_very_eager().decode('ascii')
        print(connect_result)
        if 'Login incorrect' in connect_result:
            print('Login incorrect')
            return False
            # self.log.error(connect_result)
            # self.log.critical(f"[{self.host_ip} {self.port}] login fail, wrong user name or password.")
        else:
            # self.log.info(f"{self.host_ip} login successful")
            # self.execute_command("sudo -s")
            # self.execute_command("cd /")
            print('Login correct')
            return True

    def execute_command(self, cmd):
        """实现执行命令，并输出其执行结果
        :param cmd: 需要执行的命令
        :return: 命令执行的结果
        """
        self.telnet.write(cmd.encode('ascii') + b'\n')
        cmd_result = ''
        start_time = time.time()
        while time.time() - start_time < 360:
            time.sleep(0.2)
            result = self.telnet.read_very_eager().decode('ascii')
            if 'apc>' in cmd_result.split("\n")[-1]:
                break
            cmd_result += result
        # self.log.info('%s' % cmd_result)
        print(cmd_result)
        return cmd_result

    def execute_handler(self, cmd: str, handler=b'apc>'):
        self.telnet.write(cmd.encode('ascii') + b'\r')
        result = self.telnet.read_until(handler)
        print(result)
        return result


if __name__ == '__main__':
    pass
