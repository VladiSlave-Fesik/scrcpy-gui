import time
from PyQt5 import QtGui
from PyQt5.QtGui import QIntValidator, QFont, QColor
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout,QMessageBox,QLineEdit,QMainWindow
import os
from os import startfile as run
import sys
import subprocess as sp

dir = os.getcwd().strip('scrcpy_gui')

font = QFont('Consolas',25)
style = '''
    border-style: outset;
    border-width: 2px;
    border-radius: 5px;
    border-color: cyan;
    font: bold 11px;
    min-width: 10em;
    padding: 6px;
    '''


class main_window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Options')
        self.resize(300,200)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setStyleSheet("background-image : url(back.png)")

        self.btn1 = QPushButton('scrcpy')
        self.btn1.setStyleSheet("color: rgb(14, 227, 149); border-radius: 10px; border-style: outset; border-color: yellow; border-width: 2px;")
        self.btn1.setFont(font)

        self.btn2 = QPushButton('connect gui')
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("color: rgb(14, 227, 149); border-radius: 10px; border-style: outset; border-color: yellow; border-width: 2px;")


        self.btn1.clicked.connect(lambda: self.scrcpy())
        self.btn2.clicked.connect(lambda: GUI(self))

        self.top_line = QHBoxLayout()
        self.bot_line = QHBoxLayout()

        self.top_line.addWidget(self.btn1)

        self.bot_line.addWidget(self.btn2)

        self.main_line = QVBoxLayout()
        self.main_line.addLayout(self.top_line)
        self.main_line.addLayout(self.bot_line)

        self.widget = QWidget()
        self.widget.setLayout(self.main_line)

        self.setCentralWidget(self.widget)

    def scrcpy(self):
        os.startfile(dir + 'scrcpy.exe')
        self.hide()
        self.quit()



class GUI(QWidget):
    def __init__(self,main_app):

        main_app.hide()

        super().__init__()

        with open('recents.txt') as file:
            self.recents_list = file.readlines()

        self.recents = [i.strip() for i in self.recents_list]

        self.setWindowTitle('Ip Enter')
        self.resize(300, 200)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setStyleSheet("background-color: grey;")

        self.label = QLabel('Enter ip of device:')
        self.label.setStyleSheet(style)

        self.entering = QLineEdit()


        self.entering.setStyleSheet(style)

        self.btn = QPushButton('Confirm')
        self.btn.setStyleSheet(style)

        self.label2 = QLabel('Recent`s:')

        self.top_line = QHBoxLayout()
        self.mid_line = QHBoxLayout()
        self.bot_line = QHBoxLayout()

        self.top_line.addWidget(self.label)
        self.top_line.addWidget(self.entering)
        self.top_line.addWidget(self.btn)
        self.mid_line.addWidget(self.label2)

        for i in self.recents_list[:4]:
            self.recent = QLabel(i)
            self.recent.setStyleSheet(style)
            self.bot_line.addWidget(self.recent)

        self.main_line = QVBoxLayout()
        self.main_line.addLayout(self.top_line)
        self.main_line.addLayout(self.mid_line)
        self.main_line.addLayout(self.bot_line)

        self.btn.clicked.connect(lambda: self.change_recents(self.entering.text()))

        self.setLayout(self.main_line)
        self.show()

    def change_recents(self,ip):

        connect = f'adb connect {ip}'
        sp.run(connect)
        run(dir + 'scrcpy.exe')


        if ip not in self.recents:

            self.recents = self.recents[0:3]
            self.recents.insert(0,ip)


        self.file = open('recents.txt', 'w')
        for i in self.recents:
            self.file.write(f'{i}\n')

        self.file.close()


        self.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = main_window()
    w.show()

    app.exec()