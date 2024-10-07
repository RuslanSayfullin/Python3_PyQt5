# Использование метода bindValue() для задания параметров по их символьным обозначениям
from PyQt5 import QtWidgets, QtSql
import sys

app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
query = QtSql.QSqlQuery()
query.prepare("insert into good values(null, :name, :count)")
query.bindValue(':name', 'Флеш-накопитель')
query.bindValue(':count', 20)
query.exec_()
con.close()
