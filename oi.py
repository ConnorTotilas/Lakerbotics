from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton


def getJoystick():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    joystick = Joystick(0)

    trigger = JoystickButton(joystick, Joystick.ButtonType.kTrigger)

    return joystick