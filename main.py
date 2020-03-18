import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_ui import Ui_Dialog
import os

class Ui(Ui_Dialog):
    def setup(self, Dialog):
        self.pushButton.clicked.connect(self.buttonClick)
        self.addButton.clicked.connect(self.buttonAddClick)
        self.delButton.clicked.connect(self.buttonDelClick)

    def buttonClick(self):
        text = self.textEdit.toPlainText()

        if self.to_channel.isChecked():
            mension ='<!channel> \n ' 
        elif self.to_here.isChecked():
            mension='<!here> \n'
        elif self.to_none :
            mension = ''
        data = {
          'text' : mension + text
        }

        payload =  json.dumps(data)
        config_file ='configs/url_list.txt'

        for line in open(config_file, 'r').readlines():
            sp = line.split(',')
            desc = sp[0].strip()
            url = sp[1].strip()
            ret = requests.post(url, payload)
            if ret.success:
                print('send success {}'.format(desc))
    
    def buttonAddClick(self):
        print('add button click')

    def buttonDelClick(self):
        print('del button click')
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui()
    ui.setupUi(Dialog)
    ui.setup(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
