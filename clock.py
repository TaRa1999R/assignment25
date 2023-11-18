
import time

class Time () :
    def __init__ ( self , hour , min , sec ) :
        self.hour = hour
        self.minute = min
        self.second = sec


    def plus ( self ) :
        self.second += 1

        if self.second == 60 :
            self.second = 0
            self.minute += 1
        
        if self.minute == 60 :
            self.minute = 0
            self.hour += 1
            

    def minus ( self ) :
        ...