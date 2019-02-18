from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from commands.ballintake import BallIntake
from commands.balloutake import BallOutake
from commands.liftarm import LiftArm
from commands.lowerarm import LowerArm

def getJoystick():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    joystick = Joystick(0)

    button5 = JoystickButton(joystick, 5)
    button6 = JoystickButton(joystick, 6)
    button3 = JoystickButton(joystick, 3)
    button4 = JoystickButton(joystick, 4)

    button5.whileHeld(BallIntake())
    button6.whileHeld(BallOutake())
    button3.whileHeld(LiftArm())
    button4.whileHeld(LowerArm())

    return joystick