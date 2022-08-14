from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
import sys
from random import choice

window_titles = ['>///<', 'Stop Clicking', 'So Handsy... >.<', 'Reeee']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.n_times_clicked = 0
        
        self.setWindowTitle("Ac_Cheat1")
        self.button = QPushButton("Please press me uwu")
        self.button.clicked.connect(self.button_clicked)
        self.windowTitleChanged.connect(self.window_title_change)
        
        self.setCentralWidget(self.button)
        
    def button_clicked(self):
        self.button.setText("You already clicked me >..<")
        new_window_title = choice(window_titles)
        print("Setting current title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)
    
    def window_title_change(self, window_title):
        print("Omg you made the window title change to %s" % window_title)
        
        if window_title == 'Reeee' :
            self.button.setDisabled(True)
            self.button.setText("Aw Shucks!")




app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.show()
app.exec()