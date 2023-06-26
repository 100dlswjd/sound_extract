import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PySide6.QtCore import Slot, Signal, QObject

from threading import Thread

from ui.main_form import Ui_MainWindow
from ui.gif_extract_form import Ui_Gif_extract
from ui.sound_extract_form import Ui_Sound_extract
from ui.complete_form import Ui_Complete

from myclass.extract import Extract

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

class Complete(QWidget, Ui_Complete):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_acept.clicked.connect(self.btn_acept_handler)

    def set_class_name(self, class_name : str):
        self.label_classes.setText(class_name)
        
    @Slot()
    def btn_acept_handler(self):
        self.close()

class Check_signal(QObject):
    check = Signal(bool)
    
class Gif_extract(QWidget, Ui_Gif_extract):
    def __init__(self, file_path):
        super().__init__()
        self.setupUi(self)
        self.check_signal = Check_signal()
        self.extract = Extract(file_path)
        self.spinBox_fps.setMaximum(self.extract.max_fps)
        self.pushButton_extract.clicked.connect(self.btn_extract_handler)
        self.spinBox_fps.setValue(self.extract.max_fps)
        self.pushButton_save_path_select.clicked.connect(self.btn_save_path_select_handler)
        self.save_file_path = ""
        self.pushButton_extract.setEnabled(False)

    @Slot()
    def btn_save_path_select_handler(self):
        file = QFileDialog.getSaveFileName(self, caption="GIF 파일 저장", filter="GIF 파일 (*.gif)")
        if file[0] != "":
            self.save_file_path = file[0]
            self.lineEdit_save_path.setText(self.save_file_path)
            self.pushButton_extract.setEnabled(True)
        else:
            self.pushButton_extract.setEnabled(False)

    @Slot()
    def btn_extract_handler(self):
        thread = Thread(target=self.work_thread, args=(self.extract, self.save_file_path, self.spinBox_fps.value(), self.check_signal))
        thread.start()        

    def work_thread(self, extract : Extract ,save_file_path : str, fps : int, check_signal : Check_signal):
        extract.gif_extract(save_file_path, fps)
        check_signal.check.emit(True)


    def __del__(self):
        pass

class Sound_extract(QWidget, Ui_Sound_extract):
    def __init__(self, file_path):
        super().__init__()
        self.setupUi(self)
        self.check_signal = Check_signal()
        self.extract = Extract(file_path)
        self.pushButton_save_path_select.clicked.connect(self.btn_save_path_select_handler)
        self.pushButton_extract.clicked.connect(self.btn_extract_handler)
        self.pushButton_extract.setEnabled(False)
        self.save_file_path = ""

    @Slot()
    def btn_save_path_select_handler(self):
        file = QFileDialog.getSaveFileName(self, caption="mp3 파일 저장", filter="mp3 파일 (*.mp3)")
        if file[0] != "":
            self.save_file_path = file[0]
            self.lineEdit_save_path.setText(self.save_file_path)
            self.pushButton_extract.setEnabled(True)
        else:
            self.pushButton_extract.setEnabled(False)

    @Slot()
    def btn_extract_handler(self):
        thread = Thread(target=self.work_thread, args=(self.extract, self.save_file_path, self.check_signal))
        thread.start()
    
    def work_thread(self, extract : Extract ,save_file_path : str, check_signal : Check_signal):
        extract.sound_extract(save_file_path)
        check_signal.check.emit(True)

    def __del__(self):
        pass

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_select_file.clicked.connect(self.btn_select_file_handler)
        self.complete_widget = Complete()

    @Slot()
    def btn_select_file_handler(self):
        file = QFileDialog.getOpenFileName(caption="비디오 파일 선택", filter="비디오 파일 (*.mp4)")
        if file[0] != "":
            self.tabWidget.clear()
            file_path = file[0]
            self.lineEdit_file_path.setText(file_path)
            gif_class = Gif_extract(file_path)
            gif_class.check_signal.check.connect(self.gif_extract_handler)
            sound_class = Sound_extract(file_path)
            sound_class.check_signal.check.connect(self.sound_extract_handler)
            self.tabWidget.addTab(sound_class, "소리 추출")
            self.tabWidget.addTab(gif_class, "GIF 추출")
        else:
            pass
    
    @Slot(bool)
    def gif_extract_handler(self, check):
        if check:
            self.complete_widget.set_class_name("GIF")
            self.complete_widget.show()

    @Slot(bool)
    def sound_extract_handler(self, check):
        if check:
            self.complete_widget.set_class_name("mp3")
            self.complete_widget.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.setStyle("Fusion")
    app.exec()
    