import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("yellowCircles.ui", self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_cyrcle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_cyrcle(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        l = random.randint(5, 255)
        qp.drawEllipse(random.randint(5, 100), random.randint(5, 100), l, l)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())