import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ALR0 = 5    #i
ALR0T = 6   #o
ALR1 = 24   #i
ALR2 = 25   #i
ALR0P = 12  #o

GPIO.setup(ALR0, GPIO.IN)
GPIO.setup(ALR1, GPIO.IN)
GPIO.setup(ALR2, GPIO.IN)
GPIO.setup(ALR0T, GPIO.OUT)
GPIO.setup(ALR0P, GPIO.OUT)

GPIO.output(ALR0P, GPIO.HIGH)
GPIO.output(ALR0T, GPIO.LOW)

if __name__ == '__main__':
    time.sleep(10)
    alr0_old = -1
    alr1_old = -1
    alr2_old = -1
    while True:
        GPIO.output(ALR0T, GPIO.HIGH)
        alr1 = GPIO.input(ALR1)
        alr2 = GPIO.input(ALR2)
    
        if alr1 != alr1_old:
            alr1_old = alr1
            led_str = ["00FF00", "FF0000"][alr1]
            f = open("/tmp/led1", "w")
            f.write("%s" % led_str)
            f.close()

        if alr2 != alr2_old:
            alr2_old = alr2
            led_str = ["00FF00", "FF0000"][alr2]
            f = open("/tmp/led2", "w")
            f.write("%s" % led_str)
            f.close()

        alr0_on = GPIO.input(ALR0)
        time.sleep(0.05)
        GPIO.output(ALR0T, GPIO.LOW)
        alr0_off = GPIO.input(ALR0)
        alr0 = 0
        if alr0_on == 1 and alr0_off == 1:
            alr0 = 1
        else:
            alr0 = 2

        if alr0 != alr0_old:
            alr0_old = alr0
            led_str = ["00FF00", "FF0000", "0000FF"][alr0]
            f = open("/tmp/led3", "w")
            f.write("%s" % led_str)
            f.close()

        time.sleep(0.2)
