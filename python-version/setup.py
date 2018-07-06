from setuptools import setup

setup(
    name="QCandyUi",        # 包名
    version="0.1",          # 版本信息
    packages=['QCandyUi'],  # 要打包的项目文件夹
    include_package_data=True,
    install_requires= [
        'pywin32'
    ]
)
