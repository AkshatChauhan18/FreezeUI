import sys
from cx_Freeze import setup, Executable
 

build_exe_options = {"packages":[], "excludes": [],"build_exe": "D:/pythonpro/projects/python_libraries/FreezeUI/tests/test1-1.0_win_application"}

# base="Win32GUI" should be used only for Windows GUI app
base = None

setup(
    name = "test1",
    version = "1.0",
    description = "hjdhj",
    options = {"build_exe": build_exe_options},
    executables = [Executable("D:/pythonpro/projects/python_libraries/FreezeUI/tests/app.py", base=base, icon="D:/pythonpro/projects/python_libraries/FreezeUI/tests/icon.ico", copyright = "none",target_name="test1")]
)