import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.drive import MecanumDrive
from commands.throttlemixer import ThrottleMixer

class Mecanum(Subsystem):
    """
    Subsystem to control the motors for MecanumDrive
    """

    def __init__(self):
        super().__init__("Mecanum")

        # motors and the channels they are connected to

        self.frontLeftMotor = wpilib.VictorSP(1)
        self.rearLeftMotor = wpilib.VictorSP(2)
        self.frontRightMotor = wpilib.VictorSP(3)
        self.rearRightMotor = wpilib.VictorSP(4)

        # invert the left side motors
        self.frontLeftMotor.setInverted(True)

        # you may need to change or remove this to match your robot
        self.rearLeftMotor.setInverted(True)

        self.drive = MecanumDrive(
            self.frontLeftMotor,
            self.rearLeftMotor,
            self.frontRightMotor,
            self.rearRightMotor,
        )

        self.drive.setExpiration(0.1)

    def speed(self, xaxis, yaxis, zaxis, gyro):
        self.drive.driveCartesian(yaxis, xaxis, zaxis, gyro)
    
    def initDefaultCommand(self):
        self.setDefaultCommand(ThrottleMixer())