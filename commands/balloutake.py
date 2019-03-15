from wpilib.command import Command

class BallOutake(Command):
    '''
    Command for ball outake
    '''

    def __init__(self):
        super().__init__("BallOutake")

        self.requires(self.getRobot().doublemotor)

    def execute(self):
        self.getRobot().doublemotor.setdoublemotor(-0.3)

    def end(self):
        self.getRobot().doublemotor.setdoublemotor(0)