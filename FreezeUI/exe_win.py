"""
FreezeUI | This file is the gui for creating windows exe.
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
along with this program.  If not, see <https://www.gnu.org/licenses/>."""


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from FreezeUI.editor_window import *

assets_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)),"assets")


class UiExeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        font = QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.resize(652, 650)
        self.setStyleSheet("background: #03203C")
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("FreezeUI")
        self.setWindowIcon(QIcon(f"{assets_folder}/pyicon.svg"))

# creating widgets
        gif_icon = QMovie(f'{assets_folder}/icon.gif')
        gif_icon.setScaledSize(QSize(120,120))
        img = QPixmap(f'{assets_folder}/exe_text.png')
        img = img.scaled(347,72)
        self.freezeui_icon = QLabel(self.centralwidget)
        self.freezeui_icon.setMovie(gif_icon)
        gif_icon.start()
        self.so_cool_text = QLabel(self.centralwidget)
        self.so_cool_text.setPixmap(img)
        self.app_edit = QLineEdit(self.centralwidget)
        self.version_edit = QLineEdit(self.centralwidget)
        self.copyright_edit = QLineEdit(self.centralwidget)
        self.description_edit = QLineEdit(self.centralwidget)       
        self.icon_edit = QLineEdit(self.centralwidget)
        self.icon_browser_button = QPushButton(self.centralwidget)
        self.python_script_edit = QLineEdit(self.centralwidget)        
        self.python_script_browser_button = QPushButton(self.centralwidget)
        self.dest_folder = QLineEdit(self.centralwidget)                          
        self.dest_browser_button = QPushButton(self.centralwidget)                
        self.include_modules_list = QLineEdit(self.centralwidget)                        
        self.exclude_modules_list = QLineEdit(self.centralwidget)                
        self.script_gen_button = QPushButton(self.centralwidget)

# seeting fonts to widgets        
        self.app_edit.setFont(font)
        self.copyright_edit.setFont(font)
        self.version_edit.setFont(font)
        self.description_edit.setFont(font)
        self.icon_browser_button.setFont(font)              
        self.script_gen_button.setFont(font)
        self.icon_edit.setFont(font)
        self.python_script_edit.setFont(font)                       
        self.dest_browser_button.setFont(font)                     
        self.exclude_modules_list.setFont(font)
        self.include_modules_list.setFont(font)
        self.python_script_browser_button.setFont(font)   
        self.dest_folder.setFont(font)   

# adding text and placeholder text to widgets        
        self.app_edit.setPlaceholderText("App Name")
        self.version_edit.setPlaceholderText("Version")
        self.description_edit.setPlaceholderText("Description")
        self.copyright_edit.setPlaceholderText("Copyright")
        self.icon_edit.setPlaceholderText("Icon")
        self.python_script_edit.setPlaceholderText("Path to python script")
        self.dest_folder.setPlaceholderText('Destination Folder')
        self.exclude_modules_list.setPlaceholderText('Modules to be excluded (seperated by spaces)')
        self.include_modules_list.setPlaceholderText('Modules to be included (seperated by spaces)')
        self.icon_browser_button.setText("BROWSE")
        self.python_script_browser_button.setText("BROWSE")
        self.dest_browser_button.setText("BROWSE")
        self.script_gen_button.setText("Create    EXE")

# adding stylesheet to widgets
        self.freezeui_icon.setStyleSheet(
            "background-color:red;border-radius:5px")
        self.app_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black")   
        self.copyright_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black")
        self.version_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black")   
        self.description_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black")
        self.icon_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black")   
        self.icon_browser_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)")    
        self.python_script_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black") 
        self.python_script_browser_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)")            
        self.dest_folder.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black")
        self.include_modules_list.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black")    
        self.exclude_modules_list.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black")    
        self.script_gen_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)") 
        self.dest_browser_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)") 
        

# setting geometry to widgets
        self.freezeui_icon.setGeometry(QRect(30, 10, 120, 120))
        self.so_cool_text.move(220, 40)
        self.app_edit.setGeometry(QRect(30, 150, 330, 30))
        self.version_edit.setGeometry(QRect(30, 200, 330, 30))
        self.copyright_edit.setGeometry(QRect(30, 250, 330, 30))
        self.description_edit.setGeometry(QRect(30, 300, 480, 30))
        self.icon_edit.setGeometry(QRect(30, 350, 480, 30))
        self.icon_browser_button.setGeometry(QRect(530, 350, 90, 30))
        self.python_script_edit.setGeometry(QRect(30, 400, 480, 30))
        self.python_script_browser_button.setGeometry(QRect(530, 400, 90, 30))
        self.dest_folder.setGeometry(QRect(30, 450, 480, 30))
        self.dest_browser_button.setGeometry(QRect(530, 450, 90, 30))
        self.include_modules_list.setGeometry(QRect(30, 500, 590, 30))
        self.exclude_modules_list.setGeometry(QRect(30, 550, 590, 30))
        self.script_gen_button.setGeometry(QRect(100, 600, 450, 30))
        

# triggering actions
        self.icon_browser_button.clicked.connect(self.find_icon)
        self.python_script_browser_button.clicked.connect(self.find_file)
        self.dest_browser_button.clicked.connect(self.select_dest_folder)
        self.script_gen_button.clicked.connect(self.generate_script)

        self.show()
        
# creating functions 
    
    def find_icon(self):
        icon_open_dialog,_ = QFileDialog.getOpenFileName(self,"Select Icon",filter="Icons(*.ico)")
        if icon_open_dialog:
            self.icon_edit.setText(icon_open_dialog)

    def find_file(self):
        file_open_dialog,_ = QFileDialog.getOpenFileName(self,"Select python file",filter="Python file(*.py)")
        if file_open_dialog:
            self.python_script_edit.setText(file_open_dialog)

    def select_dest_folder(self):
        select_folder= QFileDialog.getExistingDirectory(self,"Select destination folder")
        if select_folder:
            self.dest_folder.setText(select_folder)

    def generate_script(self):
        app_name = self.app_edit.text().strip()
        package_list = str([]) if self.include_modules_list.text() == "" else str(self.include_modules_list.text().strip().split(' '))
        exclude_modules_list = str([]) if self.exclude_modules_list.text() == "" else str(self.exclude_modules_list.text().strip().split(' '))
        icon = str(None) if self.icon_edit.text() == "" else f'"{self.icon_edit.text().strip()}"'
        version = str(None) if self.version_edit.text() == "" else f'"{self.version_edit.text().strip()}"'
        description = self.description_edit.text().strip()
        python_file = self.python_script_edit.text().strip()
        copyright_text = self.copyright_edit.text().strip()
        destination = f"{self.dest_folder.text().strip()}/{self.app_edit.text()}-{self.version_edit.text()}_win_application"
        
        if self.dest_folder.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select destination folder")
            msg.exec()
            return
        
        if self.python_script_edit.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select python file")
            msg.exec()
            return
        
        if not os.path.exists(python_file):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Python file does not exists")
            msg.exec()
            return

        if not os.path.exists(self.dest_folder.text().strip()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Destination Folder does not exists")
            msg.exec()
            return
            
        try:
            os.mkdir(destination)
        except FileExistsError :    
            pass
        
        

        script = open(f"{assets_folder}/exe_template.txt").read()
        converted_script = (
            script.replace('packages-',package_list)
            .replace("excludes-",exclude_modules_list)
            .replace("app_name-",app_name)
            .replace("version-", version)
            .replace("description-",description)
            .replace("python_file-",python_file)
            .replace("icon-", icon)
            .replace("copyright-",copyright_text)
            .replace("dest-", destination)
        )

        self.show_editor(converted_script,python_file)
        
    def show_editor(self, script, python_file):
        self.editor_window = EditorWindow(script, python_file, "EXE")
        self.editor_window.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = UiExeWindow()
    sys.exit(app.exec())

     
