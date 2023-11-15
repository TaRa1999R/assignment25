
import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import Signal
from world_clock import Wold_clock
from alarm import Alarm
from stop_watch import Stop_watch
from timer_section import Timer
from clock import Time
from design_ui import Ui_MainWindow

class Mainwindow ( QMainWindow ) :
    
    def __init__ ( self ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)


if __name__ == "__main__" :
    app = QApplication (sys.argv)
    window = Mainwindow ()
    window.show ()
    app.exec ()

