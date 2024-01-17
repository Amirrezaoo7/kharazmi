import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import showwindow

app = QApplication(sys.argv)

class App(QWidget):
    def __init__(self): 
        super().__init__()
        #add windows
        self.ShowWindow = showwindow.ShowApp()
        # app options
        self.setWindowTitle("سامانه مدیریت دانش آموز")
        self.setFixedSize(600, 400)
        self.setWindowIcon(QIcon("Logo.png"))
        self.setStyleSheet("background-color: #222;")
        # make layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.setSpacing(40)
        hbox.setSpacing(80)
        # add image
        image = QPixmap("../images/about-us-2-512.png")
        # make widgets
        lab1 = QLabel("سامانه مدیریت دانش آموز")
        lab1.setFont(QFont("MRT_Ramollah", 50))
        lab1.setStyleSheet("color: #FFFFFF;")

        self.registerbtn = QPushButton("ثبت دانش آموز")
        self.registerbtn.setStyleSheet("""
            background-color: #484848;
            border: 2px solid #FFFFFF;
            border-radius: 10px;
        """)
        self.registerbtn.setMinimumHeight(50)

        self.showbtn = QPushButton("نمایش دانش آموز")
        self.showbtn.setStyleSheet("""
            background-color: #484848;
            border: 2px solid #FFFFFF;
            border-radius: 10px;
        """)
        self.showbtn.setMinimumHeight(50)

        self.aboutbtn = QPushButton("درباره ما")
        self.aboutbtn.setFixedSize(100, 100)
        self.aboutbtn.setStyleSheet("""
            background-color: #484848;
            border: 2px solid #FFFFFF;
            border-radius: 100px;
        """)
        self.aboutbtn.setIcon(QIcon("../images/about-us-2-512.png"))
        self.aboutbtn.setIconSize(QSize(64, 64))
        # set layout
        vbox.addWidget(lab1)
        vbox.addWidget(self.aboutbtn)
        vbox.addLayout(hbox)
        hbox.addWidget(self.registerbtn)
        hbox.addWidget(self.showbtn)
        self.setLayout(vbox)
        # add action to buttons
        self.registerbtn.clicked.connect(self.onclick_register)
        self.showbtn.clicked.connect(self.onclick_show)
    def onclick_register(self):
        pass

    def onclick_show(self):
        self.ShowWindow.show()
        self.hide()

win = App()
win.show()
sys.exit(app.exec())