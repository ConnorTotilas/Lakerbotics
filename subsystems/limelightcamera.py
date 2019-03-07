import wpilib
from wpilib.command.subsystem import Subsystem
from commnads.findtarget import FindTarget

class LimelightCamera(Subsystem):
    '''
    Subsystem to setup camera and run tracking command
    '''

    def __init__(self):
        super().__init__("Limelight")

    def initDefaultCommand(self):
        self.setDefaultCommand(FindTarget())