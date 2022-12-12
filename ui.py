from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import sys
import time

from controller import model, intmodel


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.createB.clicked.connect(self.create_func)
        self.clear.clicked.connect(self.clear_func)

    def create_func(self):
        if self.min.value() < self.max.value():
            if self.typeVar.currentText() == "decimal":
                massObj = model(array_type=self.typeVar.currentText(),
                                amount=int(self.many.value()), 
                                minvalue=int(self.min.value()), 
                                maxvalue=int(self.max.value()))
            else:
                massObj = intmodel(array_type=self.typeVar.currentText(),
                                amount=int(self.many.value()), 
                                minvalue=int(self.min.value()), 
                                maxvalue=int(self.max.value()))
            self.mainMass.clear()
            start_gui_draw = time.time()
            array = massObj.get_array()
            if len(array) > 100000 and self.mode.currentText() == "Укороченный режим":
                maxi = 100000
            else:
                maxi = len(array)
            for i in range(maxi):
                self.mainMass.addItem(str(array[i]))
            end_gui_draw = time.time() - start_gui_draw
            if self.typeAct.currentText() == "Сложение":
                result = massObj.sum_array()
                self.logs.addItem(f"Значение: {result[0]}\tВремя: {result[1] + result[2]} + {end_gui_draw}")
            if self.typeAct.currentText() == "Вычитание":
                result = massObj.diff_array()
                self.logs.addItem(f"Значение: {result[0]}\tВремя: {result[1] + result[2]} + {end_gui_draw}")
            if self.typeAct.currentText() == "Умножение":
                result = massObj.mult_array()
                self.logs.addItem(f"Значение: {result[0]}\tВремя: {result[1] + result[2]} + {end_gui_draw}")
            if self.typeAct.currentText() == "Деление":
                result = massObj.div_array()
                self.logs.addItem(f"Значение: {result[0]}\tВремя: {result[1] + result[2]} + {end_gui_draw}")


    def clear_func(self):
        self.logs.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
