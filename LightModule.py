from NextionEdition import NextionApp, Writer
import gpio 
import RPi.GPIO as GPIO
from time import sleep

class LightController:
     
    _levels = [0,1,2]
    _lightChangedCallback = None
    

    def __init__(self, lightChangedCallback):        
        self._lightChangedCallback = lightChangedCallback 
        # GPIO.cleanup() 
        GPIO.setwarnings(False)     
        GPIO.setmode(GPIO.BCM)
        
        for i in range(3):
            level=LightLevel(i)
            # level.id = i
            self._levels[i] = level

    def SwitchLevel(self, levelId : int):
        result = self._levels[levelId].SwitchState()        
        self._lightChangedCallback(levelId, result)

class LightLevel:
    _id=0
    _pins = [17,27,22]

    _bisabled = True

    def __init__(self, id:int):        
        self._id = id
        GPIO.setup(self._pins[self._id], GPIO.OUT, initial=GPIO.HIGH)
        pass

    def SwitchState(self):
        if self._bisabled == True:
            self._bisabled = False
        else:
            self._bisabled = True        

        self.SwitchRele()
        return  self._bisabled  


    def SwitchRele(self):
        print(f'[{self}]: SwitchRele() _enabled: {self._bisabled}')
        GPIO.output(self._pins[self._id], self._bisabled)
        
if __name__ == "__main__":
    controller = LightController(None)
    while True:
        sleep(1)
        controller.SwitchLevel(0)
        sleep(1)
        controller.SwitchLevel(1)
        sleep(1)
        controller.SwitchLevel(2)