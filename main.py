import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_ui import Ui_Dialog
import os

class Ui(Ui_Dialog):
    def setup(self, Dialog):
        self.pushButton.clicked.connect(self.buttonClick)

    def buttonClick(self):
        text = self.textEdit.toPlainText()
        print(text)
        endpoint = os.getenv('HOOK')

        data = {
          'text' : '<!channel> \n ' + text
        }

        payload =  json.dumps(data)

        requests.post(endpoint, payload)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui()
    ui.setupUi(Dialog)
    ui.setup(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
