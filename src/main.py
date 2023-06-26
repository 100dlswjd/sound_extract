import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from ui.main_form import Ui_MainWindow
from ui.gif_extract_form import Ui_Gif_extract
from ui.sound_extract_form import Ui_Sound_extract

class Gif_extract(QWidget, Ui_Gif_extract):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Sound_extract(QWidget, Ui_Sound_extract):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.setStyle("Fusion")
    app.exec()
    