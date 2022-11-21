import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("yellowCircles.ui", self)
        self.pushButton.clicked.connect(self.startPaint)

    def startPaint(self):
        # Создаем объект QPainter для рисования

        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_cyrcle(qp)
        # Завершаем рисование
        qp.end()

    def draw_cyrcle(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        qp.drawEllipse(5, 5, 100, 100)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())