'''Main Window Style Application'''
# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QStatusBar,
#     QToolBar
# )
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("QMain WIndow")
#         self.setCentralWidget(QLabel("I am the Central Wiidget"))
#         self._createMenu()
#         self._createToolBar()
#         self._createStatusBar()

#     def _createMenu(self):
#         menu=self.menuBar().addMenu("&Menu")
#         menu.addAction("&Exit",self.close)

#     def _createToolBar(self):
#         tools=QToolBar()
#         tools.addAction("&Exit",self.close)
#         self.addToolBar(tools)

#     def _createStatusBar(self):
#         status=QStatusBar()
#         status.showMessage("I am Status Bar")
#         self.setStatusBar(status)

# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     window=Window()
#     window.show()
#     sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import QMainWindow, QApplication


# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.initUI()


#     def initUI(self):

#         self.statusBar().showMessage('Ready')

#         self.setGeometry(300, 300, 350, 250)
#         self.setWindowTitle('Statusbar')
#         self.show()


# def main():

#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())


# if __name__ == '__main__':
#     main()


# import sys
# from PyQt6.QtWidgets import QMainWindow, QApplication
# from PyQt6.QtGui import QIcon, QAction


# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.initUI()


#     def initUI(self):

#         exitAct = QAction(QIcon('exit.png'), '&Exit', self)
#         exitAct.setShortcut('Ctrl+Q')
#         exitAct.setStatusTip('Exit application')
#         exitAct.triggered.connect(QApplication.instance().quit)

#         self.statusBar()

#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu.addAction(exitAct)

#         self.setGeometry(300, 300, 350, 250)
#         self.setWindowTitle('Simple menu')
#         self.show()


# def main():

#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())


# if __name__ == '__main__':
# #     main()


# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QWidget,
#     QLabel,
#     QMainWindow,
#     QStatusBar,
#     QToolBar
# )
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("Main WIndow")
#         self.setCentralWidget(QLabel("I Am the Central Widget"))
#         self._createMenu()
#         self._createToolBox()
#         self._createStatusBar()

#     def _createMenu(self):
#         menu=self.menuBar().addMenu("&Menu")
#         menu.addAction("&Exit",self.close)

#     def _createToolBox(self):
#         tool=QToolBar()
#         tool.addAction("&Exit",self.close)
#         self.addToolBar(tool)

#     def _createStatusBar(self):
#         status=QStatusBar()
#         status.showMessage("I am Status Bar")
#         self.setStatusBar(status)
# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     Window=Window()
#     Window.show()
#     sys.exit(app.exec())                    

# import sys
# from PyQt6.QtWidgets import (
#     QApplication.
#     QLabel,
#     QMainWindow,
#     QWidget,
#     QStatusBar,
#     QToolBar
# )
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("QMain Window")
#         self.setCentralWindow(QLabel("I Am Central Widget"))
#         self._createMenu()
#         self._createToolBar()
#         self._createStatusBar()

#     def _createMenu(self):
#         menu=self.menuBar().addMenu('&Exit')
#         menu.addAction("&Exit",self.close)
