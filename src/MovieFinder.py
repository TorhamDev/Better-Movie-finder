import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt6.QtGui import QFont, QFontDatabase
from MainWindow.MainWindowUI import Ui_Form
from spiders.download_links import DownloadLinksSpider  # type: ignore
from spiders.search import SearchSpider


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        font_id = QFontDatabase.addApplicationFont("./fonts/Vazir.ttf")
        if font_id < 0: print("Error")
        font = QFontDatabase.applicationFontFamilies(font_id)
        print(font)
        self.lineEdit.setFont(QFont(font[0], 11))
        self.list_widget.setFont(QFont(font[0], 10))
        self.output.setFont(QFont(font[0], 10))
        self.lineEdit.returnPressed.connect(self.search_signal)
        self.search_btn.clicked.connect(self.search_signal)
        self.list_widget.clicked.connect(self.select_movie)
        self.clear_btn.clicked.connect(self.clear)










    def search_signal(self):
        if self.lineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', 'You didn\'t type anything !',
                                QMessageBox.StandardButton.Ok)
        else :
                spider = SearchSpider()
                self.search_results = spider.search(query=self.lineEdit.text())
                items = [k for k, v in self.search_results.items()]
                self.list_widget.clear()
                self.output.clear()
                self.list_widget.addItems(items)
        

    def select_movie(self):
        name = self.list_widget.currentItem().text()
        text = 'Movie Links :\n\n'
        spider = DownloadLinksSpider(self.search_results[name])
        results = spider.get_download_links()
        for quality, link in results:
            text += f"{quality} :\n{link}\n----------------\n"
        self.output.setText(text)

    def clear(self):
        self.lineEdit.clear()
        self.list_widget.clear()
        self.output.clear()
        self.search_results = {}













if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    sys.exit(app.exec())