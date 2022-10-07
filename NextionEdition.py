from datetime import datetime
from nextion import Nextion, EventType
import asyncio

_nextionApp = None
c = 0

class NextionApp: 
    Connected = False

    _switchPageListener = None
    Client = None

    serial0_url = '/dev/serial0'
    # serial_url = '/dev/ttyS0'
    def __init__(self, switchPageListener):
        if(switchPageListener == None):
            self._switchPageListener = self.SwichPageTo
        else:
            self._switchPageListener = switchPageListener
        
        self.Client = Nextion(self.serial0_url, 9600, self.__Event_handler)
        # loop = asyncio.get_event_loop()
        # asyncio.ensure_future(self.Run())
        # loop.run_forever()

    def SwichPageTo(self, pageId : int):
        print(f"[NextionApp]: SwichPageTo({pageId})")
        command = f"page {pageId}"

        try:
            asyncio.ensure_future(self.__SendCommand(command))          
                
                
        except RuntimeError as error:
            print(error.args[0])
        except Exception as error:                
            self._client.disconnect()
            print(error.args[0])
            raise error
        


    def __Event_handler(self, type_, data):
        
        if type_ == EventType.STARTUP:
            print('We have booted up!')
        elif type_ == EventType.TOUCH:
            print('A button (id: %d) was touched on page %d' % (data.component_id, data.page_id))

        if(data.page_id == 0):
            if(data.component_id == 1):
                self._switchPageListener(1)

        if(data.page_id ==1):
            if(data.component_id == 1):
                self._switchPageListener(0)
    
    async def Run(self):                 
            print('connect...')
            await self.Client.connect()  
            print('connected!') 
            self.Connected = True   

    async def __SendCommand(self, command):
        await self.Client.command(command)
        


if __name__ == '__main__':
    _nextionApp = NextionApp(None)
    
    loop = asyncio.get_event_loop()
    sensorTask = loop.create_task(_nextionApp.Run())
    asyncio.ensure_future(sensorTask)
    loop.run_forever()

class Writer():
    _client = None
    def __init__(self, nextionApp: NextionApp):
        self._client = nextionApp.Client

    async def SendTemperatura(self, temperature):
        try:
            print(f"посылаю данные на дисплей: [temperature: {temperature}]...")
            await self._client.set('page0.t4.txt', "%.1f" % (temperature))
                
                
        except RuntimeError as error:
            print(error.args[0])
        except Exception as error:                
            self._client.disconnect()
            print(error.args[0])
            raise error

    async def SendHumidity(self,humidity):
        print(f"посылаю данные на дисплей: [humidity: {humidity}]...")
        await self._client.set('page0.t5.txt', "%.1f" % (humidity))
        
    async def SendCO2(self,CO2):
        print(f"посылаю данне на дисплей: [CO2: {CO2}]...")
        await self._client.set('page0.t8.txt', "%.1f" %{CO2})    
    
    async def SendTime(self):
        
            print(f"send time...")
            dateTimeData = []
            now = datetime.now()
            print(f"{now.year}.{now.month}.{now.day} - {now.hour}:{now.minute}:{now.second}")
            dateTimeData.append(now.year) 
            print(f"0")       
            dateTimeData.append(now.month)
            print(f"1") 
            dateTimeData.append(now.day)
            print(f"2") 
            dateTimeData.append(now.hour)
            print(f"3") 
            dateTimeData.append(now.minute)
            print(f"4") 
            dateTimeData.append(now.second)
            
            for i in range(len(dateTimeData)):            
                try:                
                    print(f"rtc{i} : {dateTimeData[i]}")
                    await self._client.set(f'rtc{i}', dateTimeData[i])
                    await asyncio.sleep(3)
                    # await self._client.command(f"rtc{i}={dateTimeData[i]}")
                except RuntimeError as error:
                    print(error.args[0])
                except Exception as error:                
                    print(error.args[0])
                    raise error

            

            


        
