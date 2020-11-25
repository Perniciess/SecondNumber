# -*- coding: utf-8 -*-
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(800, 800, 800, 800)
        uic.loadUi('second.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.ellips(qp)
            self.do_paint = False
            qp.end()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            rec = randint(0, 800)
            x = randint(0, 800)
            y = randint(0, 800)
            qp.drawEllipse(x, y, rec, rec)
            self.do_paint = False
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())