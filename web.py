from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

fsize = 20
ftype = 'Arial'
buttoncol = 'background-color : #444444; color: white'

file1 = open('data.jwnb', 'r')
file2 = file1.read()
file3 = file2.replace('\n',',').split(',')


class MyWebBrowser(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)
        
        self.window = QWidget()
        self.window.setWindowTitle("JW Notice Board")
        self.window.showFullScreen()
        
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        
        self.home_btn = QPushButton("HOME")
        self.home_btn.setMinimumHeight(150)
        self.home_btn.setFont(QFont(ftype,fsize))
        self.home_btn.setStyleSheet(buttoncol)
        
        self.cong1 = QPushButton(file3[3].upper())
        self.cong1.setMinimumHeight(150)
        self.cong1.setFont(QFont(ftype,fsize))
        self.cong1.setStyleSheet(buttoncol)
        
        if int(file3[2]) > 1:
            self.cong2 = QPushButton(file3[5].upper())
            self.cong2.setMinimumHeight(150)
            self.cong2.setFont(QFont(ftype,fsize))
            self.cong2.setStyleSheet(buttoncol)
        
        if int(file3[2]) > 2:
            self.cong3 = QPushButton(file3[7].upper())
            self.cong3.setMinimumHeight(150)
            self.cong3.setFont(QFont(ftype,fsize))
            self.cong3.setStyleSheet(buttoncol)
        
        self.btn3 = QPushButton("NEWS")
        self.btn3.setMinimumHeight(150)
        self.btn3.setFont(QFont(ftype,fsize))
        self.btn3.setStyleSheet(buttoncol)
        
        self.back_btn = QPushButton("←")
        self.back_btn.setMinimumHeight(150)
        self.back_btn.setFont(QFont(ftype,fsize))
        self.back_btn.setStyleSheet(buttoncol)
        
        self.forward_btn = QPushButton("→")
        self.forward_btn.setMinimumHeight(150)
        self.forward_btn.setFont(QFont(ftype,fsize))
        self.forward_btn.setStyleSheet(buttoncol)
        
        self.horizontal.addWidget(self.home_btn)
        self.horizontal.addWidget(self.cong1)
        if int(file3[2]) > 1:
            self.horizontal.addWidget(self.cong2)
        if int(file3[2]) > 2:
            self.horizontal.addWidget(self.cong3)
        self.horizontal.addWidget(self.btn3)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        
        self.browser = QWebEngineView()
        
        self.home_btn.clicked.connect(lambda: self.navigate(file3[0]))
        self.cong1.clicked.connect(lambda: self.navigate(file3[4]))
        if int(file3[2]) > 1:
            self.cong2.clicked.connect(lambda: self.navigate(file3[6]))
        if int(file3[2]) > 2:
            self.cong3.clicked.connect(lambda: self.navigate(file3[8]))
        
        self.btn3.clicked.connect(lambda: self.navigate(file3[1]))
        
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        self.browser.setUrl(QUrl(file3[0]))
        
        self.window.setLayout(self.layout)
        self.window.show()
    
    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))
        
        
app = QApplication([])
window = MyWebBrowser()
app.exec_()

        
