# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 15:00
# @Author  : Haydn
# @Email   : haydnqiu@qq.com
# @File    : SimpleSSH.py
# @Software: PyCharm
import re
import paramiko

from carrera_lib.Log import *
from carrera_lib.libs import *


# Return One Host
def host_set_up(location='A'):
    """
    Using ssh to connect the Host A/B. 
    :param location: Host A or B
    :return: host
    """
    return SimpleSSH(**host_info_a) if location == 'A' else SimpleSSH(**host_info_b)


# SSH to host
class SimpleSSH:
    def __init__(self, address, ports, username, password, location="A"):
        self.location = location.upper()

        # log files
        self.txt = Logger(set_log_path())
        self.log = Logger(set_log_path(f'_OS{self.location}.log'))

        try:
            self.client = paramiko.client.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
            self.client.connect(address, username=username, password=password, look_for_keys=False)
            self.transport = paramiko.Transport((address, ports))
            self.transport.connect(username=username, password=password)
            self.shell = self.client.invoke_shell()
        except Exception as e:
            self.txt.error(f"SSH:Connect to server on ip {address}/HOST{self.location} fail.{e}")
            self.close_connection()
            exit()

    def loop(self, loop=None):
        if not loop:
            loop = ''
        else:
            loop = f'Loop{loop}'
        log_path = \
            str(Path(set_log_path()).parent / loop / Path(set_log_path(f'_OS{self.location}.log')).name)
        txt_path = str(Path(set_log_path()).parent / loop / Path(set_log_path()).name)
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        Path(txt_path).parent.mkdir(parents=True, exist_ok=True)
        self.log = Logger(log_path)
        self.txt = Logger(txt_path)
        self.txt.info(f"SSH:Connect to server on ip HOST{self.location} pass.")

    def close_connection(self):
        if self.client:
            try:
                self.client.close()
                self.transport.close()
            except Exception:
                pass
            finally:
                self.txt.info(f'Close the connection with Host{self.location}')

    def run(self, *args):
        """
        If the number of commands exceeds 1, use thread mode to send commands
        Else, send a command directly.
        :param args: commands
        :return: None
        """
        if args:
            for item in args:
                self.send_shell(item)

    def send_shell(self, command, sleep=1):
        """
        Send_shell command once
        :param command: cmd to send
        :param sleep: wait for console out after sending cmd.
        :return:
        """
        if self.shell:
            if command:
                if '-m 0xe' in command:
                    time.sleep(8)
                self.shell.send(b'\n' + command.encode('ascii') + b'\n')
                time.sleep(sleep)
                cmd_result = ''
                while True:
                    # Log result when available
                    if self.shell and self.shell.recv_ready():
                        now_data = self.shell.recv(65535)
                        while self.shell.recv_ready():
                            now_data += self.shell.recv(65535)
                        cmd_result += str(now_data, encoding='ascii')
                        self.log.info('%s' % cmd_result)
                        time.sleep(0.25)
                    else:
                        break
                    return cmd_result
        else:
            self.log.critical("Shell not opened.")


if __name__ == '__main__':
    host = host_set_up()
    host.send_shell('cd /')
    host.send_shell('pwd')
    host.send_shell('cd /home')
    host.send_shell('pwd')
    host.close_connection()
