import adafruit_dht
import board
import asyncio
 

_loop = None

class DHTReader:

    _dhtDevice = None
    _currentDHT = 20, 90
    _isActive = False 
    
    def __init__(self):
        self._dhtDevice = adafruit_dht.DHT22(board.D9)       

    def Stop(self):
        self._isActive = False
        self._dhtDevice.exit()

    async def Start(self):
        self._isActive =True
        while self._isActive:
            print(f"[DHTReader]: ReadSensor() ... ")
            try:
                # print(f"[DHTReader]: ReadSensor() ... 2 ...")                
                temperature = self._dhtDevice.temperature
                # print(f"[DHTReader]: ReadSensor() ... 3 ...")
                temperatureFile = open('/home/pi/Documents/Project1/Data/temperature.txt', 'w')
                temperatureFile.write(str(temperature))
                temperatureFile.close()
                # print(f"[DHTReader]: ReadSensor() ... 4 ...")
                humidity = self._dhtDevice.humidity
                humidityFile = open('/home/pi/Documents/Project1/Data/humidity.txt', 'w')
                humidityFile.write(str(humidity))
                humidityFile.close()

                TemperatureFile = open("/home/pi/Documents/Project1/Data/TemperatureHistory.txt", "r")
                fff = TemperatureFile.readline()
                TemperatureFile.close()
                llll= fff.split(sep =",")
                llll.append(f"{temperature}")
                outStr = ",".join(llll)
                TemperatureFile = open("/home/pi/Documents/Project1/Data/TemperatureHistory.txt", "w")
                TemperatureFile.write(outStr)                
                TemperatureFile.close()

                # print(f"[DHTReader]: ReadSensor() ... 5 ...")
                # print("Temp: {:.1f} C Humidity: {}%".format(temperature, humidity))
                self._currentDHT = temperature, humidity                
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
        if(self._currentDHT == None):
            return [0,0]
        else:
            return self._currentDHT

if __name__ == '__main__':
    print('main')
    testDHTReader = DHTReader() 
    loop = asyncio.get_event_loop()
    # sensorTask = loop.create_task(testDHTReader.Start())
    sensorTask = asyncio.create_task(testDHTReader.Start())
    asyncio.ensure_future(sensorTask)
    loop.run_forever()