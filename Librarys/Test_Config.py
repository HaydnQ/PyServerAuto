# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 15:00
# @Author  : Haydn
# @Email   : haydnqiu@qq.com
# @File    : Test_Config.py
# @Software: PyCharm

# Generally speaking, there are usually 2 host in one server.
HOST_INFO_A = {
    'address': 'xx.xx.xx.xx',
    'ports': 22,
    'username': 'root',
    'password': 'xxxxxx',
    'location': 'A',
}
HOST_INFO_B = {
    'address': 'xx.xx.xx.xx',
    'ports': 22,
    'username': 'root',
    'password': 'xxxxxx',
    'location': 'B',
}
PDU_INFO = {
    'hostname': 'xx.xx.xx.xx',
    'port': 23,
    'username': 'xxx',
    'password': 'xxx',
    'outlet': 'xxx'          # ports
}

# serial port info for using SSerials
# COM* for windows, /dev/ttyUSB* for linux
# using "Serial_A = SSerials(**Serial_A_INFO)" for initializing an objection Serial_A
Serial_A_INFO = {'port': 'COM*', 'baudrate': 115200, 'timeout': 5}
Serial_B_INFO = {'port': 'COM*', 'baudrate': 115200, 'timeout': 5}
Serial_C_INFO = {'port': 'COM*', 'baudrate': 115200, 'timeout': 5}
Serial_D_INFO = {'port': '/dev/ttyUSB0', 'baudrate': 115200, 'timeout': 5}
Serial_E_INFO = {'port': '/dev/ttyUSB0', 'baudrate': 115200, 'timeout': 5}
Serial_F_INFO = {'port': '/dev/ttyUSB0', 'baudrate': 115200, 'timeout': 5}

# serial set info (dict)
# using "libs.get_key(dct, value)" to get key from vaule
# using "libs.get_keys_index(dct, key)" to get key's index from key
com_set1 = {'xxxA': 'COM1', 'XXXB': 'COM2', 'XXXC': 'COM3', 'XXXD': 'COM4'}
com_set2 = {'NodeA': "COM1", 'NodeB': 'COM2'}
