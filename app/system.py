from app import app
import RPi.GPIO as GPIO
import picamera
import thread

OFF_LED_PIN = 12
ON_LED_PIN = 11
SENSOR_PIN = 7

running = False

def __init__():
    global GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(OFF_LED_PIN, GPIO.OUT)
    GPIO.setup(ON_LED_PIN, GPIO.OUT)
    GPIO.setup(SENSOR_PIN, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.output(OFF_LED_PIN, True)
    GPIO.output(ON_LED_PIN, False)
    sys.stdout("a")#
    sys.stdout.flush()#
    thread.start_new_thread(detectMotion, ())
    sys.stdout("b")#
    sys.stdout.flush()#

def detectMotion():
    sys.stdout("c")#
    sys.stdout.flush()#
    camera = picamera.PiCamera()
    sys.stdout("d")#
    sys.stdout.flush()#
    while True:
        sys.stdout("e")#
        sys.stdout.flush()#
        sys.stdout(GPIO.input(SENSOR_PIN))

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
