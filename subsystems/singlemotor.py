import wpilib
from wpilib.command.subsystem import Subsystem


class SingleMotor(Subsystem):
    """
    This example subsystem controls a single Talon in PercentVBus mode.
    """

    def __init__(self):
        """Instantiates the motor object."""

        super().__init__("SingleMotor")

        self.motor = wpilib.PWMVictorSPX(5)

    def setSpeed(self, speed):
        self.motor.set(speed)

    """def initDefaultCommand(self):
        self.setDefaultCommand()
    """