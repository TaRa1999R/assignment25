
import time
from PySide6.QtCore import QThread , Signal
from clock import Time

class Thread_Timer ( QThread ) :
    timer_signal = Signal (Time)

    def __init__ ( self , hour , minute , second ) :
        super().__init__()
        self.hour = hour
        self.minute = minute
        self.second = second
        self.time = Time (self.hour , self.minute , self.second)
    
    def run ( self ) :
        while True :
            self.time.minus ()
            self.timer_signal.emit (self.time)
            time.sleep (1)

    def reset ( self ) :
        ...