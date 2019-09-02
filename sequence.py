from time import sleep
import RPi.GPIO as GPIO

DIR = 20
STEP = 21
SLEEP = 26
CCW = 0
CW = 1
SPR = 200
PUMP = 7
VALVE = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

MODE = (14, 15, 18)
GPIO.setup(MODE, GPIO.OUT)

RESOLUTION = {
    '1/1': (0, 0, 0),
    '1/2': (1, 0, 0),
    '1/4': (0, 1, 0),
    '1/8': (1, 1, 0),
    '1/16': (0, 0, 1),
    '1/32': (1, 0, 1),
}


GPIO.output(MODE, RESOLUTION['1/8'])

step_count = SPR * 8 * 8
delay = (0.005 / 8)/10

try:
    while True:
        GPIO.output(SLEEP, GPIO.LOW)
        GPIO.output(DIR, CW)
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

        sleep(.5)

        GPIO.output(DIR, CCW)
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)


# End program cleanly with keyboard
except KeyboardInterrupt:
    print "  Quit"

    # Reset GPIO settings
    GPIO.cleanup()
    GPIO.output(SLEEP, GPIO.HIGH)

