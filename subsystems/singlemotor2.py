import wpilib
from wpilib.command.subsystem import Subsystem

class SingleMotor2(Subsystem):
    """
    This example subsystem controls two Victors in PercentVBus mode.
    """

    def __init__(self):
        """Instantiates the motor object."""

        super().__init__("SingleMotor2")

        self.motor = wpilib.PWMVictorSPX(7)

    def setsinglemotor2(self, speed):
        self.motor.set(speed)