#ifndef QSSSETTING_H
#define QSSSETTING_H

#include <QString>
#include <QStringList>
#include <QPushButton>
#include <QLineEdit>
#include <QProgressBar>
#include <QSlider>

class QssSetting
{
public:
    static QString getFontQss(const QString &fontname, const QString &fontcolor);

    static QString getPushButtonQss(const QString &normalColor, const QString &normalTextColor,
                            const QString &hoverColor, const QString &hoverTextColor,
                            const QString &pressedColor, const QString &pressedTextColor,
                            const QString &disableColor, const QString &disableTextColor);

    static QString getLineeditQss(const QString &normalColor, const QString &focusColor);

    static QString getPlaineditQss(const QString &normalColor, const QString &focusColor);

    static QString getComboxQss(const QString &backgroundColor,const QString &normalColor,
                                const QString &focusColor, const QString &arrowimageurl);

    static QString getProgressBarQss(const QString &normalColor, const QString &chunkColor);

    static QString getSliderQss(const QString &normalColor, const QString &grooveColor,
                                const QString &handleColor);

    static QString getRadioButtonQss(const QString &normimageurl, const QString &downimageurl,
                                     const QString &normimageurlhover, const QString &downimageurlhover);

    static QString getCheckBoxQss(const QString &normimageurl, const QString &checkimageurl,
                                  const QString &normimageurlhover,const QString &checkimageurlhover);

    static QString getTabWidgetQss(const QString &normalTabColor, const QString &normalTabTextColor);

    static QString getScrollbarQss(const QString &handlebarcolor);

    static void clearQssStr();


    static const QString BLACK;
    static const QString WHITE;
    static const QString RED;
    static const QString GREEN;
    static const QString BLUE;
    static const QString PURPLE;
    static const QString WATCHET;
    static const QString LIGHTGREEN;
    static const QString BLUEGREEN;
    static const QString DEEPBLUEGREEN;
    static const QString DARKBLUEGREEN;
    static const QString GRAY;
    static const QString LIGHTGRAY;

    static QString qss;

private:
        QssSetting();
};

#endif // QSSSETTING_H
