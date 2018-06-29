import os

color_theme = 'blue_green'

# 这些图片路径是相对main.py的, 而不是相对本py文件的
# 下面这些图片资源是TitleBar的
imageclosenorm = color_theme + "/" + "close.png"
imageclosehover = color_theme + "/" + "closehover.png"
imageclosepress = color_theme + "/" + "closepress.png"
imagemaxnorm = color_theme + "/" + "maxsize.png"
imagemaxhover = color_theme + "/" + "maxsizehover.png"
imagemaxpress = color_theme + "/" + "maxsizepress.png"
imageminnorm = color_theme + "/" + "minsize.png"
imageminhover = color_theme + "/" + "minsizehover.png"
imageminpress = color_theme + "/" + "minsizepress.png"
imageresizenorm = color_theme + "/" + "resize.png"
imageresizehover = color_theme + "/" + "resizehover.png"
imageresizepress = color_theme + "/" + "resizepress.png"

# 资源路径: 相对路径没找到就去安装路径下找
imageroot = './qss_ui_theme/FlatUiSrcImage/'
if not os.path.exists(imageroot + imageclosenorm):
    imageroot = (os.path.split(__file__)[0] + "\\FlatUiSrcImage\\").replace('\\', '/')
