from time import sleep
import RPi.GPIO as GPIO
import gpio
import asyncio


# print(RPi.GPIO.VERSION)
# print(dir(RPi.GPIO))
gerconMaxPin = 16
gerconMinPin = 16
pumpPin = 23

class ReservuarController:

    _pump = None
    _gerconMax = None
    _alarmMax = False
    _alarmMin = False


    def __init__(self, debug:bool):
        # GPIO.cleanup()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        # GPIO.setup(pumpPin, GPIO.OUT, initial=GPIO.HIGH)    
        self._pump = Pump(pumpPin)
        self._gerconMax = Gercon(gerconMaxPin, self._OnGerconMaxStateChanged)
        
        loop = asyncio.get_event_loop()
        LoopTask = loop.create_task(self._Loop())
        asyncio.ensure_future(LoopTask) 
        
        if(debug):
            loop.run_forever()


    async def _Loop(self):
        while True:
            await asyncio.sleep(3)
            self._gerconMax.Step()

            alarm = self._alarmMin or self._alarmMax
            if(alarm):            
                # TODO disable pump, invoke Error callBack
                pass
            else:
                self._pump.SetPumpState(self._IsTimeToWater())

    def _IsTimeToWater(self):
        # TODO получить значение у сущности, которая следит за режимом полива
        pass       
            

    def _OnGerconMaxStateChanged(self, state: bool):
        self._alarmMax = state        
    
    def _OnGerconMinStateChanged(self, state: bool):
        self._alarmMin = state


class Gercon:

    _stateChangedCallback = None
    _pin = 0

    def __init__(self, pin:int, stateChangedCallback):
        self._stateChangedCallback = stateChangedCallback
        self._pin = pin
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # gpio.setup(self._pin, gpio.IN, pullup=gpio.PUD)
    
    def Step(self):
        try:
            state = GPIO.input(self._pin)
            print(state)
            self._stateChangedCallback(state)
        except KeyboardInterrupt:
            GPIO.cleanup()   


class Pump:

    _pin = 0
    _isActive = False
    def __init__(self, pin:int):
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH) 
        self._pin = pin

    def SetPumpState(self, active:bool):
        self._isActive = active
        try:
            if active:
                print(f"SetPump({active})") 
                GPIO.output(self._pin, GPIO.LOW)
            else:
                GPIO.output(self._pin, GPIO.HIGH) 
                print(f"SetPump({active})")
        
        except KeyboardInterrupt:
            GPIO.cleanup()

    def GetPumpState(self):
        return self._isActive

if __name__ == "__main__":
    print("main")
    controller = ReservuarController(True)
    
