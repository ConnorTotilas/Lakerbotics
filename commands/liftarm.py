from wpilib.command import Command

class LiftArm(Command):
    '''
    Command for lifting the arm
    '''

    def __init__(self):
        super().__init__("LiftArm")

        self.requires(self.getRobot().singlemotor)

    def execute(self):
        self.getRobot().singlemotor.setsinglemotor(0.3)

    def end(self):
        self.getRobot().singlemotor.setsinglemotor(0)