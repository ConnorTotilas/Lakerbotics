from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
from commands.drive import Drive
from commands.autoliftarm import AutoLiftArm


class AutonomousProgram(CommandGroup):
    """
    A simple program that spins the motor for two seconds, pauses for a second,
    and then spins it in the opposite direction for two seconds.
    """

    def __init__(self):
        super().__init__("Autonomous Program")

        self.addSequential(Drive(yspeed=0.3, xspeed=0, zrotation=0, gyroangle=0, timeoutInSeconds=1))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(AutoLiftArm(motorspeed=0.6, timeoutInSeconds=1))
