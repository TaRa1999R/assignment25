
import time
from PySide6.QtCore import QThread, Signal
from alarm_database import Database

class Thread_Alarm ( QThread ) :
    alarm_signal = Signal (str)

    def __init__ ( self ) :
        super().__init__()
        self.database_alarm = Database ()

    def run ( self ) :
        while True :
            on_alarms = []
            alarms_list = self.database_alarm.get_alarms ()
            for alarm in alarms_list :
                if alarm[3] == 0 :
                    alarm_time = alarm[1].split (":")
                    on_alarms.append ({"id" : alarm[0] , "hour" : alarm_time[0] , "minute" : alarm_time[1] , "title" : alarm[2]})

            now = time.localtime ()
            for alarm in on_alarms :
                if alarm["hour"] == now.tm_hour and alarm["minute"] == now.tm_min :
                    txt = f"{alarm['hour']}:{alarm['minute']}\n{alarm['title']}"
                    self.alarm_signal.emit (txt)
                    self.database_alarm.update_alarm (alarm['id'] , 1)