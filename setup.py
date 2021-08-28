# TODO: add author homepage

from setuptools import setup
from FreezeUI import __version__ as ver
 
DESCRIPTION = 'This a GUI for converting python scripts to applications using cx_Freeze.'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

setup(
        name="FreezeUI", 
        version=ver,
        author="Akshat Chauhan",
        author_email="akki.coder@gmail.com",
        license='GNU GPL v3',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        install_requires=["PyQt5","cx_Freeze","python_version <=3.6","QtPy","qtconsole","qscintilla","plyer"], 
        packages=['FreezeUI'],
        data_files=[('bitmaps', ['FreezeUI/assets/icon.gif'])],
        include_package_data=True,
        url = 
        keywords=['python', 'gui', 'cx_Freeze', 'FreezeUI'],
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
