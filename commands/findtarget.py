from wpilib.command import Command
from networktables import NetworkTables

class FindTarget(Command):
    """
    Reads inputs from camera to determine if there is a valid target
    """

    def __init__(self):
        super().__init__("FindTarget")

        self.requires(self.getRobot().drive)

    def execute(self):
        table = NetworkTables.getTable("limelight")
        ty = table.getNumber('ty', 0)
        

        drive_K = 0.26
        drive_MAX = 0.7

        KpDistance = -0.1
        distance_error = ty

        driving_adjust = KpDistance * distance_error

        drive_cmd = driving_adjust * drive_K

        if drive_cmd > drive_MAX:
            drive_cmd = drive_MAX
        
        self.getRobot().drive.speed(
            0, drive_cmd*-1, 0, 0
        )


