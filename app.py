from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout,QMessageBox,QLineEdit

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Ip Enter')
main_win.resize(300,200)
main_win.setWindowIcon(QtGui.QIcon('icon.ico'))
main_win.setStyle('back.png')

label = QLabel('Enter ip of device:')
entering = QLineEdit()
label2 =    QLabel('Recent:')

top_line = QHBoxLayout()
mid_line = QHBoxLayout()
bot_line = QHBoxLayout()

top_line.addWidget(label)
top_line.addWidget(entering)

bot_line.addWidget(label2)

main_line = QVBoxLayout()
main_line.addLayout(top_line)
main_line.addLayout(mid_line)
main_line.addLayout(bot_line)


main_win.setLayout(main_line)
main_win.show()
app.exec()