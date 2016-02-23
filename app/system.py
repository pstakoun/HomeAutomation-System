import RPi.GPIO as GPIO

LED_PIN = 7

running = False

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, False)

def start():
    running = True
    GPIO.output(LED_PIN, True)

def stop():
    running = False
    GPIO.output(LED_PIN, False)

def isRunning():
    return running
