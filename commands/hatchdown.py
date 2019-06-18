from wpilib.command import Command

class HatchDown(Command):
    '''
    Command to lower hatch arm
    '''

    def __init__(self):
        super().__init__("HatchDown")

        self.requires(self.getRobot().singlemotor2)

    def execute(self):
        self.getRobot().singlemotor2.setsinglemotor2(-0.5)

    def end(self):
        self.getRobot().singlemotor2.setsinglemotor2(0)