import json
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import qApp

from QCandyUi import WindowWithTitleBar
from QCandyUi import simple_qss

"""
使用示例1:
    app = QApplication(sys.argv)
    w = CandyWindow.createWindow(LogViewer(), 'Log Viewer', 'myicon.ico', 'blueGreen')
    w.show()
    sys.exit(app.exec_())

使用示例2:
eg:
@colorful('blue')
class CharModify(QWidget):
    ... ...
"""


def colorful(theme):
    """
    彩色主题装饰, 可以装饰所有的QWidget类使其直接拥有彩色主题
    :param theme: 主题名, 与theme.json里面的主题名对应
    :return:
    """

    def new_func(aClass):
        def on_call(*args, **kargs):
            src_widget = aClass(*args, **kargs)
            dst_widget = createWindow(src_widget, theme)
            return dst_widget

        return on_call

    return new_func


def createWindow(mainWidget, theme=None, title='Cool', ico_path=''):
    """
    快速创建彩色窗
    :param mainWidget:
    :param theme:
    :param title:
    :param ico_path:
    :return:
    """
    coolWindow = WindowWithTitleBar.WindowWithTitleBar(mainWidget)
    coolWindow.setWindowTitle(title)
    coolWindow.setWindowIcon(QIcon(ico_path))
    setTheme(theme)
    return coolWindow


def setTheme(theme):
    THEME_FILE = 'theme.json'
    if os.path.isfile(THEME_FILE):
        path = THEME_FILE
    else:
        path = (os.path.split(__file__)[0] + '\\' + THEME_FILE).replace('\\', '/')
    tDict = json.load(open(path))
    if theme is None or theme == '':
        theme = tDict['defaultTheme']
        colorDict = tDict[theme]
    else:
        colorDict = tDict[theme]
    qss = simple_qss.getQss(colorDict['fontLight'], colorDict['fontDark'], colorDict['normal'], colorDict['light'],
                            colorDict['deep'], colorDict['disLight'], colorDict['disDark'], theme)
    qApp.setStyleSheet(qss)

