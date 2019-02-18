import wpilib
from wpilib.command.subsystem import Subsystem


class LimelightCamera(Subsystem):
    '''
    Subsystem to setup camera and run tracking command
    '''

    def __init__(self):
        super().__init__("Limelight")

        self.Max_Drive = 0.7

    def initDefaultCommand(self):
        self.setDefaultCommand()