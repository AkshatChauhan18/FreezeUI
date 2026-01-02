"""
FreezeUI | This file is for calling FreezeUI using command line.
Made by Akshat Chauhan
Message on reddit u/AkshatCha

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

from .freezeui import *
from PyQt6.QtWidgets import QApplication
import sys


def open_ui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    print(
        """
FreezeUI is used for converting .py to .exe/.msi
files using GUI.

FreezeUI is licensed under GNU GPLv3
Made by Akshat Chauhan
 _________________________________________________
|For creating exe or msi the command is 'freezeui'|
 -------------------------------------------------  
    """
    )
