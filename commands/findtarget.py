from wpilib.command import Command
from networktables import NetworkTables

class FindTarget(Command):
    """
    Reads inputs from camera to determine if there is a valid target
    """

    def __init__(self):
        super().__init__("FindTarget")

    def execute(self):
        
        table = NetworkTables.getTable("limelight")
        tx = table.getNumber('tx',None)
        ty = table.getNumber('ty',None)
        ta = table.getNumber('ta',None)
        ts = table.getNumber('ts',None)