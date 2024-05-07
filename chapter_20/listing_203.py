# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

# Использование контейнера QGridLayout
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()                # Родительский компонент — окно
window.setWindowTitle("QGridLayout")
window.resize(150, 100)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
button4 = QtWidgets.QPushButton("4")
grid = QtWidgets.QGridLayout()              # Создаем сетку
grid.addWidget(button1, 0, 0)               # Добавляем компоненты
grid.addWidget(button2, 0, 1)
grid.addWidget(button3, 1, 0)
grid.addWidget(button4, 1, 1)
window.setLayout(grid)                      # Передаем ссылку родителю
window.show()
sys.exit(app.exec_())



