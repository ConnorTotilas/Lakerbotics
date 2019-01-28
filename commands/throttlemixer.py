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
            self.throttlemixerY()*-1, self.throttlemixerX(), self.throttlemixerZ(), 0
        )
    
    def throttlemixerX(self):
        XSpeed = self.getRobot().joystick.getX()
        if (XSpeed>1.0) or (XSpeed<-1.0):
            return XSpeed*1
        elif (XSpeed<=1.0) and (XSpeed>=-1.0):
            return XSpeed*1
        else:
            return XSpeed
    def throttlemixerY(self):
        YSpeed = self.getRobot().joystick.getY()
        if (YSpeed>1.0) or (YSpeed<-1.0):
            return YSpeed*1
        elif (YSpeed<=1.0) and (YSpeed>=-1.0):
            return YSpeed*1
        else:
            return YSpeed
    def throttlemixerZ(self):
        ZSpeed = self.getRobot().joystick.getZ()
        if (ZSpeed>1.0) or (ZSpeed<-1.0):
            return ZSpeed*1
        elif (ZSpeed<=1.0) and (ZSpeed>=-1.0):
            return ZSpeed*1
        else:
            return ZSpeed
        