from FreezeUI import editor_window
from PyQt5.QtWidgets import QApplication
import sys
def test():
    script = """import sys
from cx_Freeze import setup, Executable
 

build_exe_options = {"packages":["tkinter"],"build_exe": "tmp/"}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "test app",
    version = "1.0",
    description = "test app",
    options = {"build_exe": build_exe_options},
    executables = [Executable("test_app.py", base=base, icon="icon.ico", copyright = "2021`",target_name="test app")]
)"""
    
    app = QApplication(sys.argv)
    window = editor_window.EditorWindow(script,"test_app.py","EXE")
    window.show()
    window.cre
    sys.exit(app.exec())