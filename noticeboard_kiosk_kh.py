from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
import os
from os.path import isfile, join, dirname

fsize = 20
fsize2 = 40
ftype = 'Calibri'
buttoncol = 'background-color : #444444; color: white'
buttoncoldir = 'background-color : #996100; color: white'
buttoncolcong = 'background-color : #462652; color: white'

def file_info(num):
    fo = open('data.jwnb')
    f = fo.read()
    fo.close
    f = f.replace('\n',',').split(',')
    st = f[num]
    d1 = st.find('|')
    d2 = st.find('|',d1+1)
    return st[d1+1:d2]

homepage = file_info(0)
jwnews = file_info(1)
congnum = file_info(2)
cong1 = file_info(3).upper()
cong1url = file_info(4)
cong2 = file_info(5).upper()
cong2url = file_info(6)
cong2 = file_info(7).upper()
cong2url = file_info(8)


class MyWebBrowser(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)
        
        self.window = QWidget()
        self.window.setWindowTitle("JW Notice Board")
        self.window.setWindowIcon(QIcon('jwnb_logo.ico'))
        self.window.showFullScreen()
        
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        
        self.home_btn = QPushButton("HOME")
        self.home_btn.setMinimumHeight(150)
        self.home_btn.setFont(QFont(ftype,fsize))
        self.home_btn.setStyleSheet(buttoncol)
        
        self.cong1 = QPushButton(cong1)
        self.cong1.setMinimumHeight(150)
        self.cong1.setFont(QFont(ftype,fsize))
        self.cong1.setStyleSheet(buttoncolcong)
        
        if int(congnum) > 1:
            self.cong2 = QPushButton(cong2)
            self.cong2.setMinimumHeight(150)
            self.cong2.setFont(QFont(ftype,fsize))
            self.cong2.setStyleSheet(buttoncolcong)
        
        if int(congnum) > 2:
            self.cong3 = QPushButton(cong1)
            self.cong3.setMinimumHeight(150)
            self.cong3.setFont(QFont(ftype,fsize))
            self.cong3.setStyleSheet(buttoncolcong)
        
        self.btn3 = QPushButton("NEWS")
        self.btn3.setMinimumHeight(150)
        self.btn3.setFont(QFont(ftype,fsize))
        self.btn3.setStyleSheet(buttoncol)
        
        self.wol = QPushButton("WOL")
        self.wol.setMinimumHeight(150)
        self.wol.setFont(QFont(ftype,fsize))
        self.wol.setStyleSheet(buttoncol)
        
        self.back_btn = QPushButton("←")
        self.back_btn.setMinimumHeight(150)
        self.back_btn.setFont(QFont(ftype,fsize2))
        self.back_btn.setStyleSheet(buttoncoldir)
        
        self.forward_btn = QPushButton("→")
        self.forward_btn.setMinimumHeight(150)
        self.forward_btn.setFont(QFont(ftype,fsize2))
        self.forward_btn.setStyleSheet(buttoncoldir)
        
        self.horizontal.addWidget(self.home_btn)
        self.horizontal.addWidget(self.btn3)
        self.horizontal.addWidget(self.wol)
        self.horizontal.addWidget(self.cong1)
        if int(congnum) > 1:
            self.horizontal.addWidget(self.cong2)
        if int(congnum) > 2:
            self.horizontal.addWidget(self.cong3)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        
        
        self.browser = QWebEngineView()
        
        
        self.home_btn.clicked.connect(lambda: self.navigate(homepage))
        self.btn3.clicked.connect(lambda: self.navigate(jwnews))
        self.wol.clicked.connect(lambda: self.navigate('https://wol.jw.org'))
        self.cong1.clicked.connect(lambda: self.navigate(cong1url))
        if int(congnum) > 1:
            self.cong2.clicked.connect(lambda: self.navigate(cong2url))
        if int(congnum) > 2:
            self.cong3.clicked.connect(lambda: self.navigate(cong3url))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        self.navigate(homepage)
        
        self.window.setLayout(self.layout)
        self.window.show()
    
    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))
        
    def loadPage(self):
        self.browser.load(QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'\homepage\index.html'))
        
app = QApplication([])
window = MyWebBrowser()
app.exec_()

        
