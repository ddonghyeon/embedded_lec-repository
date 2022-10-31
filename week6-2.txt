import RPi.GPIO as GPIO
import time
BUZZER = 12
SW1 = 5 
SW2 = 6 
SW3 = 13 
SW4 = 19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN)
GPIO.setup(SW2, GPIO.IN)
GPIO.setup(SW3, GPIO.IN)
GPIO.setup(SW4, GPIO.IN)
GPIO.setup(BUZZER,GPIO.OUT)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
p= GPIO.PWM(BUZZER, 261)
p.start(50)
time.sleep(0.5)
p.stop()
try:
    while True:
        SW1value = GPIO.input(SW1)
        if SW1value == True:
            p.start(50)
            p.ChangeFrequency(262)
            time.sleep(0.5)
            p.stop()
            time.sleep(0.5)
        SW2value = GPIO.input(SW2)
        if SW2value == True:
            p.start(50)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.stop()
            time.sleep(0.5)
        SW3value = GPIO.input(SW3)    
        if SW3value == True:
            p.start(50)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.stop()
            time.sleep(0.5)
        SW4value = GPIO.input(SW4)    
        if SW4value == True:
            p.start(50)
            p.ChangeFrequency(392)
            time.sleep(0.5)
            p.stop()
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()