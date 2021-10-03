import sys
from PyQt6.QtWidgets import QApplication,QWidget, QHBoxLayout, QVBoxLayout, QListWidget
from PyQt6.QtCore import Qt
from PyQt6 import uic
from lib.generator import pass_generator as pg

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("lib/ui/gui.ui", self)
        self.setWindowTitle('Password Generator')
        self.create_button.clicked.connect(self.create_pass)
        self.list_load(pg.site_list())
        self.copy_button.clicked.connect(self.copy_pass)
        self.delete_button.clicked.connect(self.delete_pass)



    def list_load(self,items_list):
        self.output_list.clear()
        for count,item in enumerate(items_list):
            self.output_list.insertItem(count, str(item))

    def create_pass(self):
        site= self.create_input.text()
        pg.create_pass(site)
        self.list_load(pg.site_list())
        self.create_input.clear()

    def copy_pass(self):
        site=self.output_list.currentItem()
        site=str(site.text())
        pg.copy_pass(site)

    def delete_pass(self):
        site=self.output_list.currentItem()
        site=str(site.text())
        pg.delete_pass(site)
        self.list_load(pg.site_list())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Myapp()
    widget.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
