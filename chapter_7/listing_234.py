# Использование метода bindValue() для задания параметров по их порядковым номерам

from PyQt5 import QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
query = QtSql.QSqlQuery()
query.prepare("insert into good values(null, ?, ?)")
query.bindValue(0, 'Компакт-диск')
query.bindValue(1, 5)
query.exec_()
con.close()