"""

    本类使用的例子在下面, WindowWithTitleBar那里

"""

from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QFrame
from PyQt5.QtCore import QEvent, QSize, Qt, pyqtSlot, QRect, QPoint
from PyQt5.QtGui import QPainter, QBitmap, QIcon, QColor
from PyQt5.Qt import QMouseEvent, QSizePolicy
import os
import win32gui, win32con

# 这些路径是相对main.py的, 而不是相对本py文件的
titletextcolor = "white"
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
# 资源路径
imageroot = './qss_ui_theme/FlatUiSrcImage/'
if not os.path.exists(imageroot + imageclosenorm):
    imageroot = (os.path.split(__file__)[0] + "\\FlatUiSrcImage\\").replace('\\', '/')


class TitleBar(QWidget):
    TITLEBAR_HEIGHT = 30
    ICON_SIZE = QSize(20, 20)
    MIN_BUTT_SIZE = QSize(27, 22)
    MAX_BUTT_SIZE = QSize(27, 22)
    CLOSE_BUTT_SIZE = QSize(27, 22)

    def __init__(self, parent, colorstr):
        super(TitleBar, self).__init__(parent)
        self.parentwidget = parent
        self.setFixedHeight(TitleBar.TITLEBAR_HEIGHT)
        self.m_pBackgroundLabel = QLabel(self)
        self.m_pIconLabel = QLabel(self)
        self.m_pTitleLabel = QLabel(self)
        self.m_pMinimizeButton = QPushButton(self)
        self.m_pMaximizeButton = QPushButton(self)
        self.m_pCloseButton = QPushButton(self)
        self.m_pIconLabel.setFixedSize(TitleBar.ICON_SIZE)
        self.m_pIconLabel.setScaledContents(True)
        self.m_pTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.m_pBackgroundLabel.resize(self.parentwidget.width(), TitleBar.TITLEBAR_HEIGHT)
        # 三大金刚按钮大小
        self.m_pMinimizeButton.setFixedSize(TitleBar.MIN_BUTT_SIZE)
        self.m_pMaximizeButton.setFixedSize(TitleBar.MAX_BUTT_SIZE)
        self.m_pCloseButton.setFixedSize(TitleBar.CLOSE_BUTT_SIZE)
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
        self.m_pTitleLabel.setStyleSheet("font-size:13px;margin-bottom:0px;color:%s" % (titletextcolor))
        # 标题栏背景颜色
        self.m_pBackgroundLabel.setStyleSheet("background:%s" % (colorstr))
        # 三大金刚按钮Ui设置
        self.m_pCloseButton.setStyleSheet(
            self.__get_button_imgqss(imageroot, imageclosenorm, imageclosehover, imageclosepress, imageclosepress))
        self.m_pMinimizeButton.setStyleSheet(
            self.__get_button_imgqss(imageroot, imageminnorm, imageminhover, imageminpress, imageminpress))
        self.m_pMaximizeButton.setStyleSheet(
            self.__get_button_imgqss(imageroot, imagemaxnorm, imagemaxhover, imagemaxpress, imagemaxpress))

    def __get_button_imgqss(self, root, norm, hover, press, disable):
        qss = str()
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
        self.m_pMaximizeButton.clicked.emit()  # 双击全屏

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
                    self.m_pMaximizeButton.setStyleSheet(self.__get_button_imgqss(imageroot, imagemaxnorm, imagemaxhover, imagemaxpress, imagemaxpress))
                else:
                    pWindow.showMaximized()
                    self.m_pMaximizeButton.setStyleSheet(self.__get_button_imgqss(imageroot, imageresizenorm, imageresizehover, imageresizepress, imageresizepress))
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
        self.m_pBackgroundLabel.resize(width, TitleBar.TITLEBAR_HEIGHT)

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

# Stretch State
NO_SELECT = 0,  # 鼠标未进入下方矩形区域
LEFT_TOP_RECT = 1  # 鼠标在左上角区域
TOP_BORDER = 2  # 鼠标在上边框区域
RIGHT_TOP_RECT = 3  # 鼠标在右上角区域
RIGHT_BORDER = 4  # 鼠标在右边框区域
RIGHT_BOTTOM_RECT = 5  # 鼠标在右下角区域
BOTTOM_BORDER = 6  # 鼠标在下边框区域
LEFT_BOTTOM_RECT = 7  # 鼠标在左下角区域
LEFT_BORDER = 8  # 鼠标在左边框区域
# 感知拉伸区域
STRETCH_RECT_WIDTH = 4
STRETCH_RECT_HEIGHT = 4


class WindowWithTitleBar(QFrame):
    def __init__(self, mainwidget, colorstr, parent):
        super(WindowWithTitleBar, self).__init__()
        self.m_titlebar = TitleBar(self, colorstr)
        self.initTitlebar(colorstr)
        self.initWidgetsAndPack(mainwidget, self.m_titlebar)
        self.initStretch()

    def initTitlebar(self, color):
        """
        初始化Titlebar
        :param color:
        :return:
        """
        self.m_titlebar = TitleBar(self, color)

    def initWidgetsAndPack(self, mainwidget, titlebar):
        """
        将主体Widget和titleBar拼装起来
        :param mainwidget:
        :param titlebar:
        :return:
        """
        self.mainwidget = mainwidget
        self.resize(mainwidget.width(), mainwidget.height() + TitleBar.TITLEBAR_HEIGHT)
        self.setWindowFlags(Qt.FramelessWindowHint | self.windowFlags())
        self.installEventFilter(self.m_titlebar)
        # 布局: titlbar在上主窗体在下
        pLayout = QVBoxLayout(self)
        pLayout.addWidget(self.m_titlebar)
        pLayout.addWidget(mainwidget)
        pLayout.setSpacing(0)  # 排列的几个widget为0间隔
        pLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(pLayout)

    def initStretch(self):
        """
        初始化拉伸功能
        :return:
        """
        self.setSupportStretch(True)
        self.m_isWindowMax = False
        self.m_stretchRectState = NO_SELECT
        self.m_isMousePressed = False
        self.setMinimumSize(400, 300)

    def setMinimumSize(self, width, height):
        """
        设置拉伸的最小Size
        :param width:
        :param height:
        :return:
        """
        self.m_windowMinWidth = width
        self.m_windowMinHeight = height
        super(WindowWithTitleBar, self).setMinimumSize(width, height)

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

    def showEvent(self, event):
        self.calculateCurrentStrechRect()
        return super().showEvent(event);

    def calculateCurrentStrechRect(self):
        # 四个角Rect
        self.m_leftTopRect = QRect(0, 0, STRETCH_RECT_WIDTH, STRETCH_RECT_HEIGHT)
        self.m_leftBottomRect = QRect(0, self.height() - STRETCH_RECT_HEIGHT, STRETCH_RECT_WIDTH, STRETCH_RECT_WIDTH)
        self.m_rightTopRect = QRect(self.width() - STRETCH_RECT_WIDTH, 0, STRETCH_RECT_WIDTH, STRETCH_RECT_HEIGHT)
        self.m_rightBottomRect = QRect(self.width() - STRETCH_RECT_WIDTH, self.height() - STRETCH_RECT_HEIGHT, STRETCH_RECT_WIDTH, STRETCH_RECT_HEIGHT)
        # 四条边Rect
        self.m_topBorderRect = QRect(STRETCH_RECT_WIDTH, 0, self.width() - STRETCH_RECT_WIDTH * 2, STRETCH_RECT_HEIGHT)
        self.m_rightBorderRect = QRect(self.width() - STRETCH_RECT_WIDTH, STRETCH_RECT_HEIGHT, STRETCH_RECT_WIDTH, self.height() - STRETCH_RECT_HEIGHT * 2)
        self.m_bottomBorderRect = QRect(STRETCH_RECT_WIDTH, self.height() - STRETCH_RECT_HEIGHT, self.width() - STRETCH_RECT_WIDTH * 2, STRETCH_RECT_HEIGHT)
        self.m_leftBorderRect = QRect(0, STRETCH_RECT_HEIGHT, STRETCH_RECT_WIDTH, self.height() - STRETCH_RECT_HEIGHT * 2)

    def getCurrentStretchState(self, cursorPos):
        """
        根据鼠标的位置获取StretchState
        :param cursorPos:
        :return:
        """
        if self.m_leftTopRect.contains(cursorPos):
            stretchState = LEFT_TOP_RECT
        elif self.m_rightTopRect.contains(cursorPos):
            stretchState = RIGHT_TOP_RECT
        elif self.m_rightBottomRect.contains(cursorPos):
            stretchState = RIGHT_BOTTOM_RECT
        elif self.m_leftBottomRect.contains(cursorPos):
            stretchState = LEFT_BOTTOM_RECT
        elif self.m_topBorderRect.contains(cursorPos):
            stretchState = TOP_BORDER
        elif self.m_rightBorderRect.contains(cursorPos):
            stretchState = RIGHT_BORDER
        elif self.m_bottomBorderRect.contains(cursorPos):
            stretchState = BOTTOM_BORDER
        elif self.m_leftBorderRect.contains(cursorPos):
            stretchState = LEFT_BORDER
        else:
            stretchState = NO_SELECT
        return stretchState

    def updateMouseStyle(self, stretchState):
        """
        根据stretchState刷新鼠标的样式
        :param stretchState:
        :return:
        """
        if stretchState == NO_SELECT:
            self.setCursor(Qt.ArrowCursor)
        elif stretchState == LEFT_TOP_RECT:
            self.setCursor(Qt.SizeFDiagCursor)
        elif stretchState == RIGHT_BOTTOM_RECT:
            self.setCursor(Qt.SizeFDiagCursor)
        elif stretchState == TOP_BORDER:
            self.setCursor(Qt.SizeVerCursor)
        elif stretchState == BOTTOM_BORDER:
            self.setCursor(Qt.SizeVerCursor)
        elif stretchState == RIGHT_TOP_RECT:
            self.setCursor(Qt.SizeBDiagCursor)
        elif stretchState == LEFT_BOTTOM_RECT:
            self.setCursor(Qt.SizeBDiagCursor)
        elif stretchState == LEFT_BORDER:
            self.setCursor(Qt.SizeHorCursor)
        elif stretchState == RIGHT_BORDER:
            self.setCursor(Qt.SizeHorCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

    def mouseMoveEvent(self, event):
        """
        重写mouseMoveEvent事件，用于获取当前鼠标的位置，将位置传递给getCurrentStretchState方法，
        得到当前鼠标的状态，然后调用updateMouseStyle对鼠标的样式进行更新
        :param event:
        :return:
        """
        # 如果窗口最大化是不能拉伸的
        # 也不用更新鼠标样式
        if (self.m_isWindowMax):
            return super().mouseMoveEvent(event)
        # 如果当前鼠标未按下，则根据当前鼠标的位置更新鼠标的状态及样式
        if not self.m_isMousePressed:
            cursorPos = event.pos()
            # 根据当前鼠标的位置显示不同的样式
            self.m_stretchRectState = self.getCurrentStretchState(cursorPos)
            self.updateMouseStyle(self.m_stretchRectState)
        # 如果当前鼠标左键已经按下，则记录下第二个点的位置，并更新窗口的大小
        else:
            self.m_endPoint = self.mapToGlobal(event.pos())
            self.updateWindowSize()
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        # 当前鼠标进入了以上指定的8个区域，并且是左键按下时才开始进行窗口拉伸
        if (self.m_stretchRectState != NO_SELECT and event.button() == Qt.LeftButton):
            self.m_isMousePressed = True
            # 记录下当前鼠标位置，为后面计算拉伸位置
            self.m_startPoint = self.mapToGlobal(event.pos())
            # 保存下拉伸前的窗口位置及大小
            self.m_windowRectBeforeStretch = QRect(self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height())
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """
        鼠标松开后意味之窗口拉伸结束，置标志位，并且重新计算用于拉伸的8个区域Rect
        :param event:
        :return:
        """
        self.m_isMousePressed = False
        self.calculateCurrentStrechRect()
        return super().mouseReleaseEvent(event)

    def updateWindowSize(self):
        """
        拉伸窗口过程中，根据记录的坐标更新窗口大小
        :return:
        """
        windowRect = QRect(self.m_windowRectBeforeStretch.x(), self.m_windowRectBeforeStretch.y(),
                           self.m_windowRectBeforeStretch.width(), self.m_windowRectBeforeStretch.height())
        delValue_X = self.m_startPoint.x() - self.m_endPoint.x()
        delValue_Y = self.m_startPoint.y() - self.m_endPoint.y()
        if (self.m_stretchRectState == LEFT_BORDER):
            topLeftPoint = windowRect.topLeft()
            topLeftPoint.setX(topLeftPoint.x() - delValue_X)
            windowRect.setTopLeft(topLeftPoint)
        elif (self.m_stretchRectState == RIGHT_BORDER):
            bottomRightPoint = windowRect.bottomRight()
            bottomRightPoint.setX(bottomRightPoint.x() - delValue_X)
            windowRect.setBottomRight(bottomRightPoint)
        elif (self.m_stretchRectState == TOP_BORDER):
            topLeftPoint = windowRect.topLeft()
            topLeftPoint.setY(topLeftPoint.y() - delValue_Y)
            windowRect.setTopLeft(topLeftPoint)
        elif (self.m_stretchRectState == BOTTOM_BORDER):
            bottomRightPoint = windowRect.bottomRight()
            bottomRightPoint.setY(bottomRightPoint.y() - delValue_Y)
            windowRect.setBottomRight(bottomRightPoint)
        elif (self.m_stretchRectState == LEFT_TOP_RECT):
            topLeftPoint = windowRect.topLeft()
            topLeftPoint.setX(topLeftPoint.x() - delValue_X)
            topLeftPoint.setY(topLeftPoint.y() - delValue_Y)
            windowRect.setTopLeft(topLeftPoint)
        elif (self.m_stretchRectState == RIGHT_TOP_RECT):
            topRightPoint = windowRect.topRight()
            topRightPoint.setX(topRightPoint.x() - delValue_X)
            topRightPoint.setY(topRightPoint.y() - delValue_Y)
            windowRect.setTopRight(topRightPoint)
        elif (self.m_stretchRectState == RIGHT_BOTTOM_RECT):
            bottomRightPoint = windowRect.bottomRight()
            bottomRightPoint.setX(bottomRightPoint.x() - delValue_X)
            bottomRightPoint.setY(bottomRightPoint.y() - delValue_Y)
            windowRect.setBottomRight(bottomRightPoint)
        elif (self.m_stretchRectState == LEFT_BOTTOM_RECT):
            bottomLeftPoint = windowRect.bottomLeft()
            bottomLeftPoint.setX(bottomLeftPoint.x() - delValue_X)
            bottomLeftPoint.setY(bottomLeftPoint.y() - delValue_Y)
            windowRect.setBottomLeft(bottomLeftPoint)
        # 避免宽或高为零窗口显示有误，这里给窗口设置最小拉伸高度、宽度
        if (windowRect.width() < self.m_windowMinWidth):
            windowRect.setLeft(self.geometry().left())
            windowRect.setWidth(self.m_windowMinWidth)
        if (windowRect.height() < self.m_windowMinHeight):
            windowRect.setTop(self.geometry().top())
            windowRect.setHeight(self.m_windowMinHeight)
        self.setGeometry(windowRect)

    def setSupportStretch(self, isSupportStretch):
        """
        设置当前窗口是否支持拉伸
        :param isSupportStretch:
        :return:
        """
        # 因为需要在鼠标未按下的情况下通过mouseMoveEvent事件捕捉鼠标位置，所以需要设置setMouseTracking为True（如果窗口支持拉伸）
        self.m_isSupportStretch = isSupportStretch
        self.setMouseTracking(isSupportStretch)
        # 这里对子控件也进行了设置，是因为如果不对子控件设置，当鼠标移动到子控件上时，不会发送mouseMoveEvent事件，也就获取不到当前鼠标位置，无法判断鼠标状态及显示样式了。
        widgetList = self.findChildren(QWidget)
        for widget in widgetList:
            widget.setMouseTracking(isSupportStretch)
        if (self.m_titlebar is not None):
            # titleBar同理,也需要对自己及子控件进行调用setMouseTracking进行设置，见上方注释
            # self.titleBar.setSupportStretch(isSupportStretch)
            pass

    def getSupportStretch(self):
        """
        返回当前窗口是否支持拉伸
        :return:
        """
        return self.m_isSupportStretch
