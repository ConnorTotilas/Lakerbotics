from wpilib.command import Command

class ThrottleMixer(Command):
    """
    Reads the input from the joystick to control
    the motors for Mecanum Drive.
    """

    def __init__(self):
        super().__init__("ThrottleMixer")

        self.requires(self.getRobot().drive)

    def execute(self):
        self.getRobot().drive.speed(
            self.getRobot().joystick.getX(), self.getRobot().joystick.getY(), self.getRobot().joystick.getZ(), 0
        )