
from PySide6.QtCore import QThread

class Thread_Alarm ( QThread ) :
    def __init__ ( self ) :
        super().__init__()

    def run ( self ) :
        ...