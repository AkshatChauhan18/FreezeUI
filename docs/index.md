![PyPI - Python Version](https://img.shields.io/pypi/pyversions/FreezeUI) ![PyPI](https://img.shields.io/pypi/v/FreezeUI) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/FreezeUI) ![PyPI - License](https://img.shields.io/pypi/l/FreezeUI?color=green)

FreezeUI is a python package used to create [cx_Freeze](https://pypi.org/project/cx-Freeze/) setup files and run them to create applications from python scripts (converts .py to .exe or .msi) .

Currently it can only make **Windows MSI and EXE**.

___

## Profit💰 of using FreezeUI

In order to convert .py to .exe using cx_freeze you need to write extra setup python files which is time taking process. FreezeUI creates those setup files for you using GUI which is a easy process and later you can edit those files using FreezeUI editor like in inno setup.

___

## Installation⏬

```
pip install FreezeUI
```

---

## Build from source🛠️

To build from source download the [zip folder](https://github.com/AkshatChauhan18/FreezeUI/archive/refs/heads/master.zip) or use *git* to
clone repo using command : 

```
git clone https://github.com/AkshatChauhan18/FreezeUI <location>
```

After that from the folder run command

 ```
pip install -e .
``` 

Now you can contribute to FreezeUI project. You can run the above command whenever you make changes to ```setup.py``` or to the code.

---

## Usage🧾

For creating **EXE** the command is

``` 
freezeui-exe
```

For creating **MSI** the command is

```
freezeui-msi
```

___

## Gallery🖼️

Check demo [here](demo.html) .

|Exe Window |Msi Window | 
| ----------- | ----------- | 
|![exewin](assets/exe_win.png)|![msiwin](assets/msi_win.png)|

|Editor Window|
| ----------- |
|![editorwin](assets/editor_window.png)|


