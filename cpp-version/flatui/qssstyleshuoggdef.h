#ifndef QSSSTYLESHUOGGDEF_H
#define QSSSTYLESHUOGGDEF_H

#include <QApplication>
#include "qsssetting.h"
#include "titlebar.h"

class QssStyleShuoGGDef
{
public:
    static QString getGreenStyleQss();
    static QString getGreenStyleTitleWindowQss();

    static void setAppGreenStyle(); //一步到位偷懒版


private:
    QssStyleShuoGGDef();
    static QString getTitleWindowQss(const QString &backgroundColor, const QString &borderColor);



};

#endif // QSSSTYLESHUOGGDEF_H
