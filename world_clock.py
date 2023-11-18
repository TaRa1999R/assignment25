
import time
from PySide6.QtCore import QThread, Signal
from clock import Time

class Thread_Wold_clock ( QThread ) :
    world_clock_signal = Signal (Time , str)

    def __init__ ( self ) :
        super().__init__()
        
    def run ( self ) :
            while True :
                gmt_time = time.gmtime ()
                self.time_iran =  Time (gmt_time.tm_hour, gmt_time.tm_min , gmt_time.tm_sec)
                self.time_iran.add (3 , 30 , 0)
                self.world_clock_signal.emit (self.time_iran , "iran")

                self.time_usa =  Time (gmt_time.tm_hour, gmt_time.tm_min , gmt_time.tm_sec)
                self.time_usa.sub (5 , 0 , 0)
                self.world_clock_signal.emit (self.time_usa , "usa")

                self.time_germany =  Time (gmt_time.tm_hour, gmt_time.tm_min , gmt_time.tm_sec)
                self.time_germany.add (1 , 0 , 0)
                self.world_clock_signal.emit (self.time_germany , "germany")                

                self.time_canada =  Time (gmt_time.tm_hour, gmt_time.tm_min , gmt_time.tm_sec)
                self.time_canada.sub (5 , 0 , 0)
                self.world_clock_signal.emit (self.time_canada , "canada")