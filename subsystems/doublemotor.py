import wpilib
from wpilib.command.subsystem import Subsystem

class DoubleMotor(Subsystem):
    """
    This example subsystem controls two Victors in PercentVBus mode.
    """

    def __init__(self):
        """Instantiates the motor object."""

        super().__init__("DoubleMotor")

        self.motor = wpilib.PWMVictorSPX(4)
        self.motor2 = wpilib.PWMVictorSPX(5)

    def setdoublemotor(self, speed):
        self.motor.set(speed)
        self.motor2.set(speed)

    