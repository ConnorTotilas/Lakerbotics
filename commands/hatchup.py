from wpilib.command import Command

class HatchUp(Command):
    '''
    Command to lift hatch arm
    '''

    def __init__(self):
        super().__init__("HatchUp")

        self.requires(self.getRobot().singlemotor2)

    def execute(self):
        self.getRobot().singlemotor2.setsinglemotor2(0.5)

    def end(self):
        self.getRobot().singlemotor2.setsinglemotor2(0)