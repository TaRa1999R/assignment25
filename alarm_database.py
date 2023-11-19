
import sqlite3

class Database () :

    def __init__ (self) :
        self.con = sqlite3.connect ("alarm.db")
        self.cur = self.con.cursor ()


    def get_alarms (self) :
        ...

    
    def add_alarm (self) :
        ...

    
    def delete_alarm (self) :
        ...
    
