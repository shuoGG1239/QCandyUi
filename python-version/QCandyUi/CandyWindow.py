import json
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import qApp

from QCandyUi import WindowWithTitleBar
from QCandyUi import simple_qss

THEME_FILE = 'theme.json'


def createWindow(mainWidget, title='Cool', ico_path='', theme=None):
    coolWindow = WindowWithTitleBar.WindowWithTitleBar(mainWidget)
    coolWindow.setWindowTitle(title)
    coolWindow.setWindowIcon(QIcon(ico_path))
    setTheme(theme)
    return coolWindow


def setTheme(theme):
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

# def green_decorator(aClass):
#     """
#     绿色主题装饰, 可以装饰所有的QWidget类使其直接拥有绿色主题
#     :param aClass:
#     :return:
#     """
#
#     def on_call(*args, **kargs):
#         src_widget = aClass(*args, **kargs)
#         dst_widget = window_titlebar.WindowWithTitleBar(src_widget, Qss.DARKBLUEGREEN)
#         qApp.setStyleSheet(qss)
#         return dst_widget
#
#     return on_call
