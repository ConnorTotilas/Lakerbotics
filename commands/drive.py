from wpilib.command import TimedCommand
from wpilib.drive import MecanumDrive


class Drive(TimedCommand):
    '''
    Drive command that can be used for autonomous.
    '''
    def __init__(self, magnitude, angle, zrotation, timeoutInSeconds):
        super().__init__("Drive", timeoutInSeconds)

        self.requires(self.getRobot().drive)
        self.magnitude = magnitude
        self.angle = angle
        self.zrotation = zrotation

    def initialize(self):
        self.getRobot().drive.drivePolar(self.magnitude, self.angle, self.zrotation)

    def end(self):
        self.getRobot().drive.drivePolar(0, 0, 0)