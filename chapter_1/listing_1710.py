from PyQt5 import QtWidgets
import ui_MyForm

class MyWindow(QtWidgets.QWidget, ui_MyForm.Ui_MyForm):
    """Использование класса формы. Вариант 3"""
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