
from PySide6.QtCore import QThread

class Thread_Timer ( QThread ) :
    def __init__ ( self ) :
        super().__init__()
    
    def run ( self ) :
        ...

    def reset ( self ) :
        ...