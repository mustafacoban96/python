from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from InterfaceOfApp import Ui_WifiPasswordApp
from CodeOfApp import WifiPassword


class WifiInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        #loadUi("UI_wifi.ui",self)

        self.ui = Ui_WifiPasswordApp()
        self.ui.setupUi(self)
        self.obj = WifiPassword()

    
    def my_slot(self):
        self.ui.wifiIsimSifre.setText(self.obj.main())




app = QApplication([])

window =WifiInterface()

window.show()
app.exec_()

