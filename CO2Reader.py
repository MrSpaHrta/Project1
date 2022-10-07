from csv import reader
import mh_z19
from time import sleep
import asyncio

ama_url = '/dev/ttyAMA2'


class CO2:

    _currentCO2 = 0
    _isActive = False

    def __init__(self):
        mh_z19.set_serialdevice(ama_url)  

        
    async def Start(self):
        self._isActive = True
        while self._isActive:
            result = mh_z19.read_all(serial_console_untouched=True)
            co2 = str(result.get('co2'))
            self._currentCO2 = co2              
            await asyncio.sleep(3)
    
    def Stop(self):
        self._isActive = False

    def GetCurrentCO2(self):
        return self._currentCO2

if __name__ == '__main__':
    print('main')
    testReader = CO2()
    loop = asyncio.get_event_loop()
    sensorTask = loop.create_task(testReader.Start())
    asyncio.ensure_future(sensorTask)
    loop.run_forever()
    

