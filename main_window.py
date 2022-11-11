import sys
from PyQt6.QtWidgets import ( 
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QLabel(' I am the central Widget'))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        menu=self.menuBar().addMenu("&Menu")
        menu.addAction("*Exit",self.close)


    def _createToolBar(self):
        tools=QToolBar()
        tools.addAction("Exit", self.close) 
        self.addToolBar(tools) 

    def _createStatusBar(self):
        status=QStatusBar()
        status.showMessage(" I am The Status Bar")      
        self.setStatusBar(status)

if __name__=="__main__":
    app=QApplication([])
    window= window()
    window.show()
    sys.exit(app.exec())
