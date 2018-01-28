from PyQt5.QtWidgets import qApp
from qss_ui_theme import window_titlebar
from qss_ui_theme import qss_setting as Qss
"""
示例:
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



def setAppGreenStyle():
    """
    一键设置,见上面的示例
    :return: void
    """
    qApp.setStyleSheet(getGreenStyleTitleWindowQss())


def getGreenStyleQss():
    """
    绿色主题的Qss, 想创造什么蓝色主题可以按这个方法的格式来创
    :return: green Qss string
    """
    qss_str = str()
    qss_str += Qss.getFontQss("微软雅黑",Qss.DEEPBLUEGREEN)
    qss_str += Qss.getPushButtonQss(Qss.BLUEGREEN,Qss.WHITE,Qss.LIGHTGREEN,Qss.BLUEGREEN,Qss.LIGHTGRAY,Qss.WHITE,Qss.GRAY,Qss.LIGHTGRAY)
    qss_str += Qss.getPlaineditQss(Qss.LIGHTGRAY,Qss.BLUEGREEN)
    qss_str += Qss.getLineeditQss(Qss.LIGHTGRAY,Qss.BLUEGREEN)
    qss_str += Qss.getComboxQss(Qss.WHITE,Qss.LIGHTGRAY,Qss.BLUEGREEN,window_titlebar.imageroot+"bluearrow.png")
    qss_str += Qss.getProgressBarQss(Qss.LIGHTGRAY,Qss.BLUEGREEN)
    img_norm = window_titlebar.imageroot + "radio_normal.png"
    img_down = window_titlebar.imageroot + "radio_down.png"
    img_hover = window_titlebar.imageroot + "radio_hoverUncheck.png"
    img_downhover = window_titlebar.imageroot + "radio_hoverCheck.png"
    qss_str += Qss.getRadioButtonQss(img_norm,img_down,img_hover,img_downhover)
    img_norm = window_titlebar.imageroot + "checkbox_normal.png"
    img_down = window_titlebar.imageroot + "checkbox_down.png"
    img_hover = window_titlebar.imageroot + "checkbox_hoverUncheck.png"
    img_downhover = window_titlebar.imageroot + "checkbox_hoverCheck.png"
    qss_str += Qss.getCheckBoxQss(img_norm,img_down,img_hover,img_downhover)
    qss_str += Qss.getTabWidgetQss(Qss.BLUEGREEN,Qss.WHITE)
    qss_str += Qss.getSliderQss(Qss.BLUEGREEN,Qss.WHITE,Qss.BLUEGREEN)
    qss_str += Qss.getScrollbarQss(Qss.BLUEGREEN)
    return qss_str


def getGreenStyleTitleWindowQss():
    """
    主体Qss加上TitleBar的Qss
    :return:
    """
    qss_str = str()
    qss_str += getGreenStyleQss()
    qss_str += __getTitleWindowQss(Qss.WHITE,Qss.DARKBLUEGREEN)
    return qss_str


def __getTitleWindowQss(backgroundColor, borderColor):
    """
    TitleBar的Qss
    :param backgroundColor: 底色
    :param borderColor: 窗口描边
    :return:
    """
    qss_str = "WindowWithTitleBar{background:%s;border:3px solid %s}"%(backgroundColor,borderColor)
    return qss_str