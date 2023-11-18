
import time
from PySide6.QtCore import QThread, Signal
from clock import Time

class Thread_Stop_watch ( QThread ) :
    stop_watch_signal = Signal (Time)

    def __init__ ( self ) :
        super().__init__()
        self.time = Time (0 , 0 , 0)

    def run ( self ) :
        while True :
            self.time.plus ()
            self.stop_watch_signal.emit (self.time)
            time.sleep (1)
    
    def reset ( self ) :
        self.time = Time (0 , 0 , 0)