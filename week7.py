import threading
import serial
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
PWMA = 18 #왼쪽모터 핀번호
PWMB = 23 #오른쪽모터 핀번호
AIN1 = 22 #왼쪽 앞모터 핀번호
AIN2 = 27 #왼쪽 뒤모터 핀번호
BIN1 = 25 #오른쪽 앞모터 핀번호
BIN2 = 24 #오른쪽 뒤모터 핀번호
GPIO.setup(PWMA,GPIO.OUT) #왼쪽 모터 속도 output
GPIO.setup(PWMB,GPIO.OUT) #오른쪽 모터 속도 output
GPIO.setup(AIN1,GPIO.OUT) #왼쪽 앞모터 output
GPIO.setup(AIN2,GPIO.OUT) #왼쪽 뒤모터 output
GPIO.setup(BIN1,GPIO.OUT) #오른쪽 앞모터 output
GPIO.setup(BIN2,GPIO.OUT) #오른쪽 뒤모터 output
L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout = 1.0)
gData = ""
def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data
def main():
    global gData
    try:
        while True:
            if gData.find("go") >= 0: #문자열에서 go를 찾으면 0을 반환하고 그렇지 않으면 -1
                gData = ""
                GPIO.output(AIN1,0)  #앞으로 이동
                GPIO.output(AIN2,1)
                GPIO.output(BIN1,0)
                GPIO.output(BIN2,1)
                L_Motor.ChangeDutyCycle(100)
                R_Motor.ChangeDutyCycle(100)
                print("ok go") #문자열 출력
                time.sleep(0.1)
            elif gData.find("back") >= 0: #문자열에서 back를 찾으면 0을 반환하고 그렇지 않으면 -1
                gData = ""
                GPIO.output(AIN1,1) #뒤로 이동
                GPIO.output(AIN2,0)
                GPIO.output(BIN1,1)
                GPIO.output(BIN2,0)
                L_Motor.ChangeDutyCycle(100)
                R_Motor.ChangeDutyCycle(100)
                print("ok back")
                time.sleep(0.1)
            elif gData.find("left") >= 0: #문자열에서 left를 찾으면 0을 반환하고 그렇지 않으면 -1
                gData = ""
                GPIO.output(AIN1,1) #왼쪽으로 회전
                GPIO.output(AIN2,0)
                GPIO.output(BIN1,0)
                GPIO.output(BIN2,1)
                L_Motor.ChangeDutyCycle(100)
                R_Motor.ChangeDutyCycle(100)
                print("ok left") #문자열 출력
                time.sleep(0.1)
            elif gData.find("right") >= 0: #문자열에서 right를 찾으면 0을 반환하고 그렇지 않으면 -1
                gData = ""
                GPIO.output(AIN1,0) #오른쪽으로 회전
                GPIO.output(AIN2,1)
                GPIO.output(BIN1,1)
                GPIO.output(BIN2,0)
                L_Motor.ChangeDutyCycle(100)
                R_Motor.ChangeDutyCycle(100)
                print("ok right") #문자열 출력
                time.sleep(0.1)
            elif gData.find("stop") >= 0: #문자열에서 stop를 찾으면 0을 반환하고 그렇지 않으면 -1
                gData = ""
                L_Motor.ChangeDutyCycle(0) #멈춤
                R_Motor.ChangeDutyCycle(0)
                print("ok stop") #문자열 출력
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
if __name__== '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()