"""
FreezeUI | This file is for calling FreezeUI using command line.
Copyright (C) 2021  Akshat Chauhan
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


from FreezeUI_U import exe_win, msi_win
from PyQt6.QtWidgets import QApplication
import sys

def create_exe():
    print("Opening window ...")
    app = QApplication(sys.argv)
    window = exe_win.UiExeWindow()
    window.show()
    sys.exit(app.exec())


def create_msi():
    print("Opening window ...")
    app = QApplication(sys.argv)
    window = msi_win.UiMsiWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    print("""
FreezeUI is used for creating cx_freeze setup
files using GUI.

FreezeUI is licensed under GNU GPLv3
Copyright 2021 Akshat Chauhan
 ______________________________________________
|For creating exe the command is 'freezeui-exe'|
|For creating msi the command is 'freezeui-msi'| 
 ----------------------------------------------  
    """)
