from wpilib.command import TimedCommand

class AutoLiftArm(TimedCommand):
    '''
    lift arm command that can be used for autonomous.
    '''
    def __init__(self, motorspeed, timeoutInSeconds):
        super().__init__("AutoLiftArm", timeoutInSeconds)

        self.requires(self.getRobot().singlemotor)
        self.motorspeed = motorspeed

    def initialize(self):
        self.getRobot().singlemotor.setsinglemotor(self.motorspeed)

    def end(self):
        self.getRobot().singlemotor.setsinglemotor(0)