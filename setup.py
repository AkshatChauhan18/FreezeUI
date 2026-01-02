from setuptools import setup
from FreezeUI import __version__ as ver

DESCRIPTION = "Convert .py to .exe/.msi using GUI and cx_Freeze"
LONG_DESCRIPTION = open("README.md", encoding="utf-8").read()

setup(
    name="FreezeUI_U",
    version=ver,
    author="Akshat Chauhan",
    author_email="coder.akshatch@gmail.com",
    license="GNU GPL v3",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=["PyQt6", "cx_Freeze", "qtconsole", "pyqt6-qscintilla ", "plyer"],
    python_requires=">=3.9",
    packages=["FreezeUI_U"],
    data_files=[
        (
            "freeze_ui_assets",
            [
                "FreezeUI_U/assets/icon_text.png",
                "FreezeUI_U/assets/editor.svg",
                "FreezeUI_U/assets/exe_icon.svg",
                "FreezeUI_U/assets/exe.svg",
                "FreezeUI_U/assets/icon_text.svg",
                "FreezeUI_U/assets/icon.svg",
                "FreezeUI_U/assets/icon.ico",
                "FreezeUI_U/assets/menu.svg",
                "FreezeUI_U/assets/msi_icon.svg",
                "FreezeUI_U/assets/msi.svg",
                "FreezeUI_U/assets/Varela_Round/VarelaRound.ttf",
                "FreezeUI_U/assets/msi_template.txt",
                "FreezeUI_U/assets/exe_template.txt",
                "FreezeUI_U/assets/main.ui",
            ],
        )
    ],
    include_package_data=True,
    url="https://akshatchauhan18.github.io/FreezeUI",
    keywords=["python", "gui", "cx_Freeze", "FreezeUI"],
    extras_require={"dev": ["pytest == 6.2.4"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        "console_scripts": [
            "freezeui = FreezeUI_U.__main__:open_ui",
        ],
    },
)
