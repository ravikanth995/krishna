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

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout,
    QDialogButtonBox,
    QLineEdit,
    QDialog,
    QFormLayout,
    QWidget
)

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        # window1=QWidget()
        self.setWindowTitle("Government Data Info.in")
        # window1.setGeometry(100,100,250,80)
        dialogLayout=QVBoxLayout()
        formLayout=QFormLayout()
        formLayout.addRow("Email:",QLineEdit())
        formLayout.addRow("PassWord:",QLineEdit())
        dialogLayout.addLayout(formLayout)
        buttons=QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)
if __name__=="__main__":
    app=QApplication([])
    window=Window()
    # window1.show()
    sys.exit(app.exec())
