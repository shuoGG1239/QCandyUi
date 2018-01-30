#include <QLabel>
#include <QPushButton>
#include <QHBoxLayout>
#include <QEvent>
#include <QMouseEvent>
#include <QApplication>
#include <QStringList>
#include <QPainter>
#include <QBitmap>
#include "titlebar.h"

#ifdef Q_OS_WIN
//#pragma comment(lib, "user32.lib")
#include <qt_windows.h>
#endif
const QString TitleBar::titletextcolor        ="white";
const QString TitleBar::imageroot             =":/image/flatui/FlatUiSrcImage/";
const QString TitleBar::imageclosenorm        ="close.png";
const QString TitleBar::imageclosehover       ="closehover.png";
const QString TitleBar::imageclosepress       ="closepress.png";
const QString TitleBar::imagemaxnorm          ="maxsize.png";
const QString TitleBar::imagemaxhover         ="maxsizehover.png";
const QString TitleBar::imagemaxpress         ="maxsizepress.png";
const QString TitleBar::imageminnorm          ="minsize.png";
const QString TitleBar::imageminhover         ="minsizehover.png";
const QString TitleBar::imageminpress         ="minsizepress.png";
const QString TitleBar::imageresizenorm       ="resize.png";
const QString TitleBar::imageresizehover      ="resizehover.png";
const QString TitleBar::imageresizepress      ="resizepress.png";

/**
 * @brief TitleBar构造函数
 *
 * @param parent 被加标题栏的widget
 * @param colorid 标题栏的底色
 */
TitleBar::TitleBar(QWidget *parent,const QString &colorid)
    : QWidget(parent)
{
    QStringList qss;
    parentwidget=parent;
    setFixedHeight(titlebarHeight);
    m_pBackgroundLabel = new QLabel(this);
    m_pIconLabel = new QLabel(this);
    m_pTitleLabel = new QLabel(this);
    m_pMinimizeButton = new QPushButton(this);
    m_pMaximizeButton = new QPushButton(this);
    m_pCloseButton = new QPushButton(this);

    m_pIconLabel->setFixedSize(20, 20);
    m_pIconLabel->setScaledContents(true);

    m_pTitleLabel->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
    m_pBackgroundLabel->resize(parentwidget->width(),titlebarHeight);
    /*三大金刚按钮大小*/
    m_pMinimizeButton->setFixedSize(27, 22);
    m_pMaximizeButton->setFixedSize(27, 22);
    m_pCloseButton->setFixedSize(27, 22);
    m_pMaximizeButton->setEnabled(false);

    m_pTitleLabel->setObjectName("whiteLabel");
    m_pMinimizeButton->setObjectName("minimizeButton");
    m_pMaximizeButton->setObjectName("maximizeButton");
    m_pCloseButton->setObjectName("closeButton");

    QHBoxLayout *pLayout = new QHBoxLayout(this);
    pLayout->addWidget(m_pIconLabel);
    pLayout->addSpacing(5);
    pLayout->addWidget(m_pTitleLabel);
    pLayout->addWidget(m_pMinimizeButton);
    pLayout->addWidget(m_pMaximizeButton);
    pLayout->addWidget(m_pCloseButton);
    pLayout->setSpacing(0);
    pLayout->setContentsMargins(5, 0, 5, 0);
    setLayout(pLayout);

    connect(m_pMinimizeButton, SIGNAL(clicked(bool)), this, SLOT(onClicked()));
    connect(m_pMaximizeButton, SIGNAL(clicked(bool)), this, SLOT(onClicked()));
    connect(m_pCloseButton, SIGNAL(clicked(bool)), this, SLOT(onClicked()));

    //标题字体颜色
    m_pTitleLabel->setStyleSheet(QString("font-size:13px;margin-bottom:0px;color:%1").arg(titletextcolor));
    //标题栏背景颜色
    m_pBackgroundLabel->setStyleSheet(QString("background:%1").arg(colorid));
    /*右上角三大金刚按钮Ui设置*/
    qss.append(QString("QPushButton{background:transparent; background-image:url(%1); border:none}")
               .arg(imageroot+imageclosenorm));
    qss.append(QString("QPushButton:hover{background:transparent; background-image:url(%1)}")
               .arg(imageroot+imageclosehover));
    qss.append(QString("QPushButton:pressed{background:transparent; background-image:url(%1)}")
               .arg(imageroot+imageclosepress));
    qss.append(QString("QPushButton:disabled{background:transparent; background-image:url(%1)}")
               .arg(imageroot+imageclosepress));
    m_pCloseButton->setStyleSheet(qss.join(""));
    qss.clear();
    qss.append(QString("QPushButton{background:transparent; background-image:url(%1); border:none}")
               .arg(imageroot+imageminnorm));
    qss.append(QString("QPushButton:hover{background:transparent; background-image:url(%1)}")
               .arg(imageroot+imageminhover));
    qss.append(QString("QPushButton:pressed{background:transparent; background-image:url(%1)}")
               .arg(imageroot+imageminpress));
    qss.append(QString("QPushButton:disabled{background:transparent; background-image:url(%1)}")
               .arg(imageroot+imageminpress));
    m_pMinimizeButton->setStyleSheet(qss.join(""));
    qss.clear();
    qss.append(QString("QPushButton{background:transparent; background-image:url(%1); border:none}")
               .arg(imageroot+imagemaxnorm));
    qss.append(QString("QPushButton:hover{background:transparent; background-image:url(%1)}")
               .arg(imageroot+imagemaxhover));
    qss.append(QString("QPushButton:pressed{background:transparent; background-image:url(%1)}")
               .arg(imageroot+imagemaxpress));
    qss.append(QString("QPushButton:disabled{background:transparent; background-image:url(%1)}")
               .arg(imageroot+imagemaxpress));
    m_pMaximizeButton->setStyleSheet(qss.join(""));
    qss.clear();
}

TitleBar::~TitleBar()
{

}

void TitleBar::mouseDoubleClickEvent(QMouseEvent *event)
{
    Q_UNUSED(event);
    emit m_pMaximizeButton->clicked();
}

void TitleBar::mousePressEvent(QMouseEvent *event)
{
#ifdef Q_OS_WIN
    if (ReleaseCapture())
    {
        QWidget *pWindow = this->window();
        if (pWindow->isTopLevel())
        {
            SendMessage(HWND(pWindow->winId()), WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0);
        }
    }
    event->ignore();
#else
#endif
}

bool TitleBar::eventFilter(QObject *obj, QEvent *event)
{
    switch ((int)event->type())
    {
    case QEvent::WindowTitleChange:
    {
        QWidget *pWidget = qobject_cast<QWidget *>(obj);
        if (pWidget)
        {
            m_pTitleLabel->setText(pWidget->windowTitle());
            return true;
        }
    }
    case QEvent::WindowIconChange:
    {
        QWidget *pWidget = qobject_cast<QWidget *>(obj);
        if (pWidget)
        {
            QIcon icon = pWidget->windowIcon();
            m_pIconLabel->setPixmap(icon.pixmap(m_pIconLabel->size()));
            return true;
        }
    }
    case QEvent::WindowStateChange:
    case QEvent::Resize:
        updateMaximize();
        setTitlebarSize(parentwidget->size());
        return true;
    }
    return QWidget::eventFilter(obj, event);
}

/**
 * @brief 三大金刚按键的clicked slot
 *
 */
void TitleBar::onClicked()
{
    QPushButton *pButton = qobject_cast<QPushButton *>(sender());
    QWidget *pWindow = this->window();
    if (pWindow->isTopLevel())
    {
        if (pButton == m_pMinimizeButton)
        {
            pWindow->showMinimized();
        }
        else if (pButton == m_pMaximizeButton)
        {
            if(pWindow->isMaximized())
            {
                pWindow->showNormal();
                m_pMaximizeButton->setStyleSheet(QString("QPushButton{background:transparent; background-image:url(%1); border:none}"
                                                         "QPushButton:hover{background-image:url(%2)}"
                                                         "QPushButton:pressed{background-image:url(%3)}")
                                                 .arg(imageroot+imagemaxnorm)
                                                 .arg(imageroot+imagemaxhover)
                                                 .arg(imageroot+imagemaxpress));
            }
            else
            {
                pWindow->showMaximized();
                m_pMaximizeButton->setStyleSheet(QString("QPushButton{background:transparent; background-image:url(%1); border:none}"
                                                         "QPushButton:hover{background-image:url(%2)}"
                                                         "QPushButton:pressed{background-image:url(%3)}")
                                                 .arg(imageroot+imageresizenorm)
                                                 .arg(imageroot+imageresizehover)
                                                 .arg(imageroot+imageresizepress));
            }

        }
        else if (pButton == m_pCloseButton)
        {
            pWindow->close();
        }
    }
}

void TitleBar::updateMaximize()
{
    QWidget *pWindow = this->window();
    if (pWindow->isTopLevel())
    {
        bool bMaximize = pWindow->isMaximized();
        if (bMaximize)
        {
            m_pMaximizeButton->setProperty("maximizeProperty", "restore");
        }
        else
        {
            m_pMaximizeButton->setProperty("maximizeProperty", "maximize");
        }
        m_pMaximizeButton->setStyle(QApplication::style());
    }
}


void TitleBar::setTitlebarSize(const QSize &size)
{
    this->m_pBackgroundLabel->resize(size.width(),titlebarHeight);
}

void TitleBar::setMaximumEnable(bool isenable)
{
    this->m_pMaximizeButton->setEnabled(isenable);
}



/***********************************************************************


                           WindowWithTitleBar


************************************************************************/
WindowWithTitleBar::WindowWithTitleBar(QWidget *mainwidget,const QString &colorstr,QWidget *parent)
    :QFrame(parent)
{
    this->resize(mainwidget->width(),mainwidget->height()+TitleBar::titlebarHeight);
    titlebar=new TitleBar(this,colorstr);
    setWindowFlags(Qt::FramelessWindowHint | windowFlags());
    installEventFilter(titlebar);
    /*布局: titlbar在上 主窗体在下*/
    QVBoxLayout *pLayout = new QVBoxLayout(this);
    pLayout->addWidget(titlebar);
    pLayout->addWidget(mainwidget);
    pLayout->setSpacing(0);  //排列的几个widget为0间隔
    pLayout->setContentsMargins(0, 0, 0, 0);
    setLayout(pLayout);
}

WindowWithTitleBar::~WindowWithTitleBar()
{
}

/**
 * @brief 圆边
 *
 * @param npx 弧度
 */
void WindowWithTitleBar::setWindowRadius(int npx)
{
    QBitmap objBitmap(this->size());
    QPainter painter(&objBitmap);
    painter.setBrush(QColor(0,0,0));
    painter.drawRoundedRect(this->rect(),npx,npx);
    this->setMask(objBitmap);

}

/**
 * @brief 设置主窗口的背景颜色和border颜色
 *
 * @param bgdcolor
 * @param bordercolor
 */
void WindowWithTitleBar::setBackgroundBorderColor(const QString &bgdcolor,const QString &bordercolor)
{
    this->setStyleSheet(QString("WindowWithTitleBar{background:%1;border:3px solid %2}")
                        .arg(bgdcolor).arg(bordercolor));
}

