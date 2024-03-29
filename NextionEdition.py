
from datetime import datetime
from nextion import Nextion, EventType
import asyncio

import NextionData as IDs
# import RPi.GPIO as GPIO

_nextionApp = None
c = 0

class NextionApp: 
    Connected = False

    _switchPageListener = None
    _switchLightListener = None
    Client = None

    serial0_url = '/dev/serial0'
    # serial_url = '/dev/ttyS0'

    def __init__(self, switchPageListener, switchLightListener, exitCallback):
        
        self._exitCallback = exitCallback
        if(switchPageListener == None):
            self._switchPageListener = self.SwichPageTo
        else:
            self._switchPageListener = switchPageListener
            self._switchLightListener = switchLightListener
        self.Client = Nextion(self.serial0_url, 9600, self.__Event_handler)
        
        
    def SwichPageTo(self, pageId : int):

        print(f"[NextionApp]: SwichPageTo({pageId})")

        command = f"page {pageId}"

        try:
            exit = (pageId == 0)
            asyncio.ensure_future(self.__SendCommand(command, exit))
            
                        
                
        except RuntimeError as error:
            print(error.args[0])
        except Exception as error:                
            self.Client.disconnect()
            print(error.args[0])
            raise error
        


    def __Event_handler(self, type_, data):
        
        if type_ == EventType.STARTUP:
            print('We have booted up!')
        elif type_ == EventType.TOUCH:
            print('A button (id: %d) was touched on page %d' % (data.component_id, data.page_id))

        if(data.page_id == 1):            
            if(data.component_id == IDs.P1_settingsButtonID):
                self._switchPageListener(2)
            if(data.component_id == IDs.P1_handleButtonID):
                self._switchPageListener(3)        
            if(data.component_id == IDs.P1_grafikButtonID):
                self._switchPageListener(4)

        if(data.page_id ==2):
            if(data.component_id == IDs.P2_backButtonID):
                self._switchPageListener(1)
        if(data.page_id ==3):
            if(data.component_id == IDs.P3_backButtonID):
                self._switchPageListener(1)
        if(data.page_id ==4):
            if(data.component_id == IDs.P4_backButtonID):
                self._switchPageListener(1)               


        
        if(data.page_id == 3):
            if(data.component_id == IDs.P3_lightButtonID):
                pass # self._switchLightListener(2) #переключить свет

        if(data.page_id == 3):
            if(data.component_id == IDs.P3_pumpButtonID):
                pass #переключить насос        

        if(data.page_id == 2):
            if(data.component_id == IDs.P2_exitButtonID):
                self._switchPageListener(0) #выключаем программу
                    
    
    async def Run(self):                 
            print('connect...')
            await self.Client.connect()  
            print('connected!') 
            self.Connected = True   

    async def __SendCommand(self, command, exit:bool ):
        await self.Client.command(command)
        if(exit):
            await self.Client.disconnect()
            self._exitCallback()   
        


if __name__ == '__main__':
    _nextionApp = NextionApp(None, None)
    
    loop = asyncio.get_event_loop()
    task = loop.create_task(_nextionApp.Run())
    asyncio.ensure_future(task)
    loop.run_forever()

class Writer():
    _client = None
    def __init__(self, nextionApp: NextionApp):
        print(f'[Nextion Writer] __init__(): nextionApp:[{nextionApp}]')
        self._client = nextionApp.Client

    async def SendTemperatura(self, temperature):
        print(f"посылаю данные на дисплей: [temperature: {temperature}]...")
        await self._client.set('page_main.airT.txt', "%.1f" % (temperature))

    async def SendTempereGrafPoint(self, temperature):
        print(f"Send Tempere Graf Point: [temperature: {(temperature)}]...")
        # await self._client.set('page0.t4.txt', "%.1f" % (temperature))
        await self._client.command(f'add {2},0,{int(temperature*10)}')
        await self._client.set('page_graf.s0.txt')

    async def SendHumidity(self,humidity):
        print(f"посылаю данные на дисплей: [humidity: {humidity}]...")
        await self._client.set('page_main.airH.txt', "%.1f" % (humidity))
        
    async def SendCO2(self, CO2: str):
        print(f"посылаю данне на дисплей: [CO2: {CO2}]...")
        await self._client.set('page_main.airCO.txt', CO2)
    
    async def SendQrCode(self, qrCode:str):
        print(f"посылаю QR на дисплей: [QR: {qrCode}]...")
        await self._client.set('page_main.qr0.txt', qrCode)      
    
    async def SendTime(self):
        
            print(f"[Writer]: SendTime()...")
            
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
                    await asyncio.sleep(0.3)
                    # await self._client.command(f"rtc{i}={dateTimeData[i]}")
                except RuntimeError as error:
                    print(error.args[0])
                except Exception as error:                
                    print(error.args[0])
                    raise error

    async def SetLightLevelButtonState(self, level: int, state: bool):
        await asyncio.sleep(10)
        # print(f"меняю состояние кнопок на дисплее: [level: {level}: state: {state}]...")
        # # await self._client.set(f'page0.b_light{level}.val', state) 
        # text = ""
        # if(state == True):
        #     text = "On"
        # else:
        #     text = "Off"
        
        # try:                
        #     await self._client.set(f'page0.b_light{level}.txt', text)       
                    
        # except RuntimeError as error:
        #     print("RuntimeError: "+error.args[0])
        # except Exception as error:                
        #     print("Exception: "+error.args[0])
        #     raise error

        

            


        
