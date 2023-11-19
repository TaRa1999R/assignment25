
import sqlite3

class Database () :

    def __init__ (self) :
        self.con = sqlite3.connect ("alarm.db")
        self.cur = self.con.cursor ()


    def get_alarms (self) :
        query = f"SELECT * FROM alarm"
        result = self.cur.execute (query)
        tasks = result.fetchall ()
        return (tasks)

    
    def add_alarm (self , time , title) :
        query = f"INSERT INTO alarm (time, title) VALUES ('{time}','{title}')"
        result = self.cur.execute (query)
        self.con.commit ()

    
    def delete_alarm (self) :
        ...

    
    def update_alarm (self) :
        ...