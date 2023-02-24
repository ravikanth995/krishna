import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, \
                            QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon


class ProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximum(100)
        self._active = False

    def updateBar(self, i):
        while True:
            time.sleep(0.01)
            value= self.value() + i
            self.setValue(value)

            if value >= 50:
                self.changeColor('green')

            if value >= self.maximum() or self._active:
                self.setValue(100)
                break
            elif value >= self.maximum() or not self._active:
                break               

    def changeColor(self, color):
        css = """
            ::chunk {{
                background: {0};
            }}
        """.format(color)
        self.setStyleSheet(css)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 200
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle('ProgressBar Template')
        self.setWindowIcon(QIcon('qt.ico'))
        self.setStyleSheet("""

            QWidget {
                background-color: #323232;
                font-size: 20px;
                color: #b1b1b1;
            }

            QPushButton {
                height: 45px;
                background-color: QLinearGradient(
                    x1: 0,
                    x2: 0,
                    y1: 0,
                    y2: 1,
                    stop: 0 #565656,
                    stop: 0.1 #525252,
                    stop: 0.5 #4e4e4e,
                    stop: 0.9 #4a4a4a,
                    stop: 1.0 #464646
                );
                border-width: 4.5px;
                border-color: #1e1e1e;
                border-style: solid;
                border-radius: 3px;
                padding: 5px;
                padding-left: 10px;
                padding-right: 10px;
            }

            QPushButton:pressed {
                background-color: orange;
                color: white;

            }

            QPushButton:hover {
                border-color: orange;
                border-color: white;
            }

            QProgressBar {
                border-style: solid;
                border-color: grey;
                border-radius: 7px;
                border-width: 2px;
                text-align: center;
            }

            QProgressBar::chunk {
                width: 2px;
                background-color: #de7c09;
                margin: 3px;
            }

        """)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.progressBar = ProgressBar()
        self.layout.addWidget(self.progressBar)

        self.button = QPushButton('Update ProressBar', clicked=self.updateProgressBar)
        self.layout.addWidget(self.button)

    def updateProgressBar(self):
        i = 10
        self.progressBar.updateBar(i)


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')

