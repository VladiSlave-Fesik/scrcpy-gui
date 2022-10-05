from PyQt5 import QtGui
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout,QMessageBox,QLineEdit


with open('recents.txt') as file:
    recents_list = file.readlines()


recents = [i.strip() for i in recents_list]

def change_recents(ip):
    recents[3] = recents[2]
    recents[2] = recents[1]
    recents[1] = recents[0]
    recents[0] = ip

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Ip Enter')
main_win.resize(300,200)
main_win.setWindowIcon(QtGui.QIcon('icon.ico'))
main_win.setStyleSheet("background-image : url(back.png)")

label = QLabel('Enter ip of device:')
entering = QLineEdit()
entering.setMaxLength(20)
btn = QPushButton('Confirm')
label2 = QLabel('Recent`s ip:')

top_line = QHBoxLayout()
mid_line = QHBoxLayout()
bot_line = QHBoxLayout()

top_line.addWidget(label)
top_line.addWidget(entering)
top_line.addWidget(btn)

mid_line.addWidget(label2)

for i in recents_list[:4]:
    recent = QLabel(i)
    bot_line.addWidget(recent)

main_line = QVBoxLayout()
main_line.addLayout(top_line)
main_line.addLayout(mid_line)
main_line.addLayout(bot_line)

btn.clicked.connect(lambda : change_recents(entering.text()))

main_win.setLayout(main_line)
main_win.show()
app.exec()



file = open('recents.txt','w')
for i in recents:
    file.write(f'{i}\n')

file.close()