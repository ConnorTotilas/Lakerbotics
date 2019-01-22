import wpilib
from wpilib.command import Command
from commandbased import CommandBasedRobot
from wpilib.drive import MecanumDrive
from subsystems import singlemotor
import oi
from commands.autonomous import AutonomousProgram


class MyRobot(CommandBasedRobot):
    """
    The CommandBasedRobot base class implements almost everything you need for
    a working robot program. All you need to do is set up the subsystems and
    commands. You do not need to override the "periodic" functions, as they
    will automatically call the scheduler. You may override the "init" functions
    if you want to do anything special when the mode changes.
    """
    # Channels on the roboRIO that the motor controllers are plugged in to
    frontLeftChannel = 2
    rearLeftChannel = 3
    frontRightChannel = 1
    rearRightChannel = 0

    # The channel on the driver station that the joystick is connected to
    joystickChannel = 0

    def robotInit(self):
        """
        This is a good place to set up your subsystems and anything else that
        you will need to access later.
        """
        """Robot initialization function"""
        self.frontLeftMotor = wpilib.VictorSP(self.frontLeftChannel)
        self.rearLeftMotor = wpilib.VictorSP(self.rearLeftChannel)
        self.frontRightMotor = wpilib.VictorSP(self.frontRightChannel)
        self.rearRightMotor = wpilib.VictorSP(self.rearRightChannel)

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

        self.stick = wpilib.Joystick(self.joystickChannel)


        Command.getRobot = lambda x=0: self
        self.motor = singlemotor.SingleMotor()

        self.autonomousProgram = AutonomousProgram()

        """
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        """
        self.joystick = oi.getJoystick()

    def autonomousInit(self):
        """
        You should call start on your autonomous program here. You can
        instantiate the program here if you like, or in robotInit as in this
        example. You can also use a SendableChooser to have the autonomous
        program chosen from the SmartDashboard.
        """

        self.autonomousProgram.start()

    def operatorControl(self):
        """Runs the motors with Mecanum drive."""

        self.drive.setSafetyEnabled(True)
        while self.isOperatorControl() and self.isEnabled():
            # Use the joystick X axis for lateral movement, Y axis for forward movement, and Z axis for rotation.
            # This sample does not use field-oriented drive, so the gyro input is set to zero.
            self.drive.driveCartesian(
                self.stick.getX(), self.stick.getY(), self.stick.getZ(), 0
            )

            wpilib.Timer.delay(0.005)  # wait 5ms to avoid hogging CPU cycles



if __name__ == "__main__":
    wpilib.run(MyRobot)


    #Also need to add in throttle mixers. And make sure mecanum drive code mixes with command code