# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
from listing_172 import MyWindow

class MyWindow(QtWidgets.QWidget):
    """Использование функции loadUi(). Вариант 2"""
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi("MyForm.ui", self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = MyWindow()
        window.show()
        sys.exit(app.exec_())