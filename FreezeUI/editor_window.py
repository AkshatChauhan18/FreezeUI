"""
FreezeUI | This file is used for editing setup files and running them.
Copyright (C) 2021  Akshat Chauhan
Message on reddit u/AkshatCha
Reddit community r/FreezeUI or r/LetsTalkProgramming

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole import styles
from qtconsole.manager import QtKernelManager
import os

USE_KERNEL = 'python3'

vertical_scroll_bar_stylesheet = """QScrollBar:vertical {  
            border: 1px solid #aaa;            
            border-radius:2px;
            background:black;
            width:13px;
            margin: 0px 3px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 #3fe433,  stop: 1 #3febe8);
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
    """
horizontal_scroll_bar_stylesheet = ("""
       QScrollBar:horizontal {
        border: 1px solid #aaa;            
        border-radius:2px;
        background-color: gray;
        height: 13px;
        margin: 3px 0px 0px 0px;
 }
  QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
 {
     background: none;
 }
 QScrollBar::handle:horizontal {
    border-radius:2px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0 #3fe433,  stop: 1 #3febe8);
    min-width: 25px;
 }
QScrollBar::add-line:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
    height: 0px;
    subcontrol-position: right;
    subcontrol-origin: margin;
 }
 QScrollBar::sub-line:horizontal {
     background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
    height: 0 px;
    subcontrol-position: left;
    subcontrol-origin: margin;
 }
    """)


def make_jupyter_widget_with_kernel():
    kernel_manager = QtKernelManager(kernel_name=USE_KERNEL)
    kernel_manager.start_kernel()
    kernel_client = kernel_manager.client()
    kernel_client.start_channels()
    jupyter_widget = RichJupyterWidget()
    jupyter_widget.style_sheet = styles.sheet_from_template(
        "inkpot", colors="linux")
    jupyter_widget.kernel_manager = kernel_manager
    jupyter_widget.kernel_client = kernel_client
    return jupyter_widget


class EditorWindow(QWidget):
    def __init__(self, script: str, python_file: str, editor_type: str):
        super(EditorWindow, self).__init__()

        font = QFont()
        font.setPointSize(14)
        font.setFamily("Yu Gothic UI")
        self.script = script
        self.python_file = python_file
        self.editor_type = editor_type            
        self.command = None
        self.setup_file_name = None

# creating widgets
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)
        self.setStyleSheet("background : #03203C")
        self.editor = QsciScintilla()
        self.editor.setText(self.script)
        self.editor.setMarginType(1, QsciScintilla.NumberMargin)
        self.editor.setMarginWidth(1, "0000")
        self.editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.editor.setLexer(QsciLexerPython())
        self.editor.setTabWidth(4)
        self.editor.setIndentationGuides(True)
        self.editor.setTabIndents(True)
        self.editor.setAutoIndent(True)
        self.editor.verticalScrollBar().setStyleSheet(vertical_scroll_bar_stylesheet)
        self.editor.horizontalScrollBar().setStyleSheet(horizontal_scroll_bar_stylesheet)
        self.frame = QFrame()
        self.create_button = QPushButton(self.frame)
        self.create_button.setFont(font)
        self.save_button = QPushButton(self.frame)
        self.save_button.setFont(font)
        self.jupyter_widget = make_jupyter_widget_with_kernel()
        self.jupyter_widget.setHidden(True)
        self.vertical_layout.addWidget(self.editor)
        self.vertical_layout.addWidget(self.frame)
        self.vertical_layout.addWidget(self.jupyter_widget)

        if self.editor_type == "MSI":
            self.create_button.setText("Create MSI")
            self.command = "run FreezeUI_msi_setup.py bdist_msi"
            self.setup_file_name = "FreezeUI_msi_setup.py"
            self.notification = (
"try:\n"
"    from plyer import notification\n"
"except:\n"
"    pass\n"
"try:"
"    notification.notify(\n"
"        title='FreezeUI Creator',\n"
"        message=('''Your MSI is created \nThanks for using FreezeUI'''),\n"
"        timeout=10)\n"
"except:\n"
"    print()"
f"    print('Your MSI is created.')")

        if self.editor_type == "EXE":
            self.create_button.setText("Create EXE")
            self.command = "run FreezeUI_exe_setup.py build"
            self.setup_file_name = "FreezeUI_exe_setup.py"
            self.notification = (
"try:\n"
"    from plyer import notification\n"
"except:\n"
"    pass\n"
"try:"
"    notification.notify(\n"
"        title='FreezeUI Creator',\n"
"        message=('''Your EXE is created \nThanks for using FreezeUI'''),\n"
"        timeout=10)\n"
"except:\n"
"    print()"
f"    print('Your EXE is created.')")

        self.save_button.setText("Save File")

        
# setting stylesheet to widgets
        self.create_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)")
        self.save_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)")

# setting geometry to widgets
        self.editor.setMinimumSize(800, 400)
        self.frame.setMinimumHeight(30)
        self.create_button.setMinimumSize(110, 30)
        self.save_button.move(QPoint(120,0))
        self.save_button.setMinimumSize(110, 30)
        self.jupyter_widget.setMinimumHeight(200)

# triggering actions
        self.create_button.clicked.connect(self.create_msi)
        self.save_button.clicked.connect(self.save_file)


    def create_msi(self):
        try:
            self.save_file()
            self.jupyter_widget.setHidden(False)
            self.jupyter_widget.kernel_client.execute(
                f'cd "{os.path.dirname(self.python_file)}"')
            self.jupyter_widget.kernel_client.execute("clear")    
            self.jupyter_widget.kernel_client.execute(self.command)
            self.jupyter_widget.kernel_client.execute(self.notification)

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.exec()
            return

    def save_file(self):
        try:
            with open(f'{os.path.dirname(self.python_file)}/{self.setup_file_name}', 'w+') as f:
                    f.write(self.editor.text())
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.exec()
            return
