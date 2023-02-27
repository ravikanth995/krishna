# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QDialog,
#     QDialogButtonBox,
#     QFormLayout,
#     QLineEdit,
#     QVBoxLayout,
    # QWidget
# )
# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QDialog,
#     QDialogButtonBox,
#     QFormLayout,
#     QLineEdit,
#     QVBoxLayout,
#     QWidget
# )


# class Window(QDialog):
#     def __init__(self):
#         super().__init__(parent=None)
#         window=QWidget()
#         window.setGeometry(100,100,250,80)
#         self.setWindowTitle("Facebook login")
#         dialogLayout=QVBoxLayout()
#         formLayout=QFormLayout()
#         formLayout.addRow("Enter Email:",QLineEdit())
#         formLayout.addRow("Enter PassWord:",QLineEdit())
#         dialogLayout.addLayout(formLayout)
#         buttons=QDialogButtonBox()
#         buttons.setStandardButtons(
#             QDialogButtonBox.StandardButton.Cancel
#             | QDialogButtonBox.StandardButton.Ok

#         )
#         dialogLayout.addWidget(buttons)
#         self.setLayout(dialogLayout)
# if __name__=="__main__":
#     app=QApplication([])
#     Window=Window()
#     Window.show()
#     sys.exit(app.exec())        

# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QVBoxLayout,
#     QHBoxLayout,
#     QDialogButtonBox,
#     QLineEdit,
#     QDialog,
#     QFormLayout,
# )
# class Window(QDialog):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("Instagram Login")
#         dialogLayout=QHBoxLayout()
#         formLayout=QFormLayout()
#         formLayout.addRow("Email:",QLineEdit())
#         formLayout.addRow("Password:",QLineEdit())
#         dialogLayout.addLayout(formLayout)
#         buttons=QDialogButtonBox()
#         buttons.setStandardButtons(
#             QDialogButtonBox.StandardButton.Cancel
#             | QDialogButtonBox.StandardButton.Ok

#             # QDialogButtonBox.StandardButton.Cancel
#             # | QDialogButtonBox.StandardButton.Ok
#         )

#         dialogLayout.addWidget(buttons)
#         self.setLayout(dialogLayout)
# if __name__=="__main__":
#     app=QApplication([])
#     window=Window()
#     window.show()
#     sys.exit(app.exec())        

# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QVBoxLayout,
#     QDialogButtonBox,
#     QLineEdit,
#     QDialog,
#     QFormLayout,
#     QWidget
# )

# class Window(QDialog):
#     def __init__(self):
#         super().__init__(parent=None)
#         # window1=QWidget()
#         self.setWindowTitle("Government Data Info.in")
#         # window1.setGeometry(100,100,250,80)
#         dialogLayout=QVBoxLayout()
#         formLayout=QFormLayout()
#         formLayout.addRow("Email:",QLineEdit())
#         formLayout.addRow("PassWord:",QLineEdit())
#         dialogLayout.addLayout(formLayout)
#         buttons=QDialogButtonBox()
#         buttons.setStandardButtons(
#             QDialogButtonBox.StandardButton.Cancel
#             | QDialogButtonBox.StandardButton.Ok
#         )
#         dialogLayout.addWidget(buttons)
#         self.setLayout(dialogLayout)
# if __name__=="__main__":
#     app=QApplication([])
#     window=Window()
#     # window1.show()
#     sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton

# app = QApplication(sys.argv)

# window = QPushButton("Push Me")
# window.show()

# app.exec()

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow

# app = QApplication(sys.argv)

# window = QMainWindow()
# window.show()

# # Start the event loop.
# app.exec()

# import sys

# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# # Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")
#         button = QPushButton("Press Me!")

#         # Set the central widget of the Window.
#         self.setCentralWidget(button)

# import sys

# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# # Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = QPushButton("Press Me!")

#         self.setFixedSize(QSize(400, 300))

#         # Set the central widget of the Window.
#         self.setCentralWidget(button)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()


# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = QPushButton("Press Me!")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)

#         # Set the central widget of the Window.
#         self.setCentralWidget(button)

#     def the_button_was_clicked(self):
#         print("Clicked!")


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()
# app.exec()
# import sys
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = QPushButton("Press Me!")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         button.clicked.connect(self.the_button_was_toggled)

#         self.setCentralWidget(button)

#     def the_button_was_clicked(self):
#         print("Clicked!")

#     def the_button_was_toggled(self, checked):
#         print("Checked?", checked)
# app=MainWindow()
# sys.exit(app.exec())

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.button_is_checked = True

#         self.setWindowTitle("My App")

#         self.button = QPushButton("Press Me!")
#         self.button.setCheckable(True)
#         self.button.released.connect(self.the_button_was_released)
#         self.button.setChecked(self.button_is_checked)

#         self.setCentralWidget(self.button)

#     def the_button_was_released(self):
#         self.button_is_checked = self.button.isChecked()

#         print(self.button_is_checked)

# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# import sys
# from random import choice

# window_titles = [
#     'My App',
#     'My App',
#     'Still My App',
#     'Still My App',
#     'What on earth',
#     'What on earth',
#     'This is surprising',
#     'This is surprising',
#     'Something went wrong'
# ]


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.n_times_clicked = 0

#         self.setWindowTitle("My App")

#         self.button = QPushButton("Press Me!")
#         self.button.clicked.connect(self.the_button_was_clicked)

#         self.windowTitleChanged.connect(self.the_window_title_changed)

#         # Set the central widget of the Window.
#         self.setCentralWidget(self.button)

#     def the_button_was_clicked(self):
#         print("Clicked.")
#         new_window_title = choice(window_titles)
#         print("Setting title:  %s" % new_window_title)
#         self.setWindowTitle(new_window_title)

#     def the_window_title_changed(self, window_title):
#         print("Window title changed: %s" % window_title)

#         if window_title == 'Something went wrong':
#             self.button.setDisabled(True)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()

#Radio Button
'''A QRadioButton class object presents a selectable button with a text label. 
The user can select one of many options presented on the form. This class is derived from QAbstractButton class.

Radio buttons are autoexclusive by default. 
Hence, only one of the radio buttons in the parent window can be selected at a time.
If one is selected, previously selected button is automatically deselected.
Radio buttons can also be put in a QGroupBox or QButtonGroup to create more than one selectable fields on the parent window.

'''
import sys
# from PyQt6.QtWidgets import QApplication, QWidget
# from PyQt6.QtGui import QIcon
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.title='First GUI'
#         self.left=10
#         self.top=10
#         self.width=300
#         self.height=250
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left,self.top,self.width,self.height)
#         self.show()
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=App()
#     sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget,QMainWindow
# from PyQt6.QtGui import QIcon
# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.title='Status Bar'
#         self.left=10
#         self.top=10
#         self.width=300
#         self.height=250
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left,self.top,self.width,self.height)
#         self.statusBar().showMessage('In progress') #Adding a Status Bar
#         self.show()
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=App()
#     sys.exit(app.exec())

"QMainWindow’ : that handles the status bar"

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget,QPushButton
# from PyQt6.QtGui import QIcon
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.title='Button Widget'
#         self.left=10
#         self.top=10
#         self.width=300
#         self.height=250
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left,self.top,self.width,self.height)
#         button=QPushButton('Click',self) #creating a instance of QPushButton class
#         button.setToolTip('This is a button') #Adding the tool tip text for the button object created
#         button.move(100,125) #Setting the location of the button
#         self.show()
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=App()
#     sys.exit(app.exec())


# PyQt Signals and Slots
# When an event occurs like a button click, user input, etc., then the widget sends signals. 
# We can set an action to occur when a particular event occurs. 
# The event here is the signal and the corresponding action is the slot.

# Let us see an example where the status bar message is shown on clicking a status bar

import sys
# from PyQt6.QtWidgets import *
# class App(QMainWindow):
#     def slot_func(self): # function that runs on button click
#         self.statusBar().showMessage('Button clicked') #Adding a Status Bar
#     def __init__(self):
#         super().__init__()
#         self.title='Signals & Slots'
#         self.left=10
#         self.top=10
#         self.width=300
#         self.height=250
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left,self.top,self.width,self.height)
#         button=QPushButton('Click',self) #creating a instance of QPushButton class
#         button.clicked.connect(self.slot_func) #adding an action on button click
#         button.move(100,125) #Setting the location of the button
#         self.show()
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=App()
#     sys.exit(app.exec())

# TextBox :
# The text boxes are mainly used to take input from the user. 
# We can use setText() and getText() methods from the QLineEdit class

# import sys
# from PyQt6.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QLineEdit,QMessageBox
# from PyQt6.QtCore import pyqtSlot
# from PyQt6.QtGui import QIcon
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.title='Text Box'
#         self.left=10
#         self.top=10
#         self.width=300
#         self.height=250
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left,self.top,self.width,self.height)
#         self.textbox=QLineEdit(self)
#         self.textbox.move(50,50)
#         self.textbox.resize(180,40)
#         self.button=QPushButton('Click',self)
#         self.button.move(100,100)
#         self.button.clicked.connect(self.click_func)
#         self.show()
#     def click_func(self):
#         textboxValue=self.textbox.text()
#         QMessageBox.question(self, 'Welcome','Hello!'+textboxValue, QMessageBox.Ok, QMessageBox.Ok)                
#         self.textbox.setText("")
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=App()
#     sys.exit(app.exec())

# from PyQt6.QtWidgets import (
#     QApplication,
#     QRadioButton,
#     QHBoxLayout,
#     QVBoxLayout,
#     QLabel,
#     QWidget,
#     QDialogButtonBox,
#     QLineEdit,
#     QFormLayout,
#     QDialog
# )

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#     def initUi(self):
#         vbox=QVBoxLayout()
#         hbox=QHBoxLayout()
#         rb1=QRadioButton("Large:",self)
#         rb1.toggled.connect(self.updateLabel)
#         rb2=QRadioButton("Medium:",self)
#         rb2.toggled.connect(self.updateLabel)
#         rb3=QRadioButton("Small:",self)
#         rb3.toggled.connect(self.updateLabel)

#         self.Label=QLabel(" ",self)
#         hbox.addWidget(rb1)
#         hbox.addWidget(rb2)
#         hbox.addWidget(rb3)
        
#         vbox.addSpacing(15)
#         vbox.addLayout(hbox)
#         vbox.addWidget(self.Label)

#         self.setLayout(vbox)
#         self.setGeometry(100,200,350,200)
#         self.setWindowTitle("Radio-Button")
#         self.show()
           
#         dialogLayout=QVBoxLayout()
#         formLayout=QFormLayout()
#         formLayout=QFormLayout()
#         formLayout.addRow("Username:",QLineEdit())
#         formLayout.addRow("Email:",QLineEdit())
#         formLayout.addRow("Password:",QLineEdit())   
#         buttons=QDialogButtonBox()
#         buttons.setStandardButtons(
#             QDialogButtonBox.StandardButton.Ok
#             | QDialogButtonBox.StandardButton.Cancel
#         )
#         dialogLayout.addWidget(buttons)
#         self.setLayout(dialogLayout)

#     def updateLabel(self):
#         rbtn=self.sender()
#         if rbtn.isChecked()==True:
#           self.Label.setText(rbtn.text())
# def main():
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec())
# if __name__=="__main__":
    # main()
# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QDialog,
#     QDialogButtonBox,
#     QFormLayout,
#     QLineEdit,
#     QVBoxLayout,
# )

# class Window(QDialog):
#     def __init__(self):
#         super().__init__(parent=None)
        
#         self.setWindowTitle("Dialog App")
#         diaogLayout=QVBoxLayout()
#         formLayout=QFormLayout()

#         formLayout.addRow("Username:",QLineEdit())
#         formLayout.addRow("e-Mail:",QLineEdit())
#         formLayout.addRow("Password:",QLineEdit())
#         diaogLayout.addLayout(formLayout)
#         buttons=QDialogButtonBox()
#         buttons.setStandardButtons(
#             QDialogButtonBox.StandardButton.Cancel
#             | QDialogButtonBox.StandardButton.Ok
#         )

#         diaogLayout.addWidget(buttons)
#         self.setLayout(diaogLayout)
# if __name__=="__main__":
#     app=QApplication(sys.argv) 
#     window=Window()
#     window.show()
#     sys.exit(app.exec())       

# import sys
# from PyQt6.QtWidgets import (
#  QApplication,
#  QDialog,
#  QWidget,
#  QDialogButtonBox,
#  QVBoxLayout,
#  QLineEdit,
#  QFormLayout
# )

# class Window(QDialog):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("Python App")

#         dialogLayout=QVBoxLayout()
#         formLayout=QFormLayout()
#         formLayout.addRow("Enter Username:",QLineEdit())
#         formLayout.addRow("Enter e-Mail:",QLineEdit())
#         formLayout.addRow("Enter Password:",QLineEdit())
#         dialogLayout.addLayout(formLayout)

#         buttons=QDialogButtonBox()
#         buttons.setStandardButtons(
#             QDialogButtonBox.StandardButton.Cancel
#             | QDialogButtonBox.StandardButton.Ok
#         )
#         dialogLayout.addWidget(buttons)
#         self.setLayout(dialogLayout)

# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     window=Window()
#     window.show()
#     sys.exit(app.exec())        

#Radio-Button
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
)

class Example(QWidget):

    def __init__(self):
      super().__init__(parent=None)
      self.__initUi__()

    def initUI(self):
      vbox=QVBoxLayout()
      hbox=QHBoxLayout()

      rb1=QRadioButton("Large:",self)
      rb1.toggled.connect(self.updateLabel)

      rb2=QRadioButton("Medium:",self)
      rb2.toggled.connect(self.updateLabel)

      rb3=QRadioButton("Small:",self)
      rb3.toggled.connect(self.updateLabel)

      self.label=QLabel(" ",self)

      hbox.addWidget(rb1)
      hbox.addWidget(rb2)
      hbox.addWidget(rb3)

      vbox.addSpacing(16)
      vbox.addLayout(vbox)
      vbox.addWidget(self.label)

      self.setLayout(hbox)
      self.Geometry(500,300,250,200)
      self.setWindowTitle("QRadio-Button App")
      self.show()

def updateLabel(self):
    rbtn=self.sender()
    if rbtn.isChecked()==True:
        self.label.setText(rbtn.Text()) 
def main():
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec())
if __name__=="__main__":
   main()               


