import adafruit_dht
import board
import asyncio
 

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
                humidityFile = open('/home/pi/Documents/Project1/Data/humidity.txt', 'w')
                humidityFile.write(str(humidity))
                humidityFile.close()

                TemperatureFile = open("/home/pi/Documents/Project1/Data/Temperature.txt", "r")
                fff = TemperatureFile.readline()
                TemperatureFile.close()
                llll= fff.split(sep =",")
                llll.append(f"{temperature}")
                outStr = ",".join(llll)
                TemperatureFile = open("/home/pi/Documents/Project1/Data/Temperature.txt", "w")
                TemperatureFile.write(outStr)                
                TemperatureFile.close()

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