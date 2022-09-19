from nextion import Nextion, EventType
import asyncio

_nextionApp = None
c = 0

class NextionApp: 

    _switchPageListener = None
    _client = None

    serial0_url = '/dev/serial0'
    # serial_url = '/dev/ttyS0'
    def __init__(self, switchPageListener):
        if(switchPageListener == None):
            self._switchPageListener = self.SwichPageTo
        else:
            self._switchPageListener = switchPageListener
        
        self._client = Nextion(self.serial0_url, 9600, self.__Event_handler)
        # loop = asyncio.get_event_loop()
        # asyncio.ensure_future(self.Run())
        # loop.run_forever()

    def SwichPageTo(self, pageId : int):
        print(f"open page {pageId}")
        command = f"page {pageId}"
        asyncio.ensure_future(self.__SendCommand(command))



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
        await self._client.connect()
        while True:
            await asyncio.sleep(1)

    async def __SendCommand(self, command):
        await self._client.command(command)


if __name__ == '__main__':
    _nextionApp = NextionApp(None)
    
    loop = asyncio.get_event_loop()
    sensorTask = loop.create_task(_nextionApp.Run())
    asyncio.ensure_future(sensorTask)
    loop.run_forever()

class Writer:
    client = NextionApp._client
    async def SendTemperatura(self, temperature):
        print(f"посылаю данные на дисплей: [temperature: {temperature}]...")
        await self.client.set('page0.t4.txt', "%.1f" % (temperature))
    async def SendHumidity(self,humidity):
        print(f"посылаю данные на дисплей: [humidity: {humidity}]...")
        await self.client.set('page0.t5.txt', "%.1f" % (humidity))
    async def SendCO2(self,CO2):
        print(f"посылаю данне на дисплей: [CO2: {CO2}]...")
        await self.client.set('page0.t8.txt', "%.1f" %{CO2})
    
    # async def SendTime(self):
    #     dateTimeData = []
    #     now = datetime.now()
    #     dateTimeData.append(now.year)
    #     dateTimeData.append(now.month)
    #     dateTimeData.append(now.day)
    #     dateTimeData.append(now.hour)
    #     dateTimeData.append(now.minute)
    #     dateTimeData.append(now.second)
        
