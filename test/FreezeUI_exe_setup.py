import sys
import os
from cx_Freeze import setup, Executable
 
file = f"{os.path.dirname(os.path.realpath(__file__))}"
build_exe_options = {"packages":["tkinter"],"build_exe": f"{file}/tmp"}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "test app",
    version = "1.0",
    description = "test app",
    options = {"build_exe": build_exe_options},
    executables = [Executable(f"{file}/app.py", base=base, icon=f"{file}/icon.ico", copyright = "2021`",target_name="test app")]
)