import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
count = 0
count1 = 0
count2 = 0
count3 = 0

try:
    while True:
        SW1value = GPIO.input(SW1)
        if SW1value == True:
            count = count+1
            time.sleep(0.1)
            print("('SW1 click',", count,")")
        time.sleep(0.1)
        SW2value = GPIO.input(SW2)
        if SW2value == True:
            count1 = count1+1
            time.sleep(0.1)
            print("('SW2 click',", count1,")")
        time.sleep(0.1)
        SW3value = GPIO.input(SW3)
        if SW3value == True:
            count2 = count2+1
            time.sleep(0.1)
            print("('SW3 click',", count2,")")
        time.sleep(0.1)
        SW4value = GPIO.input(SW4)
        if SW4value == True:
            count3 = count3+1
            time.sleep(0.1)
            print("('SW4 click',", count3,")")
        time.sleep(0.1)
except KeyboardInterrupt:
    pass    
GPIO.cleanup()