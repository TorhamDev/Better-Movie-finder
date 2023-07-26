import sys
from PyQt6.QtWidgets import QWidget, QApplication
from MainWindow.MainWindowUI import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()













if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    sys.exit(app.exec())