import wpilib
from wpilib.command.subsystem import Subsystem

class SingleMotor(Subsystem):
    """
    This example subsystem controls two Victors in PercentVBus mode.
    """

    def __init__(self):
        """Instantiates the motor object."""

        super().__init__("SingleMotor")

        self.motor = wpilib.VictorSP(6)

    def setsinglemotor(self, speed):
        self.motor.set(speed)
    