from setuptools import setup

setup(
    name="QCandyUi",       
    version="0.11",   
    description="quick beautify your pyQt5 app",
    keywords='python pyQt ui',
    author='shuoGG',
    author_email='328893769@qq.com',
    url='https://github.com/shuoGG1239/QCandyUi',
    packages=['QCandyUi'],
    include_package_data=True,
    zip_safe=False,
    install_requires= [
        'pywin32'
    ]
)
