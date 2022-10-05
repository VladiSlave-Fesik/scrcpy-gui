from PyQt5 import QtGui
from PyQt5.QtGui import QIntValidator, QFont, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout,QMessageBox,QLineEdit
import os
from os import startfile as run

com1 = r'E:\Games\scrcpy\scrcpy.exe'
com2 = r'app.py'


def main():

    app = QApplication([])
    main_win = QWidget()
    main_win.setWindowTitle('Options')
    main_win.resize(300,200)
    main_win.setWindowIcon(QtGui.QIcon('icon.ico'))
    main_win.setStyleSheet("background-image : url(back2.png)")

    btn1 = QPushButton('original scrcpy')
    btn1.setStyleSheet("color: rgb(20, 180, 160); font: bold 25px;")
    btn2 = QPushButton('scrcpy with connect_gui')
    btn2.setStyleSheet("color: rgb(20, 180, 160); font: bold 25px;")

    top_line = QHBoxLayout()

    bot_line = QHBoxLayout()

    top_line.addWidget(btn1)

    bot_line.addWidget(btn2)

    main_line = QVBoxLayout()
    main_line.addLayout(top_line)
    main_line.addLayout(bot_line)

    btn1.clicked.connect(lambda: run(com1))
    btn2.clicked.connect(lambda: run(com2))

    main_win.setLayout(main_line)
    main_win.show()
    app.exec()

if __name__ == '__main__':
    main()