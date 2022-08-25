from FreezeUI_U import editor_window
from PyQt6.QtWidgets import QApplication
import sys
import os
file = f"{os.path.dirname(os.path.realpath(__file__))}/FreezeUI_exe_setup.py"

def test():
    script = open(file).read()
    
    app = QApplication(sys.argv)
    window = editor_window.EditorWindow(script,"app.py","EXE")
    window.show()
    window.command = f"run {file} build_exe"
    window.create()
    app.exec()