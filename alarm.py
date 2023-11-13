
from PySide6.QtCore import QThread

class Alarm ( QThread ) :
    def __init__ ( self ) :
        super().__init__()

    def run ( self ) :
        ...