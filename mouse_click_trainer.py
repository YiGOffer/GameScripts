import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QTimer, QPoint


g_circle_size = 40
gr = 255 
gg = 255
gb = 255
gt = 100 # 透明度0.5
g_total = 0
g_hit = 0

class CircleWidget(QWidget):
    def __init__(self):
        global g_circle_size
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 设置无边框并置于顶层
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明

        self.circles = []  # 存储所有圆的位置信息
        self._circle_size = g_circle_size
        self._r = gr
        self._g = gg
        self._b = gb
        self._transition = gt

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateCircle)  # 每次定时器超时时触发更新
        self.timer.start(500)  # 每隔1秒更新一次

    def updateCircle(self):
        if len(self.circles) > 100:
            return
        # 随机生成新的圆的位置
        circle_x = random.randint(0, self.width() - self._circle_size)
        circle_y = random.randint(0, self.height() - self._circle_size)
        self.circles.append((circle_x, circle_y))
        self.update()  # 触发重绘事件

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制所有圆
        painter.setPen(Qt.NoPen)
        for circle_x, circle_y in self.circles:
            color = QColor(self._r, self._g, self._b, self._transition)  # 设置颜色为半透明的白色，透明度为128 (0.5 * 255)
            painter.setBrush(QBrush(color))
            painter.drawEllipse(circle_x, circle_y, self._circle_size, self._circle_size)

    def mousePressEvent(self, event):
        click_pos = event.pos()
        global g_total
        global g_hit
        g_total = g_total + 1
        for circle_x, circle_y in self.circles:
            distance = QPoint(circle_x + self._circle_size // 2, circle_y + self._circle_size // 2) - click_pos
            if distance.manhattanLength() <= self._circle_size // 2:
                self.circles.remove((circle_x, circle_y))
                self.update()
                g_hit = g_hit + 1
                print("total num = ", g_total, " , hit num = ", g_hit, " , rate = ", g_hit / g_total * 100, "%")
                break

if __name__ == '__main__':
    app = QApplication(sys.argv)

    circle_widget = CircleWidget()
    screen_geometry = app.desktop().availableGeometry()
    circle_widget.resize(screen_geometry.width(), screen_geometry.height())
    circle_widget.show()

    sys.exit(app.exec_())