# Использование функции loadUi(). Вариант 1
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("MyForm.ui")
window.btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())