import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QRect

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 设置无边框并置于顶层
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        x = 2  # 圆的半径
        rect = QRect(int(self.width() / 2) - x, int(self.height() / 2) - x, 2*x, 2*x)
        
        painter.setPen(Qt.NoPen)  # 设置无边框
        painter.setBrush(QBrush(Qt.white))  # 设置红色画刷
        painter.drawEllipse(rect)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(400, 400)
    widget.setWindowTitle('Centered Circle')
    widget.show()
    sys.exit(app.exec_())
