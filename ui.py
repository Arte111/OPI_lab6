from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import sys

from controller import model


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.createB.clicked.connect(self.create_func)
        self.clear.clicked.connect(self.clear_func)

    def create_func(self):
        if self.min.value() < self.max.value():
            massObj = model(array_type=self.typeVar.currentText(),
                            data_collector=self.collectionType.currentText(),
                            amount=int(self.many.value()), 
                            minvalue=int(self.min.value()), 
                            maxvalue=int(self.max.value()))
            array = massObj.get_array()
            self.mainMass.clear()
            for elem in array:
                self.mainMass.addItem(str(elem))
            if self.typeAct.currentText() == "Сложение":
                self.logs.addItem(f"Значение: {massObj.sum_array()[0]}\tВремя: {massObj.sum_array()[1]}")
            if self.typeAct.currentText() == "Вычитание":
                self.logs.addItem(f"Значение: {massObj.diff_array()[0]}\tВремя: {massObj.diff_array()[1]}")
            if self.typeAct.currentText() == "Умножение":
                self.logs.addItem(f"Значение: {massObj.mult_array()[0]}\tВремя: {massObj.mult_array()[1]}")
            if self.typeAct.currentText() == "Деление":
                self.logs.addItem(f"Значение: {massObj.div_array()[0]}\tВремя: {massObj.div_array()[1]}")
            if self.typeAct.currentText() == "sin":
                self.logs.addItem(f"Время: {massObj.sin_array()}")
            if self.typeAct.currentText() == "cos":
                self.logs.addItem(f"Время: {massObj.cos_array()}")
            if self.typeAct.currentText() == "tan":
                self.logs.addItem(f"Время: {massObj.tan_array()}")

    def clear_func(self):
        self.logs.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())