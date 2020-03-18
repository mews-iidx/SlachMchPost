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

        self.hooks_dict = {}
        self.list_file = 'configs/url_list.txt'

        self.readHookList()

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
        self.hooks_dict.items()
        for name, url in self.hooks_dict.items():
            try:
                ret = requests.post(url, payload)
                if ret.status_code == 200:
                    print('send success {}'.format(name))
                else:
                    ret = QtWidgets.QMessageBox.warning(None, "警告", "{} のwebhook URLが多分間違えています！！ \n 続ける？".format(name), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )
                    if ret == QtWidgets.QMessageBox.No:
                        return
            except :
                ret = QtWidgets.QMessageBox.warning(None, "警告", "{} のwebhook URLが多分間違えています！！ \n 続ける？".format(name), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )
                if ret == QtWidgets.QMessageBox.No:
                    return
        self.writeHookList()
############
    
    def buttonAddClick(self):
        hook_name = self.hookName.text()
        hook_url = self.hookUrl.text()
        if not hook_name or not hook_url:
            ret = QtWidgets.QMessageBox.warning(None, "警告", "送信先名とWebhookを入力してから押してください！！")
            return 

        self.hookList.addItem(hook_name)
        self.hooks_dict[hook_name] = hook_url

    def buttonDelClick(self):
        selected_item = self.hookList.selectedItems()
        cur_item = self.hookList.currentItem()
        if cur_item:
            cur_row = self.hookList.currentRow()
            self.hookList.takeItem(cur_row)
            del self.hooks_dict[cur_item.text()]

    def getHookList(self):
        items = self.hookList.items()
        return items
    
    def readHookList(self):
        fp = open(self.list_file, 'r')
        lines = fp.readlines()
        fp.close()

        for line in lines:
            if line == '\n':
                print('config file error')
                ret = QtWidgets.QMessageBox.warning(None, "警告", "configs/url_list.txt の書式が間違ってます！空行が入ってませんか！？")
                quit()
            sp = line.split(',')
            hook_desc = sp[0].strip()
            hook_url = sp[1].strip()
            self.hooks_dict[hook_desc] = hook_url

        for k, v in self.hooks_dict.items():
            self.hookList.addItem(k)

    def writeHookList(self):
        fp = open(self.list_file, 'w')
        for k, v in self.hooks_dict.items():
            s = str(k) + ',' + str(v) + '\n'
            fp.write(s)
        fp.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui()
    ui.setupUi(Dialog)
    ui.setup(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
