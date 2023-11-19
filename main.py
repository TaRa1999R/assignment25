
import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import Signal
from notifypy import Notify
from world_clock import Thread_Wold_clock
from alarm import Thread_Alarm
from stop_watch import Thread_Stop_watch
from timer_section import Thread_Timer
from clock import Time
from alarm_database import Database
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

        #alarm property
        self.alarm = Thread_Alarm ()
        self.alarm.start ()
        self.alarm.alarm_signal.connect (self.alarm_ring)
        self.database = Database ()
        self.show_alarms ()
        self.ui.alarm_add.clicked.connect (self.add_alarm)
        for button in self.alarm_deletebutton :
            button["button"].clicked.connect (partial (self.delet_alarm , button["id"]))
        
        for box in self.alarm_checkbox :
            box["checkbox"].clicked.connect (partial (self.alarm_mode , box["id"] , box["mode"]))
    
    #stop watch methods
    def start_stopwatch (self) :
        self.stop_watch.start ()
    
    def stop_stopwatch (self) :
        self.stop_watch.terminate ()
    
    def reset_stopwatch (self) :
        self.stop_watch.reset ()
        self.ui.stop_show.setText (f"00 : 00 : 00")
    
    def show_stopwatch (self , time) :
        self.ui.stop_show.setText (f"{time.hour} : {time.minute} : {time.second}")

    #timer methods
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
        self.alarm_list = self.database.get_alarms ()
        self.alarm_checkbox = []
        self.alarm_deletebutton = []

        for i in range (len (self.alarm_list)) :
            new_checkbox = QCheckBox ()
            new_lable_time = QLabel ()
            new_lable_title = QLabel ()
            new_button = QPushButton ()
            self.alarm_checkbox.append ({"checkbox" : new_checkbox , "id" : self.alarm_list[i][0] , "mode" : self.alarm_list[i][3]})
            self.alarm_deletebutton.append ({"button" : new_button , "id" : self.alarm_list[i][0]})

            new_lable_time.setText (self.alarm_list[i][1] ) 
            new_lable_title.setText (self.alarm_list[i][2])
            new_button.setText ("🗑")
            new_checkbox.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
            new_lable_time.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
            new_lable_title.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
            new_button.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
            new_lable_time.setFont (QFont ("Seven Segment" , 28))
            new_lable_title.setFont (QFont ("Segoe UI" , 20))
            new_lable_time.setStyleSheet ("color: rgb(0, 255, 255)")
            new_lable_title.setStyleSheet ("color: rgb(0, 255, 127)")
            new_button.setStyleSheet ("background-color: rgb(255, 87, 118)")
            if self.alarm_list[i][3] == 0 :
                new_checkbox.setChecked (True)

            self.ui.alarm_grid.addWidget (new_checkbox , i , 0)
            self.ui.alarm_grid.addWidget (new_lable_time , i , 1)
            self.ui.alarm_grid.addWidget (new_lable_title , i , 2)
            self.ui.alarm_grid.addWidget (new_button , i , 3)


    def add_alarm (self) :
        new_title = self.ui.alarm_title.text ()
        new_h = self.ui.alaram_hour.text ()
        new_min = self.ui.alarm_minute.text ()
        new_time = f"{new_h} : {new_min}"
        if self.database.add_alarm (new_time , new_title) == False :
            txt = f"Please try again later"
            message = QMessageBox (windowTitle = "❌Error!!❌" , text = txt)
            message.exec_ ()
        
        else:
            self.ui.alaram_hour.setValue (0)
            self.ui.alarm_minute.setValue (0)
            self.ui.alarm_title.setText ("")
            self.show_alarms ()
    
    def delet_alarm (self, id) :
        if self.database.delete_alarm (id) == False :
            txt = f"Please try again later"
            message = QMessageBox (windowTitle = "❌Error!!❌" , text = txt)
            message.exec_ ()
        
        # else :
            # self.show_alarms ()
    
    def alarm_mode (self, id , pr_mode) :
        if pr_mode == 0 :
            if self.database.update_alarm (id , 1) == False :
                txt = f"Please try again later"
                message = QMessageBox (windowTitle = "❌Error!!❌" , text = txt)
                message.exec_ ()

        if pr_mode == 1 :
            if self.database.update_alarm (id , 0) == False :
                txt = f"Please try again later"
                message = QMessageBox (windowTitle = "❌Error!!❌" , text = txt)
                message.exec_ ()

    def alarm_ring (self , txt) :        
        notif = Notify ()
        notif.title = "Alarm ⏰"
        notif.message = txt
        notif.audio = "alarm.wav"
        notif.send ()

if __name__ == "__main__" :
    app = QApplication (sys.argv)
    window = Mainwindow ()
    window.show ()
    app.exec ()
