from wpilib.command import TimedCommand
from wpilib.drive import MecanumDrive
import robot

class Drive(TimedCommand):

    def __init__(self, magnitude, angle, zrotation):
        super().__init__("Drive Forward")

        self.requires(self.getRobot().drive)
        self.magnitude = magnitude
        self.angle = angle
        self.zrotation = zrotation

    def initialize(self):
        self.getRobot().drive.drivePolar(self.magnitude, self.angle, self.zrotation)

    def end(self):
        self.getRobot().drive.drivePolar(0, 0, 0)