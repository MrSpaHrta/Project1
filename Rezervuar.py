from time import sleep
import RPi.GPIO as GPIO
import gpio
import asyncio

# print(RPi.GPIO.VERSION)
# print(dir(RPi.GPIO))
gerconMaxPin = 16
gerconMinPin = 16
pumpPin = 26

class ReservuarController:
    def Init(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
    
        GPIO.setup(pumpPin, GPIO.OUT, initial=GPIO.HIGH)    

    async def Loop(self):
        pass

    async def OnGerconStateChanged(self, state: bool):
        pass

class Gercon:

    _stateChangrdCallback = None
    _pin = 0
    def __init__(self, pin:int, stateChangedCallback: bool):
        self._stateChangedCallback = stateChangedCallback
        self._pin = pin
        GPIO.setup(self._pin, GPIO.IN, pullup=GPIO.PUD_DOWN)
    
    def Step(self):
        try:
            state = GPIO.input(self._pin)
            print(state)
            self._stateChangedCallback(state)
        except KeyboardInterrupt:
            GPIO.cleanup()   


class Pump:
    def __init__(self):
        pass

    def StartPump(active:bool):
        try:
            if active:
                print(f"SetPump({active})") 
                GPIO.output(pumpPin, GPIO.LOW)
            else:
                GPIO.output(pumpPin, GPIO.HIGH) 
                print(f"SetPump({active})")
        
        except KeyboardInterrupt:
            GPIO.cleanup()

    def StopPump(self):
        pass 

if __name__ == "__main__":
    print("main")
