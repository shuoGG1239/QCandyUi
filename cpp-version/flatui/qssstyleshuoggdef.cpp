#include "qssstyleshuoggdef.h"

QssStyleShuoGGDef::QssStyleShuoGGDef()
{
}


/**
 * @brief 将整个application的style设为green风格, 一步搞定, 尽量往后边放
 *
 */
void QssStyleShuoGGDef::setAppGreenStyle()
{
    qApp->setStyleSheet(QssStyleShuoGGDef::getGreenStyleTitleWindowQss());
}

/**
 * @brief 获取蓝绿色主题Qss
 *
 * @return QString
 */
QString QssStyleShuoGGDef::getGreenStyleQss()
{
    QssSetting::clearQssStr();
    QssSetting::qss += QssSetting::getFontQss("微软雅黑",QssSetting::DEEPBLUEGREEN);
    QssSetting::qss += QssSetting::getPushButtonQss(QssSetting::BLUEGREEN,QssSetting::WHITE,QssSetting::LIGHTGREEN,
                                                    QssSetting::BLUEGREEN,QssSetting::LIGHTGRAY,QssSetting::WHITE,
                                                    QssSetting::GRAY,QssSetting::LIGHTGRAY);
    QssSetting::qss += QssSetting::getPlaineditQss(QssSetting::LIGHTGRAY,QssSetting::BLUEGREEN);
    QssSetting::qss += QssSetting::getLineeditQss(QssSetting::LIGHTGRAY,QssSetting::BLUEGREEN);
    QssSetting::qss += QssSetting::getComboxQss(QssSetting::WHITE,QssSetting::LIGHTGRAY,
                                                QssSetting::BLUEGREEN,TitleBar::imageroot+"bluearrow.png");
    QssSetting::qss += QssSetting::getRadioButtonQss(TitleBar::imageroot+"radio_normal.png",TitleBar::imageroot+"radio_down.png",
                                                     TitleBar::imageroot+"radio_hoverUncheck.png",TitleBar::imageroot+"radio_hoverCheck.png");
    QssSetting::qss += QssSetting::getCheckBoxQss(TitleBar::imageroot+"checkbox_normal.png",TitleBar::imageroot+"checkbox_down.png",
                                                  TitleBar::imageroot+"checkbox_hoverUncheck.png",TitleBar::imageroot+"checkbox_hoverCheck.png");
    QssSetting::qss += QssSetting::getTabWidgetQss(QssSetting::BLUEGREEN,QssSetting::WHITE);
    QssSetting::qss += QssSetting::getSliderQss(QssSetting::BLUEGREEN,QssSetting::WHITE,QssSetting::BLUEGREEN);
    QssSetting::qss += QssSetting::getScrollbarQss(QssSetting::BLUEGREEN);
    return QssSetting::qss;
}


/**
 * @brief 获取带自定义WindowTitleBar的蓝绿色主题Qss
 *
 * @return QString
 */
QString QssStyleShuoGGDef::getGreenStyleTitleWindowQss()
{
    QssSetting::clearQssStr();
    QssSetting::qss += QssStyleShuoGGDef::getGreenStyleQss();
    QssSetting::qss += QssStyleShuoGGDef::getTitleWindowQss(QssSetting::WHITE,QssSetting::DARKBLUEGREEN);

    return QssSetting::qss;
}


/**
 * @brief 设置并获取WindowTitle的Qss
 *
 * @param backgroundColor
 * @param borderColor
 * @return QString
 */
QString QssStyleShuoGGDef::getTitleWindowQss(const QString &backgroundColor, const QString &borderColor)
{
    QString qssStr = (QString("WindowWithTitleBar{background:%1;border:3px solid %2}").arg(backgroundColor).arg(borderColor));
    return qssStr;
}

