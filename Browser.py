import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class Browser(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.showMaximized()

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl('https://google.com'))

        self.menu = QToolBar()
        self.addToolBar(self.menu)

        ReloadBtn = QAction('Reload', self)
        ReloadBtn.triggered.connect(self.browser.reload)
        self.menu.addAction(ReloadBtn)

        BackBtn = QAction('Back', self)
        BackBtn.triggered.connect(self.browser.back)
        self.menu.addAction(BackBtn)

        NextBtn = QAction('Next', self)
        NextBtn.triggered.connect(self.browser.forward)
        self.menu.addAction(NextBtn)

        HomeBtn = QAction('Home', self)
        HomeBtn.triggered.connect(self.HomeURL)
        self.menu.addAction(HomeBtn)

        self.URLTxt = QLineEdit()
        self.URLTxt.returnPressed.connect(self.NavigateURL)
        self.menu.addWidget(self.URLTxt)

        self.browser.urlChanged.connect(self.UpdateURL)

    def HomeURL(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def NavigateURL(self):
        self.browser.setUrl(QUrl(self.URLTxt.text()))

    def UpdateURL(self, u):
        self.URLTxt.setText(u.toString())


WebApp = QApplication(sys.argv)
QApplication.setApplicationName("Browser")
obj = Browser()

WebApp.exec_()
