from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, center
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QSpinBox, QTextEdit, QMessageBox
import sys
import a
import threading
import os
from login import Ui_MainWindow
from mhchinh import Ui_Form

class MainWindow:
    def __init__(self) -> None:
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

    def __init1__(self) -> None:
        self.main_win = QMainWindow()
        self.uic = Ui_Form()
        self.uic.setupUi(self.main_win)
        self.main_win.show()

        def dangnhap():
            if self.uic.lineEdit.text() == 'admin' and self.uic.lineEdit_2.text() == 'password':
                self.uic.pushButton.clicked.connect(self.__init1__)
            
        self.uic.pushButton.clicked.connect(self.__init1__)
        


    def show(self):
        self.main_win.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

