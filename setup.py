

from setuptools import setup
from FreezeUI import __version__ as ver

DESCRIPTION = 'This a GUI for converting python scripts to applications using cx_Freeze.'
LONG_DESCRIPTION = open("README.md", encoding="utf-8").read()

setup(
    name="FreezeUI",
    version=ver,
    author="Akshat Chauhan",
    author_email="akki.coder@gmail.com",
    license='GNU GPL v3',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    install_requires=["PyQt5 <= 5.15.4", "cx_Freeze <= 6.7", "python_version <=3.6",
                      "QtPy <= 1.10.0", "qtconsole <= 5.1.1", "qscintilla <= 2.13.0", "plyer <= 2.0.0"],
    packages=['FreezeUI'],
    data_files=[('bitmaps', ['FreezeUI/assets/icon.gif','FreezeUI/assets/icon.ico','FreezeUI/assets/msi_text.png','FreezeUI/assets/exe_text.png','FreezeUI/assets/pyicon.svg']),("text files",["FreezeUI/assets/msi_template.txt","FreezeUI/assets/exe_template.txt"])],
    include_package_data=True,
    url="https://akshatchauhan18.github.io/FreezeUI",
    keywords=['python', 'gui', 'cx_Freeze', 'FreezeUI'],
    extras_require = {"dev":["pytest == 6.2.4"]},
    classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: Education'
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Operating System :: Microsoft :: Windows',
    ],
    entry_points={
        "console_scripts": [
            "freezeui-exe = FreezeUI.__main__:create_exe",
            "freezeui-msi = FreezeUI.__main__:create_msi"
        ],
    }
)
