"""
FreezeUI | This file is the gui for creating windows msi.
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


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from FreezeUI.editor_window import *
import os

assets_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
include_folder_list = []
include_file_list = []


scroll_bar_stylesheet = """QScrollBar:vertical {  
            border: 1px solid #aaa;            
            border-radius:2px;
            background:gray;
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


class UiMsiWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(725, 600)
        self.setStyleSheet("background : #03203C")
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("FreezeUI")

        font = QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

# creating widgets
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.verticalScrollBar().setStyleSheet(scroll_bar_stylesheet)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.app_edit = QLineEdit(self.groupBox)
        self.version_edit = QLineEdit(self.groupBox)
        self.copyright_edit = QLineEdit(self.groupBox)
        self.description_edit = QLineEdit(self.groupBox)
        self.icon_edit = QLineEdit(self.groupBox)        
        self.icon_browser_button = QPushButton(self.groupBox)        
        self.python_script_edit = QLineEdit(self.groupBox)        
        self.python_script_browser_button = QPushButton(self.groupBox)        
        self.include_modules_list = QLineEdit(self.groupBox)        
        self.exclude_modules_list = QLineEdit(self.groupBox)        
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)        
        self.upgrade_code_edit = QLineEdit(self.groupBox_2)    
        self.file_include_edit = QLineEdit(self.groupBox_2)        
        self.include_files_button = QPushButton(self.groupBox_2)        
        self.folder_include_edit = QLineEdit(self.groupBox_2)        
        self.include_folders_button = QPushButton(self.groupBox_2)    
        self.author_edit = QLineEdit(self.groupBox_2)        
        self.add_to_path = QCheckBox(self.groupBox_2)
        self.add_to_path.setCheckable(True)
        self.add_to_path.setChecked(False)        
        self.install_for_all = QCheckBox(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QFrame(self.centralwidget)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)        
        self.freezeui_gif = QLabel(self.frame)
        self.freezeui_gif.setEnabled(True)
        gif_icon = QMovie(f'{assets_folder}/icon.gif')
        gif_icon.setScaledSize(QSize(120, 120))
        self.freezeui_gif.setMovie(gif_icon)
        gif_icon.start()
        self.so_easy_text = QLabel(self.frame)
        self.so_easy_text.setPixmap(QPixmap(f"{assets_folder}/msi_text.png"))
        self.so_easy_text.setScaledContents(True)        
        self.script_gen_button = QPushButton(self.centralwidget)
          
# setting text and placeholder text to widgets
        self.groupBox.setTitle("App Settings")
        self.groupBox_2.setTitle("MSI settings")
        self.app_edit.setPlaceholderText("App Name")
        self.version_edit.setPlaceholderText("Version")
        self.copyright_edit.setPlaceholderText("Copyright")
        self.description_edit.setPlaceholderText("Description")
        self.icon_edit.setPlaceholderText("Icon")
        self.python_script_edit.setPlaceholderText("Path to python script")
        self.author_edit.setPlaceholderText("Author")
        self.include_modules_list.setPlaceholderText("Modules to be included(seperated by spaces)")
        self.exclude_modules_list.setPlaceholderText("Modules to be excluded(seperated by spaces)")
        self.upgrade_code_edit.setPlaceholderText("Upgrade Code")
        self.file_include_edit.setPlaceholderText("Files needed to be included(list)")
        self.folder_include_edit.setPlaceholderText("Folders needed to be included(list)")
        self.include_folders_button.setText("BROWSE")
        self.add_to_path.setText("Add to path")
        self.include_files_button.setText("BROWSE")
        self.script_gen_button.setText("Generate Script")
        self.icon_browser_button.setText("BROWSE")
        self.python_script_browser_button.setText("BROWSE")
        self.install_for_all.setText("Install for all users")

# setting stylesheet to widgets
        self.script_gen_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)")
        self.file_include_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.upgrade_code_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.include_files_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)")
        self.folder_include_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.groupBox_2.setStyleSheet("color:white")
        self.include_folders_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)")
        self.freezeui_gif.setStyleSheet("background:red")
        self.groupBox.setStyleSheet("color:white")
        self.exclude_modules_list.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.app_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.version_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.icon_browser_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)")
        self.copyright_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.description_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.icon_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.author_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.python_script_edit.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")
        self.python_script_browser_button.setStyleSheet(
            "border-radius:5px;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FD297A , stop: 1 #9424F0)")
        self.include_modules_list.setStyleSheet(
            "background-color:white;border-radius: 4px;border-color:black;color:black")

# setting geometry to widgets
        self.scrollArea.setGeometry(QRect(20, 150, 690, 340))
        self.scrollArea.setMinimumSize(QSize(0, 390))
        self.scrollArea.setSizeIncrement(QSize(0, 300))
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -396, 672, 734))
        self.groupBox.setMinimumSize(QSize(0, 410))
        self.app_edit.setGeometry(QRect(10, 20, 500, 30))
        self.app_edit.setMinimumSize(QSize(500, 30))
        self.version_edit.setGeometry(QRect(10, 70, 500, 30))
        self.version_edit.setMinimumSize(QSize(500, 30))
        self.copyright_edit.setGeometry(QRect(10, 120, 500, 30))
        self.copyright_edit.setMinimumSize(QSize(500, 30))
        self.description_edit.setGeometry(QRect(10, 170, 500, 30))
        self.icon_edit.setGeometry(QRect(10, 220, 500, 30))
        self.icon_browser_button.setGeometry(QRect(530, 220, 110, 30))
        self.icon_browser_button.setMinimumSize(QSize(0, 30))
        self.python_script_edit.setGeometry(QRect(10, 270, 500, 30))
        self.python_script_browser_button.setGeometry(QRect(530, 270, 110, 30))
        self.python_script_browser_button.setMinimumSize(QSize(0, 30))
        self.include_modules_list.setGeometry(QRect(10, 320, 630, 30))
        self.exclude_modules_list.setGeometry(QRect(10, 370, 630, 30))
        self.groupBox_2.setMinimumSize(QSize(0, 300))
        self.upgrade_code_edit.setGeometry(QRect(10, 20, 630, 30))
        self.file_include_edit.setGeometry(QRect(10, 70, 500, 30))
        self.include_files_button.setGeometry(QRect(530, 70, 110, 30))
        self.include_files_button.setMinimumSize(QSize(0, 30))
        self.folder_include_edit.setGeometry(QRect(10, 120, 500, 30))
        self.include_folders_button.setGeometry(QRect(530, 120, 110, 30))
        self.include_folders_button.setMinimumSize(QSize(0, 30))
        self.author_edit.setGeometry(QRect(10, 170, 500, 30))
        self.add_to_path.setGeometry(QRect(10, 210, 140, 30))
        self.install_for_all.setGeometry(QRect(10, 250, 170, 30))
        self.frame.setGeometry(QRect(22, 9, 580, 130))
        self.frame.setMinimumSize(QSize(0, 130))
        self.freezeui_gif.setGeometry(QRect(-1, 0, 120, 120))
        self.so_easy_text.setGeometry(QRect(200, 20, 370, 80))
        self.script_gen_button.setGeometry(QRect(200, 550, 350, 30))
        self.script_gen_button.setMinimumSize(QSize(0, 30))

# setting font to widgets
        self.app_edit.setFont(font)
        self.version_edit.setFont(font)
        self.copyright_edit.setFont(font)
        self.description_edit.setFont(font)
        self.icon_edit.setFont(font)
        self.icon_browser_button.setFont(font)
        self.python_script_edit.setFont(font)
        self.python_script_browser_button.setFont(font)
        self.include_modules_list.setFont(font)
        self.exclude_modules_list.setFont(font)
        self.upgrade_code_edit.setFont(font)
        self.file_include_edit.setFont(font)
        self.include_files_button.setFont(font)
        self.folder_include_edit.setFont(font)
        self.include_folders_button.setFont(font)
        self.author_edit.setFont(font)
        font.setPointSize(12)
        self.add_to_path.setFont(font)
        self.install_for_all.setFont(font)
        self.script_gen_button.setFont(font)


# triggering actions
        self.icon_browser_button.clicked.connect(self.exe_icon_function)
        self.python_script_browser_button.clicked.connect(self.python_script_browser)
        self.include_folders_button.clicked.connect(self.include_folders)
        self.include_files_button.clicked.connect(self.include_files)
        self.script_gen_button.clicked.connect(self.generate_script)
        self.show()

    def exe_icon_function(self):
        icon_file_dialogue, _ = QFileDialog.getOpenFileName(
            self, "Select Icon", filter="Icons(*.ico)")
        if icon_file_dialogue:
            self.icon_edit.setText(icon_file_dialogue)

    def python_script_browser(self):
        python_file_dialogue, _ = QFileDialog.getOpenFileName(
            self, "Select Python Script", filter="Python file (*.py)")
        if python_file_dialogue:
            self.python_script_edit.setText(python_file_dialogue)

    def include_folders(self):
        select_folder = QFileDialog.getExistingDirectory(self, "Select folder")
        if select_folder:
            include_folder_list.append(select_folder)
            self.folder_include_edit.setText(f"{include_folder_list}")

    def include_files(self):
        select_files, _ = QFileDialog.getOpenFileNames(
            self, "Select Files", filter="All files (*.*)")
        if select_files:
            for i in select_files:
                include_file_list.append(i)
            self.file_include_edit.setText(f"{include_file_list}")

    def generate_script(self):
        app_name = self.app_edit.text().strip()
        msi_author = self.author_edit.text().strip()
        version = str(None) if self.version_edit.text() == "" else self.version_edit.text().strip()
        copyright = self.copyright_edit.text().strip()
        description = self.description_edit.text().strip()
        exe_icon = str(None) if self.icon_edit.text() == "" else self.icon_edit.text().strip()
        python_file = self.python_script_edit.text().strip()
        package_list = str([]) if self.include_modules_list.text() == "" else str(self.include_modules_list.text().strip().split(' '))
        exclude_modules_list = str([]) if self.exclude_modules_list.text() == "" else str(self.exclude_modules_list.text().strip().split(' '))
        upgrade_code = str(None) if self.upgrade_code_edit.text() == "" else self.upgrade_code_edit.text().strip()
        include_folders = self.folder_include_edit.text().strip()
        include_files = self.file_include_edit.text().strip()
        add_to_path = str(True) if self.add_to_path.isChecked() else str(False)
        install_for_all = str(True) if self.install_for_all.isChecked() else str(False)
        includes = str([])
        guid = "None" if upgrade_code == "None" else "{%s}" % upgrade_code

        if include_files != "" and include_folders != "":
            includes = include_files.strip("]")+","+include_folders.strip("[")

        if include_files == "" and include_folders != "":
            includes = include_folders

        if include_files != "" and include_folders == "":
            includes = include_files

        if python_file == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select python file (.py) ")
            msg.exec()
            return

        if not os.path.exists(python_file):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Python file does not exists")
            msg.exec()
            return

        script = open(f"{assets_folder}/msi_template.txt").read()
        converted_script = (
            script.replace("description-", description)
            .replace("version-", version)
            .replace("copyright-", copyright)
            .replace("exe_icon-", exe_icon)
            .replace("upgrade_code-", guid)
            .replace("add_to_path-", add_to_path)
            .replace("app_name-", app_name)
            .replace("exclude_module-", exclude_modules_list)
            .replace("include_module-", package_list)
            .replace("python_file-", python_file)
            .replace("include_files-", includes)
            .replace("author-", msi_author)
            .replace("all_users-", install_for_all)
        )
        self.show_editor(converted_script, python_file)

    def show_editor(self, script, python_file):
        self.editor_window = EditorWindow(script, python_file, "MSI")
        self.editor_window.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = UiMsiWindow()
    sys.exit(app.exec())
