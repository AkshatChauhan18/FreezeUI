import sys
from cx_Freeze import setup, Executable
 

build_exe_options = {"packages":[], "excludes": [],"build_exe": "C:/Users/akkic/Documents/eefwe-1.0_win_application"}

# base="Win32GUI" should be used only for Windows GUI app
base = None

setup(
    name = "eefwe",
    version = "1.0",
    description = "",
    options = {"build_exe": build_exe_options},
    executables = [Executable("D:/pythonpro/projects/python_libraries/FreezeUI/tests/app.py", base=base, icon="D:/pythonpro/projects/python_libraries/FreezeUI/tests/icon.ico", copyright = "feerfefrer",target_name="eefwe")]
)