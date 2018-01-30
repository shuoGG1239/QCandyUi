#include "qsssetting.h"

QString QssSetting::qss="";

const QString QssSetting::WHITE              ="#FFFFFF";
const QString QssSetting::BLACK              ="#000000";
const QString QssSetting::RED                ="#FF0000";
const QString QssSetting::GREEN              ="#00FF00";
const QString QssSetting::BLUE               ="#0000FF";
const QString QssSetting::PURPLE             ="#B23AEE";
const QString QssSetting::WATCHET            ="#1C86EE";
const QString QssSetting::LIGHTGREEN         ="#ECFEFE";
const QString QssSetting::BLUEGREEN          ="#33CCCC";
const QString QssSetting::DEEPBLUEGREEN      ="#015F5F";
const QString QssSetting::DARKBLUEGREEN      ="#28AAAA";
const QString QssSetting::GRAY               ="#999999";
const QString QssSetting::LIGHTGRAY          ="#CCCCCC";


QssSetting::QssSetting()
{
}



/**
 * @brief 全局字体设置(所有继承于QObject的控件都会受到影响)
 *
 * @param fontname
 * @return QString
 */
QString QssSetting::getFontQss(const QString &fontname,const QString &fontcolor)
{
    QStringList qss;
    qss.append(QString("QObject{font-family:%1;color:%2}").arg(fontname).arg(fontcolor));
    return qss.join("");
}

/**
 * @brief pushbutton的Qss生成
 *
 * @param normalColor
 * @param normalTextColor
 * @param hoverColor
 * @param hoverTextColor
 * @param pressedColor
 * @param pressedTextColor
 * @return QString QssStr
 */
QString QssSetting::getPushButtonQss(const QString &normalColor, const QString &normalTextColor,
                        const QString &hoverColor, const QString &hoverTextColor,
                        const QString &pressedColor, const QString &pressedTextColor,
                        const QString &disableColor, const QString &disableTextColor)
{
    QStringList qss;
    qss.append(QString("QPushButton{padding:0px;border-radius:5px;color:%1;background:%2;border:2px solid %3;}")\
               .arg(normalTextColor).arg(normalColor).arg(normalColor));
    qss.append(QString("QPushButton:hover{color:%1;background:%2;}").arg(hoverTextColor).arg(hoverColor));
    qss.append(QString("QPushButton:pressed{color:%1;background:%2;}").arg(pressedTextColor).arg(pressedColor));
    qss.append(QString("QPushButton:disabled{color:%1;background:%2;}").arg(disableTextColor).arg(disableColor));
    return qss.join("");
}


/**
 * @brief Lineedit的Qss生成
 *
 * @param normalColor
 * @param focusColor 编辑框focus时的颜色
 * @return QString QssStr
 */
QString QssSetting::getLineeditQss(const QString &normalColor, const QString &focusColor)
{
    QStringList qss;
    qss.append(QString("QLineEdit{border-style:none;padding:2px;border-radius:5px;border:2px solid %1;"
                       "selection-color:%2;selection-background-color:%3;}")
               .arg(normalColor).arg(QssSetting::WHITE).arg(focusColor));
    qss.append(QString("QLineEdit:focus{border:2px solid %1;}").arg(focusColor));
    qss.append(QString("QLineEdit:disabled{color:%1;}").arg(QssSetting::LIGHTGRAY)); //被disable时
    return qss.join("");
}

/**
 * @brief PlainTextEdit的Qss生成
 *
 * @param normalColor
 * @param focusColor
 * @return QString QssStr
 */
QString QssSetting::getPlaineditQss(const QString &normalColor, const QString &focusColor)
{
    QStringList qss;
    qss.append(QString("QPlainTextEdit{border-style:none;padding:2px;border-radius:5px;border:2px solid %1;"
                       "font-family:宋体;selection-color:%2;selection-background-color:%3}")
               .arg(normalColor).arg(QssSetting::WHITE).arg(focusColor));
    qss.append(QString("QPlainTextEdit:focus{border:2px solid %1;}").arg(focusColor));
    return qss.join("");
}

/**
 * @brief comboBox的Qss生成
 *
 * @param backgroundColor
 * @param normalColor
 * @param focusColor 编辑框focus时的颜色
 * @return QString QssStr
 */
QString QssSetting::getComboxQss(const QString &backgroundColor,const QString &normalColor,
                                 const QString &focusColor,const QString &arrowimageurl)
{
    QStringList qss;
    qss.append(QString("QComboBox{background:%1;padding:2px;border-radius:5px;border:2px solid %2;}")
               .arg(backgroundColor).arg(normalColor));
    qss.append(QString("QComboBox:focus{border:2px solid %1;}").arg(focusColor));
    qss.append(QString("QComboBox:on{border:2px solid %1;}").arg(focusColor));//下拉时
    qss.append(QString("QComboBox:disabled{color:%1;}").arg(QssSetting::LIGHTGRAY)); //被disable时
    qss.append(QString("QComboBox::drop-down{border-style:solid;}"));//可以被点击的倒三角按钮
    qss.append(QString("QComboBox QAbstractItemView{border:2px solid %1;border-radius:5px;background:transparent;selection-background-color:%2;}")
               .arg(focusColor).arg(focusColor));
    qss.append(QString("QComboBox::down-arrow{image:url(%1)}").arg(arrowimageurl)); //倒三角
    return qss.join("");
}

/**
 * @brief ProgressBar的Qss生成
 *
 * @param normalColor
 * @param chunkColor
 * @return QString QssStr
 */
QString QssSetting::getProgressBarQss(const QString &normalColor, const QString &chunkColor)
{
    int barHeight = 8;
    int barRadius = 8;

    QStringList qss;
    qss.append(QString("QProgressBar{font:9pt;height:%2px;background:%1;border-radius:%3px;text-align:center;border:1px solid %1;}")
               .arg(normalColor).arg(barHeight).arg(barRadius));
    qss.append(QString("QProgressBar:chunk{border-radius:%2px;background-color:%1;}").arg(chunkColor).arg(barRadius));
    return qss.join("");
}


/**
 * @brief Slider的Qss生成
 *
 * @param normalColor
 * @param grooveColor 凹槽颜色
 * @param handleColor
 * @return QString QssStr
 */
QString QssSetting::getSliderQss(const QString &normalColor, const QString &grooveColor,
                                 const QString &handleColor)
{
    int sliderHeight = 8;
    int sliderRadius = 4;
    int handleWidth  = 13;
    int handleRadius = 6;
    int handleOffset = 3;

    QStringList qss;
    qss.append(QString("QSlider::groove:horizontal,QSlider::add-page:horizontal{height:%2px;border-radius:%3px;background:%1;}")
               .arg(normalColor).arg(sliderHeight).arg(sliderRadius));
    qss.append(QString("QSlider::sub-page:horizontal{height:%2px;border-radius:%3px;background:%1;}")
               .arg(grooveColor).arg(sliderHeight).arg(sliderRadius));
    qss.append(QString("QSlider::handle:horizontal{width:%2px;margin-top:-%3px;margin-bottom:-%3px;border-radius:%4px;"
                       "background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 %1);}")
               .arg(handleColor).arg(handleWidth).arg(handleOffset).arg(handleRadius));
    return qss.join("");
}



/**
 * @brief RadioButton的Qss生成
 *
 * @param normimageurl
 * @param downimageurl
 * @param normimageurlhover
 * @param downimageurlhover
 * @return QString QssStr
 */
QString QssSetting::getRadioButtonQss(const QString &normimageurl, const QString &downimageurl,
                                      const QString &normimageurlhover,const QString &downimageurlhover)
{
    QStringList qss;
    qss.append(QString("QRadioButton::indicator{width:15px;height:15px;}")); //图片压缩到15x15pixel
    qss.append(QString("QRadioButton::indicator:unchecked{image: url(%1);}").arg(normimageurl));
    qss.append(QString("QRadioButton::indicator:checked{image: url(%1);}").arg(downimageurl));
    qss.append(QString("QRadioButton::indicator:unchecked:hover{image: url(%1);}").arg(normimageurlhover));
    qss.append(QString("QRadioButton::indicator:checked:hover{image: url(%1);}").arg(downimageurlhover));
    return qss.join("");
}


/**
 * @brief CheckBox的Qss生成
 *
 * @param normimageurl
 * @param checkimageurl
 * @param normimageurlhover
 * @param checkimageurlhover
 * @return QString QssStr
 */
QString QssSetting::getCheckBoxQss(const QString &normimageurl, const QString &checkimageurl,
                                      const QString &normimageurlhover,const QString &checkimageurlhover)
{
    QStringList qss;
    qss.append(QString("QCheckBox::indicator{width:15px;height:15px;}")); //图片压缩到15x15pixel
    qss.append(QString("QCheckBox::indicator:unchecked{image: url(%1);}").arg(normimageurl));
    qss.append(QString("QCheckBox::indicator:checked{image: url(%1);}").arg(checkimageurl));
    qss.append(QString("QCheckBox::indicator:unchecked:hover{image: url(%1);}").arg(normimageurlhover));
    qss.append(QString("QCheckBox::indicator:checked:hover{image: url(%1);}").arg(checkimageurlhover));
    return qss.join("");
}


/**
 * @brief TabWidget的Qss生成
 *
 * @param normalTabColor
 * @param normalTabTextColor
 * @return QString QssStr
 */
QString QssSetting::getTabWidgetQss(const QString &normalTabColor, const QString &normalTabTextColor)
{
    QStringList qss;
    qss.append(QString("QTabWidget{color:%1; background:%2;border:none}").arg(normalTabTextColor).arg(normalTabColor));
    qss.append(QString("QTabWidget::tab-bar{left:5px}"));
    qss.append(QString("QTabBar::tab{color:%1; background:%2;width:100px;height:25px;border-radius:2px}").arg(normalTabTextColor).arg(normalTabColor));
    qss.append(QString("QTabBar::tab:hover{color:%1; background:%2;}").arg(normalTabColor).arg(normalTabTextColor));
    qss.append(QString("QTabBar::tab:selected{color:%1; background:%2;}").arg(normalTabColor).arg(normalTabTextColor));
    return qss.join("");
}


/**
 * @brief Scrollbar的Qss生成
 *
 * @param handlebarcolor
 * @return QString QssStr
 */
QString QssSetting::getScrollbarQss(const QString &handlebarcolor)
{
    QStringList qss;
    qss.append(QString("QScrollBar{background:transparent;width:10px;padding-top:11px;padding-bottom:11px}"));
    qss.append(QString("QScrollBar::handle{background:%1;border-radius:5px;min-height:10px}").arg(handlebarcolor));
    qss.append(QString("QScrollBar::handle:pressed{background:%1}").arg(QssSetting::GRAY));
    return qss.join("");
}


/**
 * @brief 清空qss字符串
 *
 */
void QssSetting::clearQssStr()
{
    qss="";
}


