
import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import Signal
from notifypy import Notify
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

        #stop watch property
        self.stop_watch = Thread_Stop_watch ()
        self.ui.stop_startbutton.clicked.connect (self.start_stopwatch)
        self.stop_watch.stop_watch_signal.connect (self.show_stopwatch)
        self.ui.stop_stopbutton.clicked.connect (self.stop_stopwatch)
        self.ui.stop_resetbutton.clicked.connect (self.reset_stopwatch)

        #timer property
        self.timer = Thread_Timer ()
        self.ui.timer_startbutton.clicked.connect (self.start_timer)
        self.timer.timer_signal.connect (self.show_timer)
        self.ui.timer_stopbutton.clicked.connect (self.stop_timer)
        self.ui.timer_resetbutton.clicked.connect (self.reset_timer)

        #world clock property
        self.world_clock = Thread_Wold_clock ()
        self.world_clock.start ()
        self.world_clock.world_clock_signal.connect (self.show_worldclock)
    
    #stop_watch_methods
    def start_stopwatch (self) :
        self.stop_watch.start ()
    
    def stop_stopwatch (self) :
        self.stop_watch.terminate ()
    
    def reset_stopwatch (self) :
        self.stop_watch.reset ()
        self.ui.stop_show.setText (f"00 : 00 : 00")
    
    def show_stopwatch (self , time) :
        self.ui.stop_show.setText (f"{time.hour} : {time.minute} : {time.second}")

    #timer_methods
    def start_timer (self) :
        self.timer_hour = int (self.ui.timer_hour.text())
        self.timer_minute = int (self.ui.timer_minute.text())
        self.timer_second = int (self.ui.timer_second.text())
        self.timer.set_time (self.timer_hour , self.timer_minute , self.timer_second)
        self.timer.start ()

    def stop_timer (self) :
        self.timer.terminate ()

    def reset_timer (self) :
        self.timer.reset ()
        self.ui.timer_hour.setText ("00")
        self.ui.timer_minute.setText ("15")
        self.ui.timer_second.setText ("30")
    
    def show_timer (self , time) :
        self.ui.timer_hour.setText (str (time.hour))
        self.ui.timer_minute.setText (str (time.minute))
        self.ui.timer_second.setText (str (time.second))
        self.timer_check (time.hour , time.minute , time.second)
    
    def timer_check (self , h , min , sec) : 
        if h == min == sec == 0 :
            notif = Notify ()
            notif.title = "Tmer ⏳"
            notif.message = "Timer Done"
            notif.audio = "timer.wav"
            notif.send ()
            self.stop_timer ()
            self.ui.timer_hour.setText (str (self.timer_hour))
            self.ui.timer_minute.setText (str (self.timer_minute))
            self.ui.timer_second.setText (str (self.timer_second))
            
    #world clock methods
    def show_worldclock (self , time , country) :
        if country == "iran" :
            self.ui.world_iran.setText (f"{time.hour} : {time.minute} : {time.second}")
        
        elif country == "usa" :
            self.ui.world_USA.setText (f"{time.hour} : {time.minute} : {time.second}")
        
        elif country == "canada" :
            self.ui.world_canad.setText (f"{time.hour} : {time.minute} : {time.second}")
        
        elif country == "germany" :
            self.ui.world_germany.setText (f"{time.hour} : {time.minute} : {time.second}")
    
    #alarm methods
    def show_alarms (self) :
        ...
    

if __name__ == "__main__" :
    app = QApplication (sys.argv)
    window = Mainwindow ()
    window.show ()
    app.exec ()

