
from PyQt5.QtWidgets import *


app = QApplication([])


window = QWidget()



Start = QPushButton("Старт")
Shop =  QPushButton("Магазин")

mainLine = QVBoxLayout()

mainLine.addWidget(Start)
mainLine.addWidget(Shop)

window.setLayout(mainLine)

window.show()
app.exec()