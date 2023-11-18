
import time
from PySide6.QtCore import QThread , Signal
from clock import Time

class Thread_Timer ( QThread ) :
    timer_signal = Signal (Time)

    def __init__ ( self ) :
        super().__init__()

    def set_time ( self , hour , minute , second ) :
        self.time = Time (hour , minute , second)
    
    def run ( self ) :
        while True :
            self.time.minus ()
            self.timer_signal.emit (self.time)
            time.sleep (1)

    def reset ( self ) :
        ...