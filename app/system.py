import RPi.GPIO as GPIO
import picamera
import datetime

OFF_LED_PIN = 12
ON_LED_PIN = 11
SENSOR_PIN = 7

camera = picamera.PiCamera()

running = False

def __init__():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(OFF_LED_PIN, GPIO.OUT)
    GPIO.setup(ON_LED_PIN, GPIO.OUT)
    GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.output(OFF_LED_PIN, True)
    GPIO.output(ON_LED_PIN, False)
    camera.capture(datetime.datetime.now().strftime("%Y%m%d%H%M%S.jpg"))
    detectMotion()

def detectMotion():
    while True:
        print(GPIO.input(sensor))

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
