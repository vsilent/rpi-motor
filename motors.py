from time import sleep
import RPi.GPIO as GPIO

"""

Stepper motor 28BYJ-48 driver

"""

class StepperMotor28BYJ(object):
    pins = None
    CLOCKWISE = 1          # rotate clockwise
    ANTICLOCKWISE  = -1    # rotate counterclockwise
    DELAY = 0.01           # delay between steps for test

    def __init__(self, pins, **kwargs):
        self.pins = pins
        self.state = 3
        GPIO.setmode(GPIO.BOARD)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            pass

    def __del__( self ):
        """reset pins"""
        GPIO.cleanup()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """reset pins"""
        GPIO.cleanup()

    def step(self, direction, delay):
        """docstring for step_clockwise"""
        steps = (
            [0,0,0,1],
            [0,0,1,1],
            [0,0,1,0],
            [0,1,1,0],
            [0,1,0,0],
            [1,1,0,0],
            [1,0,0,0],
            [1,0,0,1]
        )

        if direction == self.CLOCKWISE:
            for byte in steps:
                #print('Send %s' % byte)

                i = 0
                for pin in self.pins:
                    GPIO.output(pin, byte[i])
                    i += 1
                sleep(delay)

        if direction == self.ANTICLOCKWISE:

            for byte in steps[::-1]:
                #print('Send %s' % byte)

                i = 0
                for pin in self.pins:
                    GPIO.output(pin, byte[i])
                    i += 1
                sleep(delay)


with StepperMotor28BYJ(pins=(11, 13, 15, 16)) as motor:
    print ('Clockwise')
    for i in range (240):
        motor.step(StepperMotor28BYJ.CLOCKWISE, 0.0009)

    print ('Anticlockwise')
    for i in range (240):
        motor.step(StepperMotor28BYJ.ANTICLOCKWISE, .0009)
