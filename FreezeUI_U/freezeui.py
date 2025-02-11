import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication,QFileDialog
from PyQt6.QtGui import QFontDatabase, QResizeEvent
from PyQt6.QtCore import QSize
from script_editor import *
import asyncio
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1"
file_dir = os.path.dirname(os.path.realpath(__file__))
assets_folder = os.path.join(file_dir, "assets")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(f"{file_dir}/main.ui", self)
        QFontDatabase.addApplicationFont(f"{assets_folder}/Varela_Round/VarelaRound.ttf")
        self.sidebar_max_width = 135
        self.script_page = EditorWidget()
        self.stacked_pages.addWidget(self.script_page)
        self.editor_btn.setHidden(True)
        self.stacked_pages.setCurrentIndex(0)
        self.include_folder_list = []
        self.include_file_list = []
        self.new_size = QSize(self.geometry().width(),self.geometry().height())
        # connecting all the buttons
        # --------------------------------------------------------
        self.toggle_btn.clicked.connect(self.change_sidebar_width)
        self.exe_icon_btn.clicked.connect(lambda:self.select_icon(0))
        self.msi_icon_btn.clicked.connect(lambda:self.select_icon(1))
        self.exe_script_btn.clicked.connect(lambda:self.select_pyscript(0))
        self.msi_script_btn.clicked.connect(lambda:self.select_pyscript(1))
        self.exe_dest_btn.clicked.connect(self.select_exe_dest)
        self.exe_gen_btn.clicked.connect(self.generate_exe_script)
        self.msi_gen_btn.clicked.connect(self.generate_msi_script)
        self.msi_folders_btn.clicked.connect(self.include_folders)
        self.msi_files_btn.clicked.connect(self.include_files)
        self.exe_btn.clicked.connect(self.show_exepage)
        self.msi_btn.clicked.connect(self.show_msipage)
        self.editor_btn.clicked.connect(self.show_editor)

    # change the width of side bar to show button text
    # ------------------------------------------------------------
    def change_sidebar_width(self):
        # self.side_bar = QWidget()
        width = self.side_bar.width()
        if width == self.sidebar_max_width:
            self.side_bar.setMinimumWidth(50)
            self.side_bar.setMaximumWidth(50)
        else:
            self.side_bar.setMinimumWidth(135)
            self.side_bar.setMaximumWidth(135)

    # function to generate cxfreeze script for creating exe 
    # ------------------------------------------------------------
    def generate_exe_script(self):
        name = self.exe_app_name.text().strip()
        version = str(None) if self.exe_app_ver.text().strip() == "" else f'"{self.exe_app_ver.text().strip()}"'
        copyright_text = self.exe_app_copyright.text().strip()
        description = self.exe_app_description.text().strip()
        icon = str(None) if self.exe_app_icon.text() == "" else f'"{self.exe_app_icon.text().strip()}"'
        python_file = self.exe_app_pyscript.text().strip()
        destination = f"{self.exe_app_dest.text().strip()}/{name}-{self.exe_app_ver.text().strip()}_win_application"
        package_list = str([]) if self.exe_app_modinc.text().strip() == "" else str(self.exe_app_modinc.text().strip().split(' '))
        exclude_package_list = str([]) if self.exe_app_modexc.text().strip() == "" else str(self.exe_app_modexc.text().strip().split(' '))
        base = str(None) if self.exe_console.isChecked() else '"Win32GUI"'
        
        if self.exe_app_dest.text().strip() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select destination folder")
            msg.exec()
            return
        
        if python_file == "":
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

        if not os.path.exists(self.exe_app_dest.text().strip()):
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
            .replace("excludes-",exclude_package_list)
            .replace("app_name-",name)
            .replace("version-", version)
            .replace("description-",description)
            .replace("python_file-",python_file)
            .replace("icon-", icon)
            .replace("copyright-",copyright_text)
            .replace("dest-", destination)
            .replace("base-",base)
        )
        self.script_page.exe_code(python_file,converted_script)
        self.stacked_pages.setCurrentIndex(2)
        self.editor_btn.setHidden(False)

    def generate_msi_script(self):
        app_name = self.msi_app_name.text().strip()
        msi_author = self.msi_author.text().strip()
        version = str(None) if self.msi_app_ver.text() == "" else f'"{self.msi_app_ver.text().strip()}"'
        copyright = self.msi_app_copyright.text().strip()
        description = self.msi_app_description.text().strip()
        exe_icon = str(None) if self.msi_app_icon.text() == "" else f'"{self.msi_app_icon.text().strip()}"'
        python_file = self.msi_app_pyscript.text().strip()
        package_list = str([]) if self.msi_app_modinc.text().strip() == "" else str(self.msi_app_modinc.text().strip().split(' '))
        exclude_package_list = str([]) if self.msi_app_modexc.text().strip() == "" else str(self.msi_app_modexc.text().strip().split(' '))
        upgrade_code = str(None) if self.msi_upgrade_code.text() == "" else self.msi_upgrade_code.text().strip()
        include_folders = self.msi_folders_inc.text().strip()
        include_files = self.msi_files_inc.text().strip()
        add_to_path = str(True) if self.msi_atp.isChecked() else str(False)
        install_for_all = str(True) if self.msi_ifau.isChecked() else str(False)
        includes = str([])
        base = str(None) if self.msi_console.isChecked() else '"Win32GUI"'
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
            .replace("exclude_module-", exclude_package_list)
            .replace("include_module-", package_list)
            .replace("python_file-", python_file)
            .replace("include_files-", includes)
            .replace("author-", msi_author)
            .replace("all_users-", install_for_all)
            .replace("base-",base)
        )

        self.script_page.msi_code(python_file,converted_script)
        self.stacked_pages.setCurrentIndex(2)
        self.editor_btn.setHidden(False)

    def select_icon(self,n):
        icon_open_dialog,_ = QFileDialog.getOpenFileName(self,"Select Icon",filter="Icons(*.ico)")
        if icon_open_dialog:
            if n == 0:
                self.exe_app_icon.setText(icon_open_dialog)
            else:
                self.msi_app_icon.setText(icon_open_dialog)

    def select_pyscript(self,n):
        file_open_dialog,_ = QFileDialog.getOpenFileName(self,"Select python file",filter="Python file(*.py)")
        if file_open_dialog:
            if n==0:
                self.exe_app_pyscript.setText(file_open_dialog)
            else:
                self.msi_app_pyscript.setText(file_open_dialog)

    def include_folders(self):
        select_folder = QFileDialog.getExistingDirectory(self, "Select folder")
        if select_folder:
            self.include_folder_list.append(select_folder)
            self.msi_folders_inc.setText(f"{self.include_folder_list}")

    def include_files(self):
        select_files, _ = QFileDialog.getOpenFileNames(
            self, "Select Files", filter="All files (*.*)")
        if select_files:
            for i in select_files:
                self.include_file_list.append(i)
            self.msi_files_inc.setText(f"{self.include_file_list}")


    def select_exe_dest(self):
        select_folder= QFileDialog.getExistingDirectory(self,"Select destination folder")
        if select_folder:
            self.exe_app_dest.setText(select_folder)

    def resizeEvent(self,event:QResizeEvent):
        if QResizeEvent.spontaneous(event):
            self.new_size = QSize(self.geometry().width(),self.geometry().height())
            print(self.new_size)

    def show_exepage(self):
        if self.script_page.jupyter_widget_shown:
            self.script_page.jupyter_widget.setHidden(True)
        self.stacked_pages.setCurrentIndex(0) 
        self.resize(self.new_size)
    
    def show_msipage(self):
        if self.script_page.jupyter_widget_shown:
            self.script_page.jupyter_widget.setHidden(True)
        self.stacked_pages.setCurrentIndex(1) 
        self.resize(self.new_size)

    def show_editor(self):
        self.stacked_pages.setCurrentIndex(2)
        if self.script_page.jupyter_widget_shown:
            self.script_page.jupyter_widget.setHidden(False)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()