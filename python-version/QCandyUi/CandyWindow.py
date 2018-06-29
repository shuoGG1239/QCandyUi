from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import qApp

from QCandyUi import WindowWithTitleBar
from QCandyUi import simple_qss


def createWindow(mainWidget, title='Cool', ico_path='', theme='blueGreen'):
    coolWindow = WindowWithTitleBar.WindowWithTitleBar(mainWidget)
    coolWindow.setWindowTitle(title)
    coolWindow.setWindowIcon(QIcon(ico_path))
    __setTheme(theme)
    return coolWindow


def __setTheme(theme):
    qss = simple_qss.getQssByTheme(theme)
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
