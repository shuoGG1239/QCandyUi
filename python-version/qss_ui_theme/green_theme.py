from PyQt5.QtWidgets import qApp

from qss_ui_theme import qss_setting as Qss
from qss_ui_theme import titlebar
from qss_ui_theme import window_titlebar

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


def green_decorator(aClass):
    """
    绿色主题装饰, 可以装饰所有的QWidget类使其直接拥有绿色主题
    :param aClass:
    :return:
    """

    def on_call(*args, **kargs):
        src_widget = aClass(*args, **kargs)
        dst_widget = window_titlebar.WindowWithTitleBar(src_widget, Qss.DARKBLUEGREEN, 0)
        setAppGreenStyle()
        return dst_widget

    return on_call


def setAppGreenStyle():
    """
    一键设置,见上面的示例
    :return: void
    """
    qApp.setStyleSheet(getGreenStyleTitleWindowQss())


def __getGreenStyleQss():
    """
    绿色主题的Qss, 想创造什么蓝色主题可以按这个方法的格式来创
    :return: green Qss string
    """
    qss_str = str()
    qss_str += Qss.getFontQss("微软雅黑", Qss.DEEPBLUEGREEN)
    qss_str += Qss.getPushButtonQss(Qss.BLUEGREEN, Qss.WHITE, Qss.LIGHTGREEN, Qss.BLUEGREEN, Qss.LIGHTGRAY, Qss.WHITE,
                                    Qss.GRAY, Qss.LIGHTGRAY)
    qss_str += Qss.getPlaineditQss(Qss.LIGHTGRAY, Qss.BLUEGREEN)
    qss_str += Qss.getTextBrowerQss(Qss.LIGHTGRAY, Qss.BLUEGREEN)
    qss_str += Qss.getLineeditQss(Qss.LIGHTGRAY, Qss.BLUEGREEN)
    qss_str += Qss.getComboxQss(Qss.WHITE, Qss.LIGHTGRAY, Qss.BLUEGREEN, titlebar.imageroot + "down_arrow.png")
    img_norm = titlebar.imageroot + "radio_normal.png"
    img_down = titlebar.imageroot + "radio_down.png"
    img_hover = titlebar.imageroot + "radio_hoverUncheck.png"
    img_downhover = titlebar.imageroot + "radio_hoverCheck.png"
    qss_str += Qss.getRadioButtonQss(img_norm, img_down, img_hover, img_downhover)
    img_norm = titlebar.imageroot + "checkbox_normal.png"
    img_down = titlebar.imageroot + "checkbox_down.png"
    img_hover = titlebar.imageroot + "checkbox_hoverUncheck.png"
    img_downhover = titlebar.imageroot + "checkbox_hoverCheck.png"
    qss_str += Qss.getCheckBoxQss(img_norm, img_down, img_hover, img_downhover)
    qss_str += Qss.getTabWidgetQss(Qss.BLUEGREEN, Qss.WHITE)
    qss_str += Qss.getSliderQss(Qss.BLUEGREEN, Qss.WHITE, Qss.BLUEGREEN)
    qss_str += Qss.getScrollbarQss(Qss.BLUEGREEN)
    return qss_str


def getGreenStyleTitleWindowQss():
    """
    主体Qss加上TitleBar的Qss
    :return:
    """
    qss_str = str()
    qss_str += __getGreenStyleQss()
    qss_str += __getTitleWindowQss(Qss.WHITE, Qss.DARKBLUEGREEN)
    qss_str += __getTitleBarQss(Qss.WHITE, Qss.DARKBLUEGREEN)
    return qss_str


def __getTitleBarQss(textColor, backgroundColor):
    qss_str = str()
    qss_str += "QLabel#%s{font-size:13px;margin-bottom:0px;color:%s;}" % (titlebar.Titlebar.TITLE_LABEL_NAME, textColor)
    qss_str += "QLabel#%s{background:%s;}" % (titlebar.Titlebar.BACKGROUND_LABEL_NAME, backgroundColor)
    return qss_str


def __getTitleWindowQss(backgroundColor, borderColor):
    """
    TitleBar的Qss
    :param backgroundColor: 底色
    :param borderColor: 窗口描边
    :return:
    """
    qss_str = "WindowWithTitleBar{background:%s;border:3px solid %s}" % (backgroundColor, borderColor)
    return qss_str
