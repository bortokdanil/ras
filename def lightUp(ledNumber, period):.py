import RPi.GPIO as GPIO
import time
a = [24, 25, 8, 7, 12, 16, 20, 21]
GPIO.setmode(GPIO.BCM)
GPIO.setup(a, GPIO.OUT)


for i in range(len(a)):
    GPIO.output(a[i], 0)
time.sleep(1)
def lightUp(ledNumber, period):
     GPIO.output(a[ledNumber], 1)
     time.sleep(period)
     GPIO.output(a[ledNumber], 0)
def lightDown(ledNumber, period):
    GPIO.output(a[ledNumber], 0)
    time.sleep(period)
    GPIO.output(a[ledNumber], 1)
def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
def blink2(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)
def blink3(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        lightDown(ledNumber, blinkPeriod)
def runningLight(count, period):
    for j in range(count):
        for i in range(len(a)):
            blink2(i, 1, period)
def runningDark(count, period):
    GPIO.output(a, 1)
    for j in range(count):
        for i in range(len(a)):
            blink3(i, 1, period)
    GPIO.output(a, 0)
def decToBinList(decNumber):
    a = bin(decNumber)
    b = a[2:]
    b = list(b)
    for i in range(len(b)):
        b[i] = int(b[i])
    while len(b) < 8:
        b.insert(0,0)
    return b
def lidhtNumber(number):
    u = decToBinList(number)
    for i in range(len(u)):
        if u[i] == 1:
            GPIO.output(a[7 - i], 1)
def runningPattern(pattern, direction):
    u = decToBinList(pattern)
    print(u)
    for i in range(len(u)):
                if u[i] == 1:
                    GPIO.output(a[7 - i], 1)
    if direction == 0:
        while True:
            for i in range(len(u)):
                if u[i] == 1:
                    GPIO.output(a[7 - i], 1)
            time.sleep(0.1)
            m = u[7]
            u = u[:7]
            print(u)
            u.insert(0, m)
            for i in range(len(a)):
                GPIO.output(a[i], 0)
    if direction == 1:
        while True:
            for i in range(len(u)):
                if u[i] == 1:
                    GPIO.output(a[7 - i], 1)
            time.sleep(0.1)
            m = u[0]
            u = u[1:]
            u.append(m)
            for i in range(len(a)):
                GPIO.output(a[i], 0)
runningPattern(7, 1)
