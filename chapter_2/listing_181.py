# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

# Создание и отображение окна
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()            # Создаем окно
window.setWindowTitle("Заголовок окна") # Указываем заголовок
window.resize(300, 50)  # Минимальные размеры
window.show()           # Отображаем окно
sys.exit(app.exec_())



