# QCandy-UI
方便快速地美化Qt应用, 提供了C++版和PyQt版


# 使用方法(Python版)
* 仅需在需要美化的窗口类上加上@colorful装饰器即可
* 也可以调用CandyWindow.creatWindow()返回经美化的QWidget (推荐用这种)

# 实例
* 原味窗口
```python
# 窗口类为TcpUdpSerialPortTool
# TcpUdpSerialPortTool.py
class TcpUdpSerialPortTool(QWidget):
    ... ...

# main.py
app = QApplication(sys.argv)
mainWindow = TcpUdpSerialportTool.TcpUdpSerialPortTool()
mainWindow.show()
sys.exit(app.exec_())
```
![norm](https://i.loli.net/2018/07/04/5b3c404bde41f.png)
  
  
* 加了蓝绿色主题的窗口(使用@colorful)
```python
# 窗口类为TcpUdpSerialPortTool
# TcpUdpSerialPortTool.py
from QCandyUi.CandyWindow import colorful

@colorful('blueGreen')
class TcpUdpSerialPortTool(QWidget):
    ... ...

# main.py
app = QApplication(sys.argv)
mainWindow = TcpUdpSerialportTool.TcpUdpSerialPortTool()
mainWindow.show()
sys.exit(app.exec_())
```
![blueGreen](https://i.loli.net/2018/07/04/5b3c412bc2977.png)
  
  
* 加了深蓝色主题的窗口(使用@colorful)
```python
# 窗口类为TcpUdpSerialPortTool
# TcpUdpSerialPortTool.py
from QCandyUi.CandyWindow import colorful

@colorful('blueDeep')
class TcpUdpSerialPortTool(QWidget):
    ... ...

# main.py
app = QApplication(sys.argv)
mainWindow = TcpUdpSerialportTool.TcpUdpSerialPortTool()
mainWindow.show()
sys.exit(app.exec_())
```
![blueDeep](https://i.loli.net/2018/07/04/5b3ca389e4e53.png)
* 加了深蓝色主题的窗口(使用CandyWindow.createWindow)
```python
from QCandyUi import CandyWindow

mainWindow = TcpUdpSerialportTool.TcpUdpSerialPortTool()
mainWindow = CandyWindow.createWindow(mainWindow, 'blueDeep')
mainWindow.show()
```

* 想自己新增颜色主题可以在theme.json里面配
* py模块的安装包在/python-version/dist中
