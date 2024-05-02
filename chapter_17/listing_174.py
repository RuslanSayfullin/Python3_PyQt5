# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import sys

# Использование функции loadUi() . Вариант 1
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("chapter_17/MyForm.ui")
window.btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())