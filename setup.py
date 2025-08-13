from setuptools import setup
from FreezeUI_U import __version__ as ver

DESCRIPTION = 'This a GUI for converting python scripts to applications using cx_Freeze.'
LONG_DESCRIPTION = open("README.md", encoding="utf-8").read()

setup(
    name="FreezeUI_U",
    version=ver,
    author="Akshat Chauhan",
    author_email="coder.akshatch@gmail.com",
    license='GNU GPL v3',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    install_requires=["PyQt6", "cx_Freeze", "qtconsole", "pyqt6-qscintilla ", "plyer"],
    python_requires = ">=3.9",
    packages=['FreezeUI_U'],
    data_files=[('bitmaps', ['FreezeUI_U/assets/icon.gif','FreezeUI_U/assets/icon.ico','FreezeUI_U/assets/msi_text.png','FreezeUI_U/assets/exe_text.png','FreezeUI_U/assets/pyicon.svg']),("text files",["FreezeUI_U/assets/msi_template.txt","FreezeUI_U/assets/exe_template.txt"])],
    include_package_data=True,
    url="https://akshatchauhan18.github.io/FreezeUI",
    keywords=['python', 'gui', 'cx_Freeze', 'FreezeUI'],
    extras_require = {"dev":["pytest == 6.2.4"]},
    classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Operating System :: Microsoft :: Windows',
    ],
    entry_points={
        "console_scripts": [
            "freezeui-exe = FreezeUI_U.__main__:create_exe",
            "freezeui-msi = FreezeUI_U.__main__:create_msi"
        ],
    }
)
