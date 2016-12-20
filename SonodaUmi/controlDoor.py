import RPi.GPIO as GPIO
import time

def initdoor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)


def opendoor(interval):
    GPIO.output(24, True)
    time.sleep(interval)
    GPIO.output(24, False)


def opendoor():
    GPIO.output(24, True)


def closedoor():
    GPIO.output(24, False)


def cleandoor():
    GPIO.cleanup()