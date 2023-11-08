import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

PWR1 = 27   #i

GPIO.setup(PWR1, GPIO.IN)

if __name__ == '__main__':
    time.sleep(5)
    pwr1_old = -1
    while True:
        pwr1 = GPIO.input(PWR1)
    
        if pwr1 != pwr1_old:
            pwr1_old = pwr1
            led_str = "00000000000000000000FF00"
            if pwr1 == 1:
                led_str = "0000000000000000000000FF"
            f = open("/tmp/led0", "w")
            f.write("%s" % led_str)
            f.close()
        time.sleep(0.25)
