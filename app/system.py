import RPi.GPIO as GPIO

ON_LED_PIN = -1
OFF_LED_PIN = -1
SENSOR_PIN = -1
CAMERA_PIN = -1

running = False

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ON_LED_PIN, GPIO.OUT)
    GPIO.setup(OFF_LED_PIN, GPIO.OUT)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    GPIO.setup(CAMERA_PIN, GPIO.IN)
    GPIO.output(ON_LED_PIN, False)
    GPIO.output(OFF_LED_PIN, True)

def start():
    running = True
    GPIO.output(ON_LED_PIN, True)
    GPIO.output(OFF_LED_PIN, False)

def stop():
    running = False
    GPIO.output(OFF_LED_PIN, True)
    GPIO.output(ON_LED_PIN, False)

def isRunning():
    return running
