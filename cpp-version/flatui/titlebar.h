/*-----------------------------------------------------------------------------------------
 *                                  使用帮助
 * WindowWithTitleBar:
 *              使用须知:导入的主窗体要用new,不要用栈的
 *              使用方法:
 *                        TabWidget *utwindow=new TabWidget();
 *                        WindowWithTitleBar mainwindow(utwindow,QssSetting::DARKBLUEGREEN);
 *                        mainwindow.setWindowTitle("UtTestTool");
 *                        mainwindow.setWindowIcon(QIcon("shuoGG_re.ico"));
 *
 *
 *  TitleBar
 *
------------------------------------------------------------------------------------------*/


#ifndef TITLEBAR_H
#define TITLEBAR_H

#include <QWidget>
#include <QFrame>
#include <QSize>
#include <QIcon>
#include "qsssetting.h"

class QLabel;
class QPushButton;

/*----------------------------------------------------------------------------
 *
 *                                  TitleBar
 *
------------------------------------------------------------------------------*/
class TitleBar : public QWidget
{
    Q_OBJECT
public:
    explicit TitleBar(QWidget *parent, const QString &colorid);
    ~TitleBar();
    void setMaximumEnable(bool isenable);

    static const int titlebarHeight=30;
    static const QString imageroot;

protected:
    // 双击标题栏进行界面的最大化/还原
    virtual void mouseDoubleClickEvent(QMouseEvent *event);
    // 进行鼠界面的拖动
    virtual void mousePressEvent(QMouseEvent *event);
    // 设置界面标题与图标
    virtual bool eventFilter(QObject *obj, QEvent *event);

private slots:
    // 进行最小化、最大化/还原、关闭操作
    void onClicked();

private:
    // 最大化/还原
    void updateMaximize();
    //设置背景label的大小
    void setTitlebarSize(const QSize &size);

    QWidget *parentwidget;
    static const QString titletextcolor;
    static const QString imageclosenorm;
    static const QString imageclosehover;
    static const QString imageclosepress;
    static const QString imagemaxnorm;
    static const QString imagemaxhover;
    static const QString imagemaxpress;
    static const QString imageminnorm;
    static const QString imageminhover;
    static const QString imageminpress;
    static const QString imageresizenorm;
    static const QString imageresizehover;
    static const QString imageresizepress;



private:
    QLabel *m_pIconLabel;
    QLabel *m_pTitleLabel;
    QLabel *m_pBackgroundLabel;
    QPushButton *m_pMinimizeButton;
    QPushButton *m_pMaximizeButton;
    QPushButton *m_pCloseButton;
};

/*----------------------------------------------------------------------------
 *
 *                          WindowWithTitleBar
 *
------------------------------------------------------------------------------*/

class TabWidget;
class WindowWithTitleBar : public QFrame
{
    Q_OBJECT
public:
    explicit WindowWithTitleBar(QWidget *mainwidget,const QString &colorstr,QWidget *parent=0);
    ~WindowWithTitleBar();
    void setWindowRadius(int npx);
    void setBackgroundBorderColor(const QString &bgdcolor,const QString &bordercolor);
private:
    TitleBar *titlebar;

};


#endif // TITLEBAR_H
