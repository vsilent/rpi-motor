from time import sleep
import RPi.GPIO as GPIO


class StepperMotor(object):
    pins = None
    CLOCKWISE = 1          # rotate clockwise
    ANTICLOCKWISE  = -1    # rotate counterclockwise
    DELAY = 0.01           # delay between steps for test

    def __init__(self, pins, **kwargs):
        self.pins = pins
        self.state = 1
        GPIO.setmode(GPIO.BOARD)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

    def __del__( self ):
        GPIO.cleanup()
        print('pins reset')

    def step(self, direction, delay):
        """docstring for step_clockwise"""
        if direction == self.CLOCKWISE:
            for i in range (4):
                byte = self.state << i
                print('send %d' % byte)
                pin0 = byte & 1 > 0
                pin1 = byte & 2 > 0
                pin2 = byte & 4 > 0
                pin3 = byte & 8 > 0
                print('Send %s' % byte)
                print(pin0, pin1, pin2, pin3)
                GPIO.output(self.pins[0], pin0)
                GPIO.output(self.pins[1], pin1)
                GPIO.output(self.pins[2], pin2)
                GPIO.output(self.pins[3], pin3)
                sleep(delay)

        elif direction == self.ANTICLOCKWISE:
            state = 8
            for i in range (4):
                byte = state >> i
                pin0 = byte & 8 > 0
                pin1 = byte & 4 > 0
                pin2 = byte & 2 > 0
                pin3 = byte & 1 > 0
                print('Send %s' % byte)
                print(pin0, pin1, pin2, pin3)
                GPIO.output(self.pins[0], pin0)
                GPIO.output(self.pins[1], pin1)
                GPIO.output(self.pins[2], pin2)
                GPIO.output(self.pins[3], pin3)
                sleep(delay)

motor1 = StepperMotor(pins=(3, 5, 7, 8))
print ('Clockwise')
for i in range (2):
    motor1.step(StepperMotor.CLOCKWISE, .05)
for i in range (2):
    print ('Anticlockwise')
    motor1.step(StepperMotor.ANTICLOCKWISE, .05)

