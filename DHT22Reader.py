import adafruit_dht
import board
from time import sleep
import time
import asyncio
 
dhtDevice = adafruit_dht.DHT22(board.D10)

_loop = None

class DHTReader:

    _currentDHT = 20, 90
    # temperature, humidity = 20, 90


    # def Start(self):
    #     print('')
    #     loop = asyncio.get_event_loop()
    #     sensorTask = loop.create_task(self.ReadSensor())
    #     asyncio.ensure_future(sensorTask)
    #     loop.run_forever()        

    async def ReadSensor(self):
        while True:
            await asyncio.sleep(2)
            try:
                temperature = dhtDevice.temperature
                humidity = dhtDevice.humidity
                # print("Temp: {:.1f} C Humidity: {}%".format(temperature, humidity))
                self._currentDHT = temperature, humidity
            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2)
                continue
            except Exception as error:
                dhtDevice.exit()
                raise error
            time.sleep(1.0)
        
    def GetCurrentDHT(self):
        return self._currentDHT

if __name__ == '__main__':
    print('main')
    testDHTReader = DHTReader() 
    loop = asyncio.get_event_loop()
    sensorTask = loop.create_task(testDHTReader.ReadSensor())
    asyncio.ensure_future(sensorTask)
    loop.run_forever()