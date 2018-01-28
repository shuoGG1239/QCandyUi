"""

    本类使用的例子在下面, WindowWithTitleBar那里

"""

from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QFrame
from PyQt5.QtCore import QEvent, QSize, Qt, pyqtSlot
from PyQt5.QtGui import QPainter, QBitmap, QIcon, QColor
from PyQt5.Qt import QMouseEvent, QSizePolicy
import os
import win32gui, win32con

# 这些路径是相对main.py的, 而不是相对本py文件的
titletextcolor = "white"
imageroot = "./qss_ui_theme/FlatUiSrcImage/"
imageclosenorm = "close.png"
imageclosehover = "closehover.png"
imageclosepress = "closepress.png"
imagemaxnorm = "maxsize.png"
imagemaxhover = "maxsizehover.png"
imagemaxpress = "maxsizepress.png"
imageminnorm = "minsize.png"
imageminhover = "minsizehover.png"
imageminpress = "minsizepress.png"
imageresizenorm = "resize.png"
imageresizehover = "resizehover.png"
imageresizepress = "resizepress.png"


class TitleBar(QWidget):
    titlebarHeight = 30
    parentwidget = None

    def __init__(self, parent, colorid):
        super(TitleBar, self).__init__(parent)
        qss = str()
        self.parentwidget = parent
        self.setFixedHeight(self.titlebarHeight)
        self.m_pBackgroundLabel = QLabel(self)
        self.m_pIconLabel = QLabel(self)
        self.m_pTitleLabel = QLabel(self)
        self.m_pMinimizeButton = QPushButton(self)
        self.m_pMaximizeButton = QPushButton(self)
        self.m_pCloseButton = QPushButton(self)
        self.m_pIconLabel.setFixedSize(20, 20)
        self.m_pIconLabel.setScaledContents(True)
        self.m_pTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.m_pBackgroundLabel.resize(self.parentwidget.width(), self.titlebarHeight)
        # 三大金刚按钮大小
        self.m_pMinimizeButton.setFixedSize(27, 22)
        self.m_pMaximizeButton.setFixedSize(27, 22)
        self.m_pCloseButton.setFixedSize(27, 22)
        self.m_pMaximizeButton.setEnabled(False)
        self.m_pTitleLabel.setObjectName("whiteLabel")
        self.m_pMinimizeButton.setObjectName("minimizeButton")
        self.m_pMaximizeButton.setObjectName("maximizeButton")
        self.m_pCloseButton.setObjectName("closeButton")
        # 布局
        pLayout = QHBoxLayout(self)
        pLayout.addWidget(self.m_pIconLabel)
        pLayout.addSpacing(5)
        pLayout.addWidget(self.m_pTitleLabel)
        pLayout.addWidget(self.m_pMinimizeButton)
        pLayout.addWidget(self.m_pMaximizeButton)
        pLayout.addWidget(self.m_pCloseButton)
        pLayout.setSpacing(0)
        pLayout.setContentsMargins(5, 0, 5, 0)
        self.setLayout(pLayout)
        # 信号连接
        self.m_pMinimizeButton.clicked.connect(self.__slot_onclicked)
        self.m_pMaximizeButton.clicked.connect(self.__slot_onclicked)
        self.m_pCloseButton.clicked.connect(self.__slot_onclicked)
        # 标题字体颜色
        self.m_pTitleLabel.setStyleSheet("font-size:13px;margin-bottom:0px;color:%s" % (titletextcolor));
        # 标题栏背景颜色
        self.m_pBackgroundLabel.setStyleSheet("background:%s" % (colorid));
        # 三大金刚按钮Ui设置
        self.m_pCloseButton.setStyleSheet(
            self.__get_button_imgqss(imageroot, imageclosenorm, imageclosehover, imageclosepress, imageclosepress))
        self.m_pMinimizeButton.setStyleSheet(
            self.__get_button_imgqss(imageroot, imageminnorm, imageminhover, imageminpress, imageminpress))
        self.m_pMaximizeButton.setStyleSheet(
            self.__get_button_imgqss(imageroot, imagemaxnorm, imagemaxhover, imagemaxpress, imagemaxpress))

    def __get_button_imgqss(self, root, norm, hover, press, disable):
        qss = ''
        qss += "QPushButton{background:transparent; background-image:url(%s); border:none}" % (
            root + norm)
        qss += "QPushButton:hover{background:transparent; background-image:url(%s)}" % (
            root + hover)
        qss += "QPushButton:pressed{background:transparent; background-image:url(%s)}" % (
            root + press)
        qss += "QPushButton:disabled{background:transparent; background-image:url(%s)}" % (
            root + disable)
        return qss

    def mouseDoubleClickEvent(self, e):
        # self.m_pMaximizeButton.clicked.emit()     # 双击全屏
        pass

    def mousePressEvent(self, e):
        """
        使窗口能被拖动
        :param e:
        :return:
        """
        win32gui.ReleaseCapture()
        pWindow = self.window()
        if pWindow.isWindow():
            win32gui.SendMessage(pWindow.winId(), win32con.WM_SYSCOMMAND, win32con.SC_MOVE + win32con.HTCAPTION, 0)
        e.ignore()

    def eventFilter(self, object, e):
        if e.type() == QEvent.WindowTitleChange:
            if object != None:
                self.m_pTitleLabel.setText(object.windowTitle())
                return True
        if e.type() == QEvent.WindowIconChange:
            if object != None:
                icon = object.windowIcon()
                self.m_pIconLabel.setPixmap(icon.pixmap(self.m_pIconLabel.size()))
                return True
        if e.type() == QEvent.Resize:
            self.__updateMaxmize()
            self.__setTitleBarSize(self.parentwidget.width())
            return True
        # 注意!这里self要加上!!!!!!!!!
        return QWidget.eventFilter(self, object, e)

    @pyqtSlot()
    def __slot_onclicked(self):
        pButton = self.sender()
        pWindow = self.window()
        if pWindow.isWindow():
            if pButton.objectName() == 'minimizeButton':
                pWindow.showMinimized()
            elif pButton.objectName() == 'maximizeButton':
                if pWindow.isMaximized():
                    pWindow.showNormal()
                    # self.setStyleSheet(...)   # cpp有这段代码,虽然暂时未察觉有什么影响
                else:
                    pWindow.showMaximized()
                    # self.setStyleSheet(...)   # cpp有这段代码,虽然暂时未察觉有什么影响
            elif pButton.objectName() == 'closeButton':
                pWindow.close()
                os._exit(0)

    def __updateMaxmize(self):
        pWindow = self.window()
        if pWindow.isWindow() == True:
            bMaximize = pWindow.isMaximized()
            if bMaximize == 0:
                self.m_pMaximizeButton.setProperty("maximizeProperty", "restore")
            else:
                self.m_pMaximizeButton.setProperty("maximizeProperty", "maximize")
                self.m_pMaximizeButton.setStyle(QApplication.style())

    def __setTitleBarSize(self, width):
        self.m_pBackgroundLabel.resize(width, self.titlebarHeight)

    def setMaximumEnable(self, isenable):
        self.m_pMaximizeButton.setEnabled(isenable)


"""
使用示例:
    app = QApplication(sys.argv)
    keywidget = KeyActionWidget.KeyActionWidget()
    mainWindow = window_titlebar.WindowWithTitleBar(keywidget, qss_setting.DARKBLUEGREEN, 0)
    mainWindow.setWindowTitle('Key action')
    mainWindow.setWindowIcon(QIcon(window_titlebar.imageroot + 'myicon.ico'))
    green_theme.setAppGreenStyle()
    mainWindow.show()
    sys.exit(app.exec_())
"""


class WindowWithTitleBar(QFrame):
    titlebar = None

    def __init__(self, mainwidget, colorstr, parent):
        super(WindowWithTitleBar, self).__init__()
        self.mainwidget = mainwidget;
        self.resize(mainwidget.width(), mainwidget.height() + TitleBar.titlebarHeight)
        self.titlebar = TitleBar(self, colorstr)
        self.setWindowFlags(Qt.FramelessWindowHint | self.windowFlags())
        self.installEventFilter(self.titlebar)
        # 布局: titlbar在上主窗体在下
        pLayout = QVBoxLayout(self)
        pLayout.addWidget(self.titlebar)
        pLayout.addWidget(mainwidget)
        pLayout.setSpacing(0)  # 排列的几个widget为0间隔
        pLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(pLayout)

    def setWindowRadius(self, n_px):
        """
        圆边
        :param n_px: 弧度
        :return:
        """
        objBitmap = QBitmap(self.size())
        painter = QPainter(objBitmap)
        painter.setBrush(QColor(0, 0, 0))
        painter.drawRoundedRect(self.rect(), n_px, n_px)
        self.setMask(objBitmap)

    def setBackgroundBorderColor(self, bgdcolor, bordercolor):
        self.setStyleSheet("WindowWithTitleBar{background:%s;border:3px solid %s}" % (bgdcolor, bordercolor))

    def closeEvent(self, *args, **kwargs):
        self.mainwidget.close()
