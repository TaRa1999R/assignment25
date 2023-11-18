
import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import Signal
from world_clock import Thread_Wold_clock
from alarm import Thread_Alarm
from stop_watch import Thread_Stop_watch
from timer_section import Thread_Timer
from clock import Time
from design_ui import Ui_MainWindow

class Mainwindow ( QMainWindow ) :
    
    def __init__ ( self ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)

        #stop_watch_property
        self.stop_watch = Thread_Stop_watch ()
        self.ui.stop_startbutton.clicked.connect (self.start_stopwatch)
        self.stop_watch.stop_watch_signal.connect (self.show_stopwatch)
        self.ui.stop_stopbutton.clicked.connect (self.stop_stopwatch)
        self.ui.stop_resetbutton.clicked.connect (self.reset_stopwatch)
    
    #stop_watch_methods
    def start_stopwatch (self) :
        self.stop_watch.start ()
    
    def stop_stopwatch (self) :
        ...
    
    def reset_stopwatch (self) :
        ...
    
    def show_stopwatch (self , time) :
        self.ui.stop_show.setText (f"{time.hour} : {time.minute} : {time.second}")


if __name__ == "__main__" :
    app = QApplication (sys.argv)
    window = Mainwindow ()
    window.show ()
    app.exec ()

