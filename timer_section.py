
from PySide6.QtCore import QThread

class Timer ( QThread ) :
    def __init__ ( self ) :
        super().__init__()
    
    def run ( self ) :
        ...

    def reset ( self ) :
        ...