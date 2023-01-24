from time import sleep
import RPi.GPIO as GPIO

# print(RPi.GPIO.VERSION)
# print(dir(RPi.GPIO))
gerconMaxPin = 16
gerconMinPin = 16
pumpPin = 26

def Init():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
  
    GPIO.setup(pumpPin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(gerconMinPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gerconMaxPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def Gercon():
    try:
        while True:
            sleep(0.1)
            if GPIO .input(gerconMinPin) == True:
                print("False")
                SetPump(True)
            else:
                print("True")
                SetPump(False)
    except KeyboardInterrupt:
        GPIO.cleanup()

def SetPump(active:bool):
    try:
        if active:
            print(f"SetPump({active})") 
            GPIO.output(pumpPin, GPIO.LOW)
        else:
            GPIO.output(pumpPin, GPIO.HIGH) 
            print(f"SetPump({active})")
    
    except KeyboardInterrupt:
        GPIO.cleanup() 

if __name__ == "__main__":
    print("main")
    Init()
    Gercon()
