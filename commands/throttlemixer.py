from wpilib.command import Command

class ThrottleMixer(Command):
    """
    Reads the input from the joystick to control
    the motors for Mecanum Drive.
    """

    def __init__(self):
        super().__init__("ThrottleMixer")

        self.requires(self.getRobot().drive)

    def execute(self):
        self.getRobot().drive.speed(
            self.throttlemixerX(), self.throttlemixerY()*-1, self.throttlemixerZ(), 0
        )

    def throttlemixerX(self):
        XSpeed = self.getRobot().joystick.getX()
        if (XSpeed>0.2) or (XSpeed<-0.2):
            return XSpeed*0.8
        elif (XSpeed<=0.2) and (XSpeed>=-0.2):
            return XSpeed*0
        else:
            return XSpeed
    def throttlemixerY(self):
        YSpeed = self.getRobot().joystick.getY()
        if (YSpeed>0.2) or (YSpeed<-0.2):
            return YSpeed*0.9
        elif (YSpeed<=0.2) and (YSpeed>=-0.2):
            return YSpeed*0
        else:
            return YSpeed
    def throttlemixerZ(self):
        ZSpeed = self.getRobot().joystick.getTwist()
        if (ZSpeed>0.2) or (ZSpeed<-0.2):
            return ZSpeed*0.7
        elif (ZSpeed<=0.2) and (ZSpeed>=-0.2):
            return ZSpeed*0
        else:
            return ZSpeed
