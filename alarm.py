
import time
from PySide6.QtCore import QThread, Signal
from clock import Time
from alarm_database import Database

class Thread_Alarm ( QThread ) :
    alarm_signal = Signal ()
    
    def __init__ ( self ) :
        super().__init__()

    def run ( self ) :
        ...