# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 15:00
# @Author  : Haydn
# @Email   : haydnqiu@qq.com
# @File    : SimpleSerial.py
# @Software: PyCharm
import re
import xmodem
import serial.tools.list_ports
from threading import Thread

from carrera_lib.libs import *
from carrera_lib.Log import *


class SSerial(serial.Serial):
    # Open the serial
    def connect(self, loop=None):
        self.which = get_key(com_set1, self.port)[0]
        self.baudrate = 115200
        self.loop = '' if not loop else f'Loop{loop}'

        log_path = \
            str(Path(set_log_path()).parent / self.loop / Path(set_log_path(f"_{self.which}.log")).name)
        txt_path = str(Path(set_log_path()).parent / Path(set_log_path()).name)

        Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        Path(txt_path).parent.mkdir(parents=True, exist_ok=True)
        self.log = Logger(log_path)
        self.txt = Logger(txt_path)

    # receive the messages
    def reads(self):
        gets = self.read_all().decode('gbk', errors='ignore')
        self.log.info(gets)
        return gets

    # write the commands & receive the messages
    def sends(self, data: str):
        """
        Input commands into serial port, and receive messages for it.
        :param data: commands to send
        :return: messages to read
        """
        self.write(b'\r' + data.encode() + b"\r")
        time.sleep(4) if 'set' in data else time.sleep(0.25)

        gets = self.read_all().decode('gbk', errors='ignore')
        self.log.info(gets)
        return gets

    # send + read + compare(if need)
    def run(self, *args, cmp: bool = True):
        """
        :param args: commands
        :param cmp: do compare or not
        :return: None
        """
        if args:
            for i in args:
                self.sends(i) if not cmp else self.compare(self.sends(i), i)

    # Compare function
    def compare(self, rev, cmd):
        temp, msg, rev = '', '', str(rev)
        if cmd:
            try:
                if 'xxx' in cmd:
                    msg = re.findall(r'xxxxxxxxxxxx', rev)[0]
                    self.txt.info(f'{self.which}:"{cmd}", Messages: {msg}.')
                    Conditions = msg in ['aaa', 'bbb']
                    if Conditions:
                        temp = 'fail'
                if temp == 'fail':
                    self.txt.error(f'{self.which}:"{cmd}" {temp} with "{msg}"')
            except Exception as e:
                self.txt.critical(str(e))

    # Print information
    def print_info(self):
        # print(self.main_engine.name, end=', ')  # 设备名字
        print(f'{self.port}, {self.baudrate}')  # 读或者写端口
        print(self.baudrate, end=', ')  # 波特率
        print(self.bytesize, end=', ')  # 字节大小
        print(self.parity, end=', ')  # 校验位
        print(self.stopbits, end=', ')  # 停止位
        print(self.timeout, end=', ')  # 读超时设置
        print(self.writeTimeout, end=', ')  # 写超时
        print(self.xonxoff, end=', ')  # 软件流控
        print(self.rtscts, end=', ')  # 软件流控
        print(self.dsrdtr, end=', ')  # 硬件流控
        print(self.interCharTimeout)  # 字符间隔超时

    # Print available ports
    @staticmethod
    def available_ports(shows=True):
        port_list = [x.name for x in serial.tools.list_ports.comports()]
        if shows:
            print(f'All serials: {", ".join(port_list)}.')
        return port_list

# Serial operation using Thread(Becase some of these operations are similar.)
class ThreadingSerials:
    cmd = str()
    list_all = list()

    def __init__(self, defaults=1, loop=None):
        """
        Make thread for all serial ports, and connect these.
        """
        txt_path = str(Path(set_log_path()).parent / Path(set_log_path()).name)
        Path(txt_path).parent.mkdir(parents=True, exist_ok=True)
        self.txt = Logger(txt_path)

        if defaults == 1:
            for i in com_set1.values():
                self.list_all.append(SSerial(i, baudrate=115200))
        else:
            for i in com_set2.values():
                self.list_all.append(SSerial(i, baudrate=115200))
        for item in self.list_all:
            item.connect(loop)

    def connect(self, loop):
        if loop:
            self.txt.info('*'*25 + f" Loop{loop} " + '*'*25)
        for item in self.list_all:
            item.connect(loop)

    def close(self):
        # close all serial ports
        for i in self.list_all:
            i.close()

    def run(self, *command, select=None):
        """
        :param select: Select from com_set1/com_set2 to send command.
        :param command: command(s) to send
        :return: None
        """
        def sends(which):
            """
            :param which: Select a port to send commands
            :return: None
            """
            which = self.list_all[which]
            which.run(*self.cmd)

        if command:
            self.cmd = command
        if not select:
            select = list(range(0, len(self.list_all)))
        elif isinstance(select, str):
            if select.upper() == 'TypeA':
                select = [0, 1]
            elif select.upper() == 'TypeB':
                select = [2, 3]
            elif select.upper() == 'LocationA':
                select = [0, 2]
            elif select.upper() == 'LocationB':
                select = [1, 3]
        elif select in range(len(self.list_all)):
            sends(select)
            return

        t_list = []
        for i in select:
            t = Thread(target=sends, args=(i,))
            t.start()
            t_list.append(t)
        for i in t_list:
            i.join()


if __name__ == '__main__':
    pass
