from wpilib.command import TimedCommand
from wpilib.drive import MecanumDrive


class Drive(TimedCommand):
    '''
    Drive command that can be used for autonomous.
    '''
    def __init__(self, yspeed, xspeed, zrotation, gyroangle, timeoutInSeconds):
        super().__init__("Drive", timeoutInSeconds)

        self.requires(self.getRobot().drive)
        self.yspeed = yspeed
        self.xspeed = xspeed
        self.zrotation = zrotation
        self.gyroangle = gyroangle

    def initialize(self):
        self.getRobot().drive.speed(self.yspeed, self.xspeed, self.zrotation, self.gyroangle)

    def end(self):
        self.getRobot().drive.speed(0, 0, 0, 0)