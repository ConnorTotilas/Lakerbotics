from wpilib.command.commandgroup import CommandGroup
from wpilib.drive import MecanumDrive
from wpilib.command.waitcommand import WaitCommand
from robot import MyRobot


class AutonomousProgram(CommandGroup):
    """
    A simple program that spins the motor for two seconds, pauses for a second,
    and then spins it in the opposite direction for two seconds.
    """

    def __init__(self):
        super().__init__("Autonomous Program")

        self.addSequential(RobotDrive.drivePolar(1.0, 0, 0.0))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(RobotDrive.drivePolar(1.0, 0, 0.0))