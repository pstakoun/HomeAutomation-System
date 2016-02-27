import RPi.GPIO as GPIO

OFF_LED_PIN = 12
ON_LED_PIN = 11
SENSOR_PIN = -1
CAMERA_PIN = -1

running = False

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(OFF_LED_PIN, GPIO.OUT)
    GPIO.setup(ON_LED_PIN, GPIO.OUT)
    #GPIO.setup(SENSOR_PIN, GPIO.IN)
    #GPIO.setup(CAMERA_PIN, GPIO.IN)
    GPIO.output(OFF_LED_PIN, True)
    GPIO.output(ON_LED_PIN, False)

def start():
    global running
    running = True
    GPIO.output(OFF_LED_PIN, False)
    GPIO.output(ON_LED_PIN, True)

def stop():
    global running
    running = False
    GPIO.output(OFF_LED_PIN, True)
    GPIO.output(ON_LED_PIN, False)

def isRunning():
    return running
