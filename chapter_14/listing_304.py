# Создание панели инструментов на миниатюре приложения
from PyQt5 import QtCore, QtWidgets, QtGui, QtWinExtras
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Панель инструментов на миниатюре")
        # Создаем значки для кнопок
        icon1 = QtGui.QIcon("icon3.png")
        icon2 = QtGui.QIcon("icon4.png")
        icon3 = QtGui.QIcon("icon5.png")
        # Создаем панель инструментов
        self.thumbnailToolbar = QtWinExtras.QWinThumbnailToolBar(parent=self)
        # Создаем первые две кнопки
        button1 = QtWinExtras.QWinThumbnailToolButton(parent=self)
        button1.setIcon(icon1)
        button1.setToolTip("Кнопка 1")
        button1.setDismissOnClick(True)
        button1.clicked.connect(self.button1Clicked)
        self.thumbnailToolbar.addButton(button1)
        button2 = QtWinExtras.QWinThumbnailToolButton(parent=self)
        button2.setIcon(icon2)
        button2.setToolTip("Кнопка 2")
        button2.setDismissOnClick(True)
        button2.clicked.connect(self.button2Clicked)
        self.thumbnailToolbar.addButton(button2)
        # Создаем кнопку, что сформирует свободное пространство
        # между второй и третьей кнопками
        button0 = QtWinExtras.QWinThumbnailToolButton(parent=self)
        button0.setInteractive(False)
        button0.setFlat(True)
        self.thumbnailToolbar.addButton(button0)
        # Создаем третью кнопку
        button3 = QtWinExtras.QWinThumbnailToolButton(parent=self)
        button3.setIcon(icon3)
        button3.setToolTip("Кнопка 3")
        button3.clicked.connect(self.button3Clicked)
        self.thumbnailToolbar.addButton(button3)
        # Создаем надпись, куда будут выводиться сообщения о нажатии
        # кнопок панели инструментов, и кнопку выхода
        vbox = QtWidgets.QVBoxLayout()
        self.lblOutput = QtWidgets.QLabel(parent=self)
        vbox.addWidget(self.lblOutput)
        btnClose = QtWidgets.QPushButton("&Выход")
        btnClose.clicked.connect(QtWidgets.qApp.quit)
        vbox.addWidget(btnClose)
        self.setLayout(vbox)
        self.resize(200, 100)
    
    # После вывода окна на экран привязываем его к панели инструментов
    def showEvent(self, evt):
        self.thumbnailToolbar.setWindow(self.windowHandle())
    # Выводим в надпись сообщения о нажатии кнопок
    def button1Clicked(self):
        self.lblOutput.setText("Нажата кнопка 1")
    def button2Clicked(self):
        self.lblOutput.setText("Нажата кнопка 2")
    def button3Clicked(self):
        self.lblOutput.setText("Нажата кнопка 3")


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())