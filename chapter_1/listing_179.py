# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import ui_MyForm

class MyWindow(QtWidgets.QWidget):
    """Использование класса формы. Вариант 2"""
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ui_MyForm.Ui_MyForm()
        self.ui.setupUi(self)
        self.ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())