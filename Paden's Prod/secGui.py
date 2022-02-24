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
        self.setGeometry(100, 100, 350, 200)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
  
        # creating a push button
        button = QPushButton("MicOn", self)
        button2 = QPushButton("MicOff", self)
        button3 = QPushButton("CamOn", self)
        button4 = QPushButton("CamOff", self)
  
        # setting geometry of button
        button.setGeometry(100, 150, 100, 30)
        button2.setGeometry(200, 150, 100, 30)
        button3.setGeometry(100, 100, 100, 30)
        button4.setGeometry(200, 100, 100, 30)
  
        # adding action to a button
        button.clicked.connect(self.clickme)
        button2.clicked.connect(self.clickme2)
        button3.clicked.connect(self.clickme3)
        button4.clicked.connect(self.clickme4)
  
    # action method
    def clickme(self):
  
        # Mic off action
        os.system("mic_On.bat")

    def clickme2(self):
        
        os.system("mic_Off.bat")

    def clickme3(self):

        os.system("cam_On.bat")

    def clickme4(self):
       
        os.system("cam_Off.bat")
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())