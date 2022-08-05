## *My thoughts in PyServerAuto*

*Once you make your own case, please make sure you have read this **README.md** file.*
## 1. Librarys
***
### **Test_Config.py**
This is the configuration file of this project. **You should fill your own configuration at first!**
### **libs.py**
A basic function lib. You don't have to import it to the case.*(But if you do need, please use the command below)* 
> from libs import *
### **SimpleSerial.py**
An essential function lib of **Serial Port Operational Testing**. You should import it at the first time as you have some operation at your serial port.
> from SimpleSerial import *
### **SimpleSSH.py**
An essential function lib of **SSH command Testing**. You should import it at the first time when you remote another unit and want to send some  commands.
> from SimpleSSH import *
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
