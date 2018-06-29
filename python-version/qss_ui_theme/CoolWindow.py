from qss_ui_theme import green_theme
from qss_ui_theme import qss_setting
from qss_ui_theme import window_titlebar
from PyQt5.QtGui import QIcon


def createWindow(mainWidget, title='Cool', ico_path='', theme='green_blue'):
    coolWindow = window_titlebar.WindowWithTitleBar(mainWidget)
    coolWindow.setWindowTitle(title)
    coolWindow.setWindowIcon(QIcon(ico_path))
    __setStyle(theme)
    return coolWindow


def __setStyle(theme):
    if theme == 'green_blue':
        green_theme.setAppGreenStyle()
