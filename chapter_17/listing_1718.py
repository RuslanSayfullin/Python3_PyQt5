def change_x(self):
    ml = QtCore.QMutexLocker(MyThread.mutex)
    print("x =", MyThread.x, "id =", self.id)
    MyThread.x += 5
    self.sleep(2)
    print("x =", MyThread.x, "id =", self.id)
    MyThread.x += 34
    print("x =", MyThread.x, "id =", self.id)
    # Блокировка автоматически снимется