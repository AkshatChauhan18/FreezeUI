import sys
from cx_Freeze import setup, Executable
 

build_exe_options = {"packages":[], "excludes": [],"build_exe": "D:/pythonpro/projects/python_libraries/FreezeUI/FreezeUI_U/assets/zswert-123243_win_application"}

# base="Win32GUI" should be used only for Windows GUI app
base = None

setup(
    name = "zswert",
    version = "123243",
    description = "",
    options = {"build_exe": build_exe_options},
    executables = [Executable("D:/pythonpro/projects/python_libraries/FreezeUI/setup.py", base=base, icon=None, copyright = "",target_name="zswert")]
)