# Использование функции loadUiType(). Вариант 2
from PyQt5 import QtWidgets, uic
from listing_172 import MyWindow

Form, Base = uic.loadUiType("MyForm.ui")

class MyWindow(QtWidgets.QWidget, Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())