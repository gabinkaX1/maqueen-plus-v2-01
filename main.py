distance = 0
DFRobotMaqueenPlusV2.init()

def on_forever():
    global distance
    distance = DFRobotMaqueenPlusV2.read_ultrasonic(DigitalPin.P13, DigitalPin.P14)
    if distance < 30 and distance != 0:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_LEFT_MOTOR, MyEnumDir.E_FORWARD, 0)
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_RIGHT_MOTOR, MyEnumDir.E_FORWARD, 0)
        basic.pause(1000)
    else:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_ALL_MOTOR, MyEnumDir.E_FORWARD, 0)
basic.forever(on_forever)