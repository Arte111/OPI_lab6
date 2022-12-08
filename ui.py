from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import sys
import time

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
                            amount=int(self.many.value()), 
                            minvalue=int(self.min.value()), 
                            maxvalue=int(self.max.value()))
            self.mainMass.clear()
            start_gui_draw = time.time()
            array = massObj.get_array()
            for elem in array:
                self.mainMass.addItem(str(elem))
            end_gui_draw = time.time() - start_gui_draw
            if self.typeAct.currentText() == "Сложение":
                self.logs.addItem(f"Значение: {massObj.sum_array()[0]}\tВремя: {massObj.sum_array()[1]} Время отрисовки: {end_gui_draw}")
            if self.typeAct.currentText() == "Вычитание":
                self.logs.addItem(f"Значение: {massObj.diff_array()[0]}\tВремя: {massObj.diff_array()[1]} Время отрисовки: {end_gui_draw}")
            if self.typeAct.currentText() == "Умножение":
                self.logs.addItem(f"Значение: {massObj.mult_array()[0]}\tВремя: {massObj.mult_array()[1]} Время отрисовки: {end_gui_draw}")
            if self.typeAct.currentText() == "Деление":
                self.logs.addItem(f"Значение: {massObj.div_array()[0]}\tВремя: {massObj.div_array()[1]} Время отрисовки: {end_gui_draw}")
            if self.typeAct.currentText() == "sin":
                self.logs.addItem(f"Время: {massObj.sin_array()} Время отрисовки: {end_gui_draw}")
            if self.typeAct.currentText() == "cos":
                self.logs.addItem(f"Время: {massObj.cos_array()} Время отрисовки: {end_gui_draw}")
            if self.typeAct.currentText() == "tan":
                self.logs.addItem(f"Время: {massObj.tan_array()} Время отрисовки: {end_gui_draw}")

    def clear_func(self):
        self.logs.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
