from wpilib.command import TimedCommand

class AutoBallIntake(TimedCommand):
    '''
    ball intake command that can be used for autonomous.
    '''
    def __init__(self, motorspeed, timeoutInSeconds):
        super().__init__("AutoBallIntake", timeoutInSeconds)

        self.requires(self.getRobot().doublemotor)
        self.motorspeed = motorspeed

    def initialize(self):
        self.getRobot().doublemotor.setdoublemotor(self.motorspeed)

    def end(self):
        self.getRobot().doublemotor.setdoublemotor(0)