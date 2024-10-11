# Вывод метаданных мультимедийного файла
from PyQt5 import QtCore, QtWidgets, QtMultimedia
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Метаданные")
        self.mplPlayer = QtMultimedia.QMediaPlayer()
        self.mplPlayer.setVolume(50)
        self.mplPlayer.mediaStatusChanged.connect(self.showMetadata)
        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton("&Открыть файл...")
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)
        # Создаем доступное только для чтения многострочное текстовое
        # поле, в которое будет выводиться результат
        self.txtOutput = QtWidgets.QTextEdit()
        self.txtOutput.setReadOnly(True)
        vbox.addWidget(self.txtOutput)
        self.setLayout(vbox)
        self.resize(300, 250)
    
    def openFile(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(parent=self, caption = "Выберите звуковой файл",filter = "Звуковые файлы (*.mp3 *.ac3)")
        self.mplPlayer.setMedia(QtMultimedia.QMediaContent(file[0]))

    def showMetadata(self, state):
        self.txtOutput.clear()
        # Как только файл будет загружен...
        if state == QtMultimedia.QMediaPlayer.LoadedMedia:
            # ...извлекаем ключи всех доступных метаданных...
            keys = self.mplPlayer.availableMetaData()
            s = ""
            # ...перебираем их в цикле...
            for k in keys:
                v = self.mplPlayer.metaData(k)
                # ...на случай пустых списков проверяем, действительно
                # ли по этому ключу хранится какое-то значение...
                if v:
                    # ...если значение представляет собой список,
                    # преобразуем его в строку...
                    if v is list:
                        v = ", ".join(v)
                    # ...формируем на основе значений текст...
                    s += "<strong>" + k + "</strong>: " + str(v) + "<br>"
            # ...и выводим его в текстовое поле
            self.txtOutput.setHtml(s)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())