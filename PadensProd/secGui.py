from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Simple Security ")

        # setting geometry
        self.setGeometry(700, 300, 400, 350)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # creating a push button
        button = QPushButton("Microphone On", self)
        button2 = QPushButton("Microphone Off", self)
        button3 = QPushButton("Camera On", self)
        button4 = QPushButton("Camera Off", self)
        button5 = QPushButton("Printer fix", self)
        button6 = QPushButton("Last resort printer fix", self)

        # setting geometry of button
        button.setGeometry(70, 150, 100, 30)
        button2.setGeometry(200, 150, 100, 30)
        button3.setGeometry(70, 100, 100, 30)
        button4.setGeometry(200, 100, 100, 30)
        button5.setGeometry(70, 200, 250, 30)
        button6.setGeometry(70, 250, 250, 30)

        # adding action to a button
        button.clicked.connect(self.clickme)
        button2.clicked.connect(self.clickme2)
        button3.clicked.connect(self.clickme3)
        button4.clicked.connect(self.clickme4)
        button5.clicked.connect(self.clickme5)
        button6.clicked.connect(self.clickme6)


    # action method
    def clickme(self):

        # Mic off action
        os.system("secAcc\mic_On.bat")
        os.system("certifywithsuccess.bat")

    def clickme2(self):

        os.system("secAcc\mic_Off.bat")
        os.system("certifywithsuccess.bat")

    def clickme3(self):

        os.system("secAcc\cam_On.bat")
        os.system("certifywithsuccess.bat")

    def clickme4(self):

        os.system("secAcc\cam_Off.bat")
        os.system("certifywithsuccess.bat")

    def clickme5(self):

        os.system("tools\printerFix.bat")
        os.system("certifywithsuccess.bat")

    def clickme6(self):

        os.system("tools\printerFixDel.bat")
        os.system("certifywithsuccess.bat")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
