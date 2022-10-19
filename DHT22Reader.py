import adafruit_dht
import board
import asyncio
import Site.Server
 

_loop = None

class DHTReader:

    _dhtDevice = None
    _currentDHT = 20, 90
    # temperature, humidity = 20, 90


    # def Start(self):
    #     print('')
    #     loop = asyncio.get_event_loop()
    #     sensorTask = loop.create_task(self.ReadSensor())
    #     asyncio.ensure_future(sensorTask)
    #     loop.run_forever()

    def __init__(self):
        self._dhtDevice = adafruit_dht.DHT22(board.D9)       

    async def ReadSensor(self):
        while True:
            # print(f"[DHTReader]: ReadSensor() ... 1 ...")
            try:
                # print(f"[DHTReader]: ReadSensor() ... 2 ...")
                temperature = self._dhtDevice.temperature
                temperatureFile = open('/home/pi/Documents/Project1/Data/temperature.txt', 'w')
                temperatureFile.write(str(temperature))
                temperatureFile.close()
                # print(f"[DHTReader]: ReadSensor() ... 3 ...")
                humidity = self._dhtDevice.humidity
                
                # print(f"[DHTReader]: ReadSensor() ... 4 ...")
                # print("Temp: {:.1f} C Humidity: {}%".format(temperature, humidity))
                self._currentDHT = temperature, humidity                
                # print(f"[DHTReader]: ReadSensor() ... 5 ...")
                await asyncio.sleep(5)
            except RuntimeError as error:
                print(f"[DHTReader]: RuntimeError: {error.args[0]}")
                await asyncio.sleep(1)
                continue
            except Exception as error:
                print(f"[DHTReader]: Exception: {error.args[0]} --> dhtDevice.exit()")
                self._dhtDevice.exit()
                raise error
            
        
    def GetCurrentDHT(self):
        # print("Temp:", self._currentDHT[0])
        # print("Humidite:", self._currentDHT[1])
        return self._currentDHT

if __name__ == '__main__':
    print('main')
    testDHTReader = DHTReader() 
    loop = asyncio.get_event_loop()
    sensorTask = loop.create_task(testDHTReader.ReadSensor())
    asyncio.ensure_future(sensorTask)
    loop.run_forever()