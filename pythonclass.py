from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button1")

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
