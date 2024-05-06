# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets
import sys

# Смена значка в заголовке окна
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Смена значка в заголовке окна")
window.resize(300, 100)
ico = QtGui.QIcon("icon.png")
window.setWindowIcon(ico)   # Значок для окна
app.setWindowIcon(ico)      # Значок приложения
window.show()
sys.exit(app.exec_())