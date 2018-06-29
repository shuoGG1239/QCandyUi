from PyQt5.QtWidgets import qApp

from QCandyUi import qss_getter as Qss
from QCandyUi.Titlebar import Titlebar
from QCandyUi import WindowWithTitleBar
from QCandyUi.resourse_cfg import *

"""
示例1:
    直接使用装饰器@green_decorator
eg:
@green_decorator
class CharModify(QWidget):
    ... ...


示例2:
    非常简单, 只要一句setAppGreenStyle()就能做到设置绿色主题;
    但是只用这句的话只有绿色样式, 没有绿色扁平titlebar, 是系统自带的标题栏;
eg:
    import sys
    app = QApplication(sys.argv)
    mainWindow = KeyActionWidget.KeyActionWidget()
    green_theme.setAppGreenStyle()
    mainWindow.show()
    sys.exit(app.exec_())
"""


def getBlueGreenQss():
    """
    蓝绿主题
    :return:
    """
    # fontLight, fontDark, normal, light, deep, disLight, disDark
    return getQss(Qss.WHITE, Qss.DEEPBLUEGREEN, Qss.BLUEGREEN, Qss.LIGHTGREEN, Qss.DARKBLUEGREEN, Qss.LIGHTGRAY, Qss.GRAY, "blueGreen")


def getQss(fontLight, fontDark, normal, light, deep, disLight, disDark, themeName):
    """
    通用组件的Qss + CandyBar的Qss
    :param fontLight:
    :param fontDark:
    :param normal:
    :param light:
    :param deep:
    :param disLight:
    :param disDark:
    :param themeName:
    :return:
    """
    qss_str = str()
    qss_str += __getWidgetsQss(fontLight, fontDark, normal, light, deep, disLight, disDark, themeName)
    qss_str += __getCandyQss(fontLight, deep, fontLight, themeName)
    return qss_str


def __getWidgetsQss(fontLight, fontDark, normal, light, deep, disLight, disDark, themeName):
    """
    通用组件(Widgets)的Qss
    :param fontLight:
    :param fontDark:
    :param normal:
    :param light:
    :param deep:
    :param disLight:
    :param disDark:
    :param themeName:
    :return:
    """
    qss_str = str()
    qss_str += Qss.getFontQss("微软雅黑", fontDark)
    qss_str += Qss.getPushButtonQss(normal, fontLight, light, normal, disLight, fontLight, disDark, disLight)
    qss_str += Qss.getPlaineditQss(disLight, normal)
    qss_str += Qss.getTextBrowerQss(disLight, normal)
    qss_str += Qss.getLineeditQss(disLight, normal)
    qss_str += Qss.getComboxQss(fontLight, disLight, normal, IMAGE_ROOT + themeName + "/" + "down_arrow.png")
    img_norm = IMAGE_ROOT + themeName + "/" + "radio_normal.png"
    img_down = IMAGE_ROOT + themeName + "/" + "radio_down.png"
    img_hover = IMAGE_ROOT + themeName + "/" + "radio_hoverUncheck.png"
    img_downhover = IMAGE_ROOT + themeName + "/" + "radio_hoverCheck.png"
    qss_str += Qss.getRadioButtonQss(img_norm, img_down, img_hover, img_downhover)
    img_norm = IMAGE_ROOT + themeName + "/" + "checkbox_normal.png"
    img_down = IMAGE_ROOT + themeName + "/" + "checkbox_down.png"
    img_hover = IMAGE_ROOT + themeName + "/" + "checkbox_hoverUncheck.png"
    img_downhover = IMAGE_ROOT + themeName + "/" + "checkbox_hoverCheck.png"
    qss_str += Qss.getCheckBoxQss(img_norm, img_down, img_hover, img_downhover)
    qss_str += Qss.getTabWidgetQss(normal, fontLight)
    qss_str += Qss.getSliderQss(normal, fontLight, normal)
    qss_str += Qss.getScrollbarQss(normal)
    return qss_str


def __getCandyQss(barTextColor, barColor, winBgdColor, themeName):
    """
    TitleBar+CandyWindow的Qss
    :param barTextColor: 文字颜色
    :param barColor: bar主体颜色
    :param winBgdColor: 主体窗口背景颜色
    :param themeName: 主题名(作用主要是为了找按钮图片)
    :return: qss
    """
    Titlebar.THEME = themeName
    qss_str = str()
    qss_str += "Titlebar QLabel#%s{font-size:13px;margin-bottom:0px;color:%s;}" % (Titlebar.TITLE_LABEL_NAME, barTextColor)
    qss_str += "Titlebar QLabel#%s{background:%s;}" % (Titlebar.BACKGROUND_LABEL_NAME, barColor)
    # 三大金刚键的图片设置 (最大化恢复正常大小的图片设置只能在Title的onclick中设置)
    qss_str += "Titlebar QPushButton#%s{background:transparent; background-image:url(%s); border:none}" % \
               (Titlebar.MIN_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_MIN_NORM)
    qss_str += "Titlebar QPushButton#%s:hover{background:transparent; background-image:url(%s)}" % \
               (Titlebar.MIN_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_MIN_HOVER)
    qss_str += "Titlebar QPushButton#%s:pressed{background:transparent; background-image:url(%s)}" % \
               (Titlebar.MIN_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_MIN_PRESS)
    qss_str += "Titlebar QPushButton#%s:disabled{background:transparent; background-image:url(%s)}" % \
               (Titlebar.MIN_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_MIN_PRESS)
    qss_str += "Titlebar QPushButton#%s{background:transparent; background-image:url(%s); border:none}" % \
               (Titlebar.MAX_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_MAX_NORM)
    qss_str += "Titlebar QPushButton#%s:hover{background:transparent; background-image:url(%s)}" % \
               (Titlebar.MAX_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_MAX_HOVER)
    qss_str += "Titlebar QPushButton#%s:pressed{background:transparent; background-image:url(%s)}" % \
               (Titlebar.MAX_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_MAX_PRESS)
    qss_str += "Titlebar QPushButton#%s:disabled{background:transparent; background-image:url(%s)}" % \
               (Titlebar.MAX_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_MAX_PRESS)
    qss_str += "Titlebar QPushButton#%s{background:transparent; background-image:url(%s); border:none}" % \
               (Titlebar.CLOSE_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_CLOSE_NORM)
    qss_str += "Titlebar QPushButton#%s:hover{background:transparent; background-image:url(%s)}" % \
               (Titlebar.CLOSE_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_CLOSE_HOVER)
    qss_str += "Titlebar QPushButton#%s:pressed{background:transparent; background-image:url(%s)}" % \
               (Titlebar.CLOSE_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_CLOSE_PRESS)
    qss_str += "Titlebar QPushButton#%s:disabled{background:transparent; background-image:url(%s)}" % \
               (Titlebar.CLOSE_BUTT_NAME, IMAGE_ROOT + themeName + "/" + IMG_CLOSE_PRESS)
    # CandyWindow窗口内底色+外围描边
    qss_str += "WindowWithTitleBar{background:%s;border:3px solid %s}" % (winBgdColor, barColor)
    return qss_str
