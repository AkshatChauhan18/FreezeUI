from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QPushButton, QMessageBox,QApplication
from PyQt6.QtCore import QPoint
from PyQt6.Qsci import QsciScintilla, QsciLexerPython
from PyQt6.QtGui import QFont,QColor
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole import styles
from qtconsole.manager import QtKernelManager
import os

USE_KERNEL = "python3"


def make_jupyter_widget_with_kernel():
    kernel_manager = QtKernelManager(kernel_name=USE_KERNEL)
    kernel_manager.start_kernel()
    kernel_client = kernel_manager.client()
    kernel_client.start_channels()
    jupyter_widget = RichJupyterWidget()
    jupyter_widget.style_sheet = styles.sheet_from_template("inkpot", colors="linux")
    jupyter_widget.kernel_manager = kernel_manager
    jupyter_widget.kernel_client = kernel_client
    return jupyter_widget


class EditorWidget(QWidget):
    def __init__(self):
        super(EditorWidget, self).__init__()
        self.ver_layout = QVBoxLayout()
        self.setLayout(self.ver_layout)

        font = QFont()
        font.setPointSize(14)
        font.setFamily("Verala Round")
        self.command = None
        self.setup_file_name = None
        self.python_file = None

        self.editor = QsciScintilla()
        self.editor.setMarginsBackgroundColor(QColor(55, 66, 89, 255))
        self.editor.setMarginType(1, QsciScintilla.MarginType.NumberMargin)
        self.editor.setMarginWidth(1, "0000")
        self.editor.setBraceMatching(QsciScintilla.BraceMatch.SloppyBraceMatch)
        self.lexer = QsciLexerPython()
        self.lexer.setDefaultPaper(QColor(40, 44, 52,255))
        self.editor.setLexer(self.lexer)
        self.editor.setTabWidth(4)
        self.editor.setIndentationGuides(True)
        self.editor.setTabIndents(True)
        self.editor.setAutoIndent(True)

        # self.editor.verticalScrollBar().setStyleSheet(vertical_scroll_bar_stylesheet)
        # self.editor.horizontalScrollBar().setStyleSheet(horizontal_scroll_bar_stylesheet)
        self.frame = QFrame()
        self.create_button = QPushButton(self.frame)
        self.create_button.setFont(font)
        self.save_button = QPushButton(self.frame)
        self.save_button.setFont(font)
        self.jupyter_widget = make_jupyter_widget_with_kernel()
        self.jupyter_widget.setHidden(True)
        self.ver_layout.addWidget(self.editor)
        self.ver_layout.addWidget(self.frame)
        self.ver_layout.addWidget(self.jupyter_widget)
        self.save_button.setText("Save File")
        self.jupyter_widget_shown = False
        # setting stylesheet to widgets
        self.create_button.setStyleSheet(
            "border-radius:5px;background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #218c74, stop:1 #33d8b3);color:rgb(91, 101, 124)")
        self.save_button.setStyleSheet(
            "border-radius:5px;background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #218c74, stop:1 #33d8b3);color:rgb(91, 101, 124)")

        # setting geometry to widgets
        self.editor.setMinimumSize(800, 400)
        self.frame.setMinimumHeight(30)
        self.create_button.setMinimumSize(110, 30)
        self.save_button.move(QPoint(120, 0))
        self.save_button.setMinimumSize(110, 30)
        self.jupyter_widget.setMinimumHeight(200)

        # triggering actions
        self.create_button.clicked.connect(self.create)
        self.save_button.clicked.connect(self.save_file)

    def msi_code(self, python_file,cx_script):
        self.editor.setText(cx_script)
        self.python_file = python_file
        self.create_button.setText("Create MSI")
        self.command = "run FreezeUI_msi_setup.py bdist_msi"
        self.setup_file_name = "FreezeUI_msi_setup.py"
        self.notification = (
            "try:\n"
            "    from plyer import notification\n"
            "    from FreezeUI_U import __icon__\n"
            "    notification.notify(\n"
            "        title='FreezeUI Creator',\n"
            "        message=('''Your MSI is created \nThanks for using FreezeUI'''),\n"
            "        app_icon = __icon__,\n"
            "        timeout=10)\n"
            "    print()\n"
            "    print('Your msi is created.')\n"
            "except:\n"
            "    print()\n"
            "    print('Your msi is created.')"
        )

    def exe_code(self, python_file,cx_script):
        self.editor.setText(cx_script)
        self.python_file = python_file
        self.create_button.setText("Create EXE")
        self.command = "run FreezeUI_exe_setup.py build"
        self.setup_file_name = "FreezeUI_exe_setup.py"
        self.notification = (
            "try:\n"
            "    from plyer import notification\n"
            "    from FreezeUI_U import __icon__\n"
            "    notification.notify(\n"
            "        title='FreezeUI Creator',\n"
            "        message=('''Your EXE is created \nThanks for using FreezeUI'''),\n"
            "        app_icon = __icon__,\n"
            "        timeout=10)\n"
            "    print('Your exe is created.')\n"
            "    print()\n"
            "except:\n"
            "    print()\n"
            "    print('Your exe is created.')"
        )

        

    def create(self):
        try:
            self.save_file()
            self.jupyter_widget.setHidden(False)
            self.jupyter_widget_shown = True
            self.jupyter_widget.kernel_client.execute(
                f'cd "{os.path.dirname(self.python_file)}"'
            )
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
            with open(
                f"{os.path.dirname(self.python_file)}/{self.setup_file_name}", "w+"
            ) as f:
                f.write(self.editor.text())
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.exec()
            return

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = EditorWidget()
    ui.show()
    sys.exit(app.exec())