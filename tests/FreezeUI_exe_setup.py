import sys
from cx_Freeze import setup, Executable
 

build_exe_options = {"packages":['tkinter'], "excludes": [],"build_exe": "D:/pythonpro/projects/python_libraries/FreezeUI/tests/tes-1_win_application"}

# base="Win32GUI" should be used only for Windows GUI app
base = None

setup(
    name = "tes",
    version = "1",
    description = "iuytrte",
    options = {"build_exe": build_exe_options},
    executables = [Executable("D:/pythonpro/projects/python_libraries/FreezeUI/tests/app.py", base=base, icon=None, copyright = "",target_name="tes")]
)