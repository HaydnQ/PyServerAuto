## *My thoughts in PyServerAuto*

*Once you make your own case, please make sure you have read this **README.md** file.*
## 1. Librarys
***
### **Test_Config.py**
This is the configuration file of this project. **You should fill your own configuration at first!**
### **libs.py**
A basic function lib. You don't have to import it to the case.*(But if you do need, please use the command below)* 
> from Librarys.libs import *
### **SimpleSerial.py**
An essential function lib of **Serial Port Operational Testing**. You should import it at the first time as you have some operation at your serial port.
> from Librarys.SimpleSerial import *
### **SimpleSSH.py**
An essential function lib of **SSH command Testing**. You should import it at the first time when you remote another unit and want to send some  commands.
> from Librarys.SimpleSSH import *
### **Log.py**
The logging lib. You won't see it at your case because if you don't have any operation about serial port or SSH.  
The Log.py works after you import "SimpleSerial.py" or "SimpleSSH.py" accordingly. Don't worry about it.
***
## 2. Case syntax
　You should follow the syntax below. 
1. Make sure your python version > 3.6.
2. Make sure you have writen your own "main" like below.
```
from Librarys.SimpleSerial import *
from Librarys.SimpleSSH import *

if __name__ == "__main__":
  ......
　(code here)
  ......
```

## *我对PyServerAuto构想*
*请在第一时间查阅此README.md文档*
## 1.基本函数库
***
### **Test_Config.py**
项目的配置文件**在写自己的case前请第一时间编辑此配置文件**
### **libs.py**
基本函数库。这个文件会在你包含SimpleSerial.py或SimpleSSH.py时候一同包入*（但如果确确实实需要的话，请使用下面的命令）*
>from Librarys.libs import *
### **SimpleSerial.py**
这个是**执行串口操作**的基本函数库。在cases里应在第一时间导入它。
>from Librarys.SimpleSerial import *
### **SimpleSSH.py**
这个是**执行SSH命令**的基本函数库。如果你需要远程ssh控制其他机器+发送一些命令时，应在第一时间导入它。
>from Librarys.SimpleSSH import *
### **Log.py**
这个是log库。log.py在导入“SimpleSerial.py”或“SimpleSSH.py后会自行运作。
***
## 2.语法
遵循以下规则。


1.确保您的python版本>3.6.


2.参考以下代码。
```
from Librarys.SimpleSerial import *
from Librarys.SimpleSSH import *

if __name__ == "__main__":
  ......
　(code here)
  ......
```
