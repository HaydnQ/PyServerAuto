# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 15:00
# @Author  : Haydn
# @Email   : haydnqiu@qq.com
# @File    : libs.py
# @Software: PyCharm

# coding=utf-8
import telnetlib
import time
import sys
from pathlib import Path
from Librarys.Test_Config import *


def get_key(dct, value) -> list:
    """
    Retuen keys from A distinct vaule.
    :param dct: Dict to serch
    :param value: the value
    :return: keys' list
    """
    return list(filter(lambda key: dct[key] == value, dct))

def get_keys_index(dct, key) -> int:
    """
    Return one key's index from itself in the dict
    :param dct: Dict to serch
    :param key: the key
    :return: key's index
    """
    return list(dct.keys()).index(key)

def set_log_path(dir_name=None, file_name=None, suffix='.txt', parent_path=r"C:\Log\ProjectName") -> str:
    """
    Generating log file path
    Usage: set_log_path(dir_name="TestCase_1_dir", file_name="TestCase1"， suffix="_opps.txt")
    It will return: "C:\Log\ProjectName\TestCase_1_dir\TestCase1_opps.txt"
    :param dir_name: Default: executing py file name's stem. IF u need change, please type it.
    :param file_name: Default: executing py file name's stem. IF u need change, please type it.
    :param suffix: Default: '.txt'. It can also be "_opps.txt" like "TestCase1_opps.txt"
    :param parent_path: Log file parent's parent dir, log file parent's dir is "dir_name"
    :return: the absolute path of log file.
    """
    if not dir_name:
        dir_name = Path(sys.argv[0]).stem
    if not file_name:
        file_name = Path(sys.argv[0]).stem

    log_dir = Path(parent_path, dir_name)
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file_path = str(Path(log_dir, f'{file_name}{suffix}'))
    return log_file_path

def pdu_control(method='on'):
    """
    Telnet PDU control.
    :param method: 'on', 'off' and 'reboot' can be used.
    :return: True or False
    """
    method = method.lower()
    if method.upper() not in ['ON', 'OFF', 'REBOOT']:
        return False
    ip, port, user, passwd, outlet = PDU_INFO.values()

    pdu = telnetlib.Telnet()
    pdu.open(ip, port, 10)
    print(pdu.read_until(b'User Name :').decode())
    pdu.write(user.encode() + b'\r')
    print(pdu.read_until(b'Password  :').decode())
    pdu.write(passwd.encode() + b'\r')
    print(pdu.read_until(b'apc>').decode())
    pdu.write(f'ol{method} {outlet}\r'.encode())
    print(pdu.read_until(b'apc>').decode())
    pdu.close()
    return True


def execute_command(channel, command: str, handle: bytes = b'>', newline: bytes = b'\r'):
    # it could be used in serial or telnet if u wish.
    cmd = command.encode() + newline
    channel.write(cmd)
    channel.read_until(cmd)
    return channel.read_until(handle).decode()


if __name__ == '__main__':
    pdu_control('on')
    pass
