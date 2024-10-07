# Использование методов prepare(), addBindValue() и exec_()
from PyQt5 import QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
query = QtSql.QSqlQuery()
# Добавляем в только что созданную таблицу good запись,
# используя SQL-команду INSERT
query.prepare("insert into good values(null, ?, ?)")
query.addBindValue('Дискета')
query.addBindValue(10)
query.exec_()
con.close()