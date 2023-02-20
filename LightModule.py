from NextionEdition import NextionApp, Writer 
import RPi.GPIO as GPIO
from time import sleep
import asyncio

class LightController: 
    def __init__(self, lightChangedCallback, isTimeToLightingCallback):        
        self._lightChangedCallback = lightChangedCallback
        self._isTimeToLightingCallback = isTimeToLightingCallback
        loop = asyncio.get_event_loop()
        LoopTask = loop.create_task(self._Loop())
        asyncio.ensure_future(LoopTask) 
        # GPIO.cleanup() 
        GPIO.setwarnings(False)     
        GPIO.setmode(GPIO.BCM)
        
        self._levels = [LightLevel(0), LightLevel(1),LightLevel(2)]
        # for i in range(3):
        #     level=LightLevel(i)            
        #     self._levels[i] = level

    def SwitchLevel(self, levelId : int):
        result = self._levels[levelId].SwitchState()        
        self._lightChangedCallback(levelId, result)

    async def _Loop(self):
        while True:
            await asyncio.sleep(3)
            devState = self._isTimeToLightingCallback(0)
            for level in self._levels:
                # level.SetState(self._isTimeToLightingCallback(level.Id))
                level.SetState(devState)
                self._lightChangedCallback(level.Id, devState)
                

class LightLevel:
    Id=0
    _pins = [17,27,22]

    _bisabled = True

    def __init__(self, id:int):        
        self.Id = id
        GPIO.setup(self._pins[self.Id], GPIO.OUT, initial=GPIO.HIGH)
        pass

    def SwitchState(self):
        if self._bisabled == True:
            self._bisabled = False
        else:
            self._bisabled = True        

        self.SwitchRele()
        return  self._bisabled  

    def SetState(self, state:bool ):
        self._bisabled = not state
        self.SwitchRele()
        


    def SwitchRele(self):
        print(f'[{self}]: SwitchRele() _enabled: {self._bisabled}')
        GPIO.output(self._pins[self.Id], self._bisabled)
        
if __name__ == "__main__":
    controller = LightController(None)
    while True:
        sleep(1)
        controller.SwitchLevel(0)
        sleep(1)
        controller.SwitchLevel(1)
        sleep(1)
        controller.SwitchLevel(2)