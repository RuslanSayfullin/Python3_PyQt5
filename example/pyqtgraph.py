import pyqtgraph as pg

# Создание графического окна
win = pg.GraphicsWindow()
win.setWindowTitle('Example')

# Создание объекта PlotWidget
plot_widget = win.addPlot()

# Установка диапазона осей X и Y
plot_widget.setRange(xRange=[0, 10], yRange=[-5, 5])

# Отображение окна
win.show()