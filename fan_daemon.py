import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

FAN = 13    #o

GPIO.setup(FAN, GPIO.OUT)

FILE_PREFIX = "/tmp/led"

if __name__ == '__main__':
    while True:
        GPIO.output(FAN, GPIO.LOW)
        f = open("/tmp/led4", "w")
        f.write("%s" % "0000FF")
        f.close()        
        time.sleep(15)
        GPIO.output(FAN, GPIO.HIGH)
        f = open("/tmp/led4", "w")
        f.write("%s" % "00FF00")
        f.close()        
        time.sleep(15)
