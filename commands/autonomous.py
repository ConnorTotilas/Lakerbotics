from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
from commands.drive import Drive


class AutonomousProgram(CommandGroup):
    """
    A simple program that spins the motor for two seconds, pauses for a second,
    and then spins it in the opposite direction for two seconds.
    """

    def __init__(self):
        super().__init__("Autonomous Program")

        self.addSequential(Drive(1.0, 0, 0, timeoutInSeconds=2))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(Drive(-1.0, 0, 0, timeoutInSeconds=2)) 