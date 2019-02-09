from wpilib.command import Command

class BallIntake(Command):
    '''
    Command for ball intake
    '''

    def __init__(self):
        super().__init__("BallIntake")

        self.requires(self.getRobot().doublemotor)

    def execute(self):
        self.getRobot().doublemotor.setdoublemotor(1)
    
        