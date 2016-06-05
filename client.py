from PyQt4 import QtGui, QtCore, uic
import sys,json
from urllib import request,parse

form_class = uic.loadUiType("client.ui")[0]

class Window(form_class,QtGui.QMainWindow):
    def __init__(self,parent=False):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.get.clicked.connect(self.get_msg_func)
        self.send.clicked.connect(self.send_func)
    def get_msg_func(self):
        data = request.urlopen("http://localhost/message/jon").read().decode()
        data = json.loads(data)
        data = data["messages"]
        for i in data:
            QtGui.QMessageBox.information(self,"Messages",str(i))
    def send_func(self):
        to = self.to.text()
        From = self.From.text()
        msg = self.msg.text()
        data = {"to": to, "from": From, "msg": msg}
        data = bytes( parse.urlencode( data ).encode() )
        handler = request.urlopen("http://localhost/message/jon",data)
        print(handler.read().decode())
        
app = QtGui.QApplication(sys.argv)

window = Window(None)

window.show()

app.exec_()
