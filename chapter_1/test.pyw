from PyQt6 import QtWidgets
import MyWindow

class MyDialog(QtWidgets.QDialog):
    def __init__ (self, parent=None):
        QtWidgets.QDialog. init (self, parent)
        self.myWidget = MyWindow.MyWindow()
        self.myWidget.vbox.setContentsMargins(0, О, О, О)
        self.button = QtWidgets.QPushВutton("&Измeнить надпись")
        mainBox = QtWidgets.QVВoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText("Hoвaя надпись")
        self.button.setDisaЫed(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowТitle("Пpeимyщecтвo ООП-стиля")
    window.resize(З00, 100)
    window.show()
    sys.exit(app.exec())
