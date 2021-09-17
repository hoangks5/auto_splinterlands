from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, center
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QSpinBox, QTextEdit, QMessageBox
import sys
import a
import threading
import os

def __win__():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500,200,720,720)
    win.setWindowTitle("AUTO By Hoàng")






    input_text = QTextEdit(win)
    input_text.move(30,30)
    input_text.resize(400,500)
    input_text.setFont(QFont('Arial',13))
    input_text.setPlaceholderText('Copy và Paste list accout vào đây ')


    def getText():
        b = input_text.toPlainText()
        b = b.splitlines()
        msg = QMessageBox(win)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Thông báo")
        msg.setText("Đã upload thành công "+str(len(b))+" tài khoản.")
        x = msg.exec_()
        label_d.setText("Danh sách có "+str(len(b))+" tài khoản")
        label_d.setStyleSheet('color: green')
        label_d.adjustSize()










    check = QtWidgets.QCheckBox(win)
    check.setText("Tự động mở rương")
    check.resize(200,70)
    check.setFont(QFont('Tahoma',11))
    check.move(480,100)


    def batdau():
        acc = input_text.toPlainText()
        acc = acc.splitlines()
        a.chay(acc)
    runbutton = QPushButton('Bắt đầu',win)
    runbutton.setFont(QFont('Tahoma',13))
    runbutton.move(460,190)
    def bd():
        x = threading.Thread(target=batdau)
        x.start()
    runbutton.clicked.connect(bd)

    def dung():
        os.system("taskkill /f /im chrome.exe")
    
    def kill():
        x = threading.Thread(target=dung)
        x.start()

    stopbutton = QPushButton('Dừng',win)
    stopbutton.setFont(QFont('Tahoma',13))
    stopbutton.move(580,190)
    stopbutton.clicked.connect(kill)
    


    button = QPushButton('Upload',win)
    button.move(50,550)
    button.setFont(QFont('Tahoma',13))
    button.clicked.connect(getText)



    label_d = QtWidgets.QLabel(win)
    label_d.setText("Chưa thêm tài khoản nào")
    label_d.setFont(QFont('Tahoma',13))
    label_d.setStyleSheet('color: red')
    label_d.adjustSize()
    label_d.move(480,70)





    win.show()
    sys.exit(app.exec_())


while(True):
    __win__()