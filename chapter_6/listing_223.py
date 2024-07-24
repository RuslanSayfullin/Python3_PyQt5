# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets
import sys

# Простой список QListView
lv = QtWidgets.QListView()
sti = QtGui.QStandardItemModel(parent = window)
lst = ['Perl', 'PHP', 'Python', 'Ruby']
for row in range(0, 4):
    if row == 2:
        iconfile = 'python.png'
    else:
        iconfile = 'icon.png'
    item = QtGui.QStandardItem(QtGui.QIcon(iconfile), lst[row])
    sti.appendRow(item)
lv.setModel(sti)