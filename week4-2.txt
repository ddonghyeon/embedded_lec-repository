import RPi.GPIO as GPIO         #사용할 모듈 지정
import time			            #delay를 위한 시간 모듈
import random
GPIO.setmode(GPIO.BOARD)        #핀모드 설정
GPIO.setup(37, GPIO.OUT)	    #led 1번 지정
GPIO.setup(36, GPIO.OUT)        #led 2번 지정
GPIO.setup(40, GPIO.OUT)        #led 3번 지정
GPIO.setup(38, GPIO.OUT)        #led 4번 지정


for i in range(10):             #10번 반복
    arrs = [37,36,40,38]        #핀번호 배열
    list = random.choice(arrs)  #led핀 중 하나 선택
    GPIO.output(list,True)      #led on
    time.sleep(0.25)            #0.25초 유지
    GPIO.output(list,False)     #led off
    time.sleep(0.25)            #0.25초 유지