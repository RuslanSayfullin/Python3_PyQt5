# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic


class MyWindow(QtWidgets.QWidget):
    """Использование функции loadUiType() Вариант 1"""
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("chapter_17/MyForm.ui")
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())