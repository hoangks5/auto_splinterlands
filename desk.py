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
from chienthuat import Ui1_MainWindow
import urllib.request
import main

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def __main__():
    global ui
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    ui.pushButton_5.clicked.connect(__chienthuat__)
    MainWindow.show()





    
def check():
    with urllib.request.urlopen('https://raw.githubusercontent.com/hoangks5/auto_splinterlands/main/coment/pw.txt') as url:
        s = url.read()
        s = s.decode("utf-8")
        s = s.strip()
    if s == str(ui.lineEdit_2.text()):
        __main__()
    else:
        pass
   
def __login__():
    global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(check)
    MainWindow.show()
    
    
    



def __chienthuat__():
    global ui
    ui = Ui1_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_4.clicked.connect(__main__)
    MainWindow.show()

    

__login__()

sys.exit(app.exec_())