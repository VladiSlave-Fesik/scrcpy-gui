import time

from PyQt5 import QtGui
from PyQt5.QtGui import QIntValidator, QFont, QColor
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout,QMessageBox,QLineEdit
import os
from os import startfile as run
import sys

app = QApplication([])

def main():
    global app, main_win


    main_win = QWidget()
    main_win.setWindowTitle('Options')
    main_win.resize(300,200)
    main_win.setWindowIcon(QtGui.QIcon('icon.ico'))
    main_win.setStyleSheet("background-image : url(back1.png)")

    btn1 = QPushButton('scrcpy')
    btn1.setStyleSheet("color: rgb(14, 227, 149); border-radius: 10px; border-style: outset; border-color: yellow; border-width: 2px;")
    btn1.setFont(font)

    btn2 = QPushButton('connect gui')
    btn2.setFont(font)
    btn2.setStyleSheet("color: rgb(14, 227, 149); border-radius: 10px; border-style: outset; border-color: yellow; border-width: 2px;")

    top_line = QHBoxLayout()
    bot_line = QHBoxLayout()

    top_line.addWidget(btn1)

    bot_line.addWidget(btn2)

    main_line = QVBoxLayout()
    main_line.addLayout(top_line)
    main_line.addLayout(bot_line)

    btn1.clicked.connect(lambda: run_scrcpy())
    btn2.clicked.connect(lambda: run_connect_app())

    main_win.setLayout(main_line)
    main_win.show()
    app.exec()

def connect_app():
    style = '''
    border-style: outset;
    border-width: 2px;
    border-radius: 5px;
    border-color: cyan;
    font: bold 11px;
    min-width: 10em;
    padding: 6px;
    '''

    with open('recents.txt') as file:
        recents_list = file.readlines()

    recents = [i.strip() for i in recents_list]

    def change_recents(ip):
        if ip not in recents:
            recents[3] = recents[2]
            recents[2] = recents[1]
            recents[1] = recents[0]
            recents[0] = ip


    
    main_win = QWidget()
    main_win.setWindowTitle('Ip Enter')
    main_win.resize(300, 200)
    main_win.setWindowIcon(QtGui.QIcon('icon.ico'))
    main_win.setStyleSheet("background-color: grey;")

    label = QLabel('Enter ip of device:')
    label.setStyleSheet(style)

    entering = QLineEdit()
    entering.setMaxLength(20)
    entering.setStyleSheet(style)

    btn = QPushButton('Confirm')
    btn.setStyleSheet(style)

    label2 = QLabel('Recent`s:')

    top_line = QHBoxLayout()
    mid_line = QHBoxLayout()
    bot_line = QHBoxLayout()

    top_line.addWidget(label)
    top_line.addWidget(entering)
    top_line.addWidget(btn)

    mid_line.addWidget(label2)

    for i in recents_list[:4]:
        recent = QLabel(i)
        recent.setStyleSheet(style)
        bot_line.addWidget(recent)

    main_line = QVBoxLayout()
    main_line.addLayout(top_line)
    main_line.addLayout(mid_line)
    main_line.addLayout(bot_line)

    btn.clicked.connect(lambda: change_recents(entering.text()))

    main_win.setLayout(main_line)
    main_win.show()
    app.exec()

    file = open('recents.txt', 'w')
    for i in recents:
        file.write(f'{i}\n')

    file.close()

def run_connect_app():
    time.sleep(0.2)
    app.quit()
    time.sleep(0.2)
    connect_app()


def run_scrcpy():
    run(r'E:\Games\scrcpy\scrcpy.exe')
    app.quit()

font = QFont('Consolas',25)

if __name__ == '__main__':
    main()