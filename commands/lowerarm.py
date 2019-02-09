from wpilib.command import Command

class LowerArm(Command):
    '''
    Command for lowering the arm
    '''

    def __init__(self):
        super().__init__("LowerArm")

        self.requires(self.getRobot().singlemotor)

    def execute(self):
        self.getRobot().singlemotor.setsinglemotor(-1)