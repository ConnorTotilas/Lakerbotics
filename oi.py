from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from commands.ballintake import BallIntake
from commands.balloutake import BallOutake
from commands.liftarm import LiftArm
from commands.lowerarm import LowerArm
from commands.hatchup import HatchUp
from commands.hatchdown import HatchDown

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
    button1 = JoystickButton(joystick, 1)
    button2 = JoystickButton(joystick, 2)

    button5.whileHeld(BallIntake())
    button6.whileHeld(BallOutake())
    button3.whileHeld(LiftArm())
    button4.whileHeld(LowerArm())
    button1.whileHeld(HatchUp())
    button2.whileHeld(HatchDown())

    return joystick