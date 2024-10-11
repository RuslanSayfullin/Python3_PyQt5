# Использование класса QWinTaskbarProgress
from PyQt5 import QtCore, QtWidgets, QtWinExtras
import sys, time

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Класс QWinTaskbarProgress")
        # Создаем кнопку панели задач
        self.taskbarButton = QtWinExtras.QWinTaskbarButton(parent=self)
        # Получаем индикатор процесса, задаем его параметры
        # и делаем его видимым
        self.progress = self.taskbarButton.progress()
        self.progress.setRange(0, 10)
        self.progress.show()
        # Создаем необходимые кнопки
        vbox = QtWidgets.QVBoxLayout()
        btnStart = QtWidgets.QPushButton("&Пуск")
        btnStart.clicked.connect(self.start)
        vbox.addWidget(btnStart)
        btnPause = QtWidgets.QPushButton("Па&уза")
        btnPause.clicked.connect(self.progress.pause)
        vbox.addWidget(btnPause)
        btnStop = QtWidgets.QPushButton("&Стоп")
        btnStop.clicked.connect(self.progress.stop)
        vbox.addWidget(btnStop)
        btnResume = QtWidgets.QPushButton("П&родолжить")
        btnResume.clicked.connect(self.progress.resume)
        vbox.addWidget(btnResume)
        self.setLayout(vbox)
        self.resize(100, 100)

    # После вывода окна на экран привязываем его к кнопке панели задач
    def showEvent(self, evt):
        self.taskbarButton.setWindow(self.windowHandle())
    
    # При нажатии кнопки "Пуск" последовательно, с секундным промежутком
    # увеличиваем значение индикатора от 0 до 10, конечно, если индикатор
    # не поставлен на паузу и не остановлен
    def start(self):
        i = 0
        while i < 11:
            if not self.progress.isPaused() and not self.progress.isStopped():
                self.progress.setValue(i)
                i += 1
            time.sleep(1)
            QtWidgets.qApp.processEvents()
        self.progress.reset()

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())