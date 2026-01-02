import sys
from cx_Freeze import setup, Executable
 

build_exe_options = {"packages":['tkinter'], "excludes": [],"build_exe": "D:/pythonpro/projects/python_libraries/FreezeUI/tests/my app-2.0_win_application"}

# base="Win32GUI" should be used only for Windows GUI app
base = None

setup(
    name = "my app",
    version = "2.0",
    description = "df",
    options = {"build_exe": build_exe_options},
    executables = [Executable("D:/pythonpro/projects/python_libraries/FreezeUI/tests/app.py", base=base, icon="D:/pythonpro/projects/python_libraries/FreezeUI/tests/icon.ico", copyright = "none",target_name="my app")]
)