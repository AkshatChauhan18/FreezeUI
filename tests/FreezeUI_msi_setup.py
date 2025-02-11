import sys
from cx_Freeze import setup, Executable  

directory_table = [
    ("ProgramMenuFolder", "TARGETDIR", "."),
    ("MyProgramMenu", "ProgramMenuFolder", "MYPROG~1|My Program")
]

base = None

msi_data = {
    "Directory": directory_table,
    "ProgId": [
        ("Prog.Id", None, None, "dcdccd" , "IconId",None),
    ]
}

bdist_msi_options = {
    "add_to_path": True,
    "all_users": True,
    "data": msi_data,
    "upgrade_code": None,
    "install_icon":"D:/pythonpro/projects/python_libraries/FreezeUI/tests/icon.ico",
    "summary_data":{"author":"akshat"}
}

build_exe_options = {"excludes":[],"packages":[],"include_files":['D:/pythonpro/projects/python_libraries/FreezeUI/tests/icon.ico','D:/pythonpro/projects/python_libraries/FreezeUI/tests/assets']}

executables = [
    Executable(
        "D:/pythonpro/projects/python_libraries/FreezeUI/tests/app.py",
        copyright="hhhuds",
        base=base,
        icon="D:/pythonpro/projects/python_libraries/FreezeUI/tests/icon.ico",
        shortcut_name="hall",
        shortcut_dir="MyProgramMenu",
        target_name="hall"
    )
]

setup(
    name="hall",
    version="1.0",
    description="dcdccd",
    executables=executables,
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    })