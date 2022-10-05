from time import sleep
from NextionEdition import NextionApp, Writer
from DHT22Reader import DHTReader
from CO2Reader import CO2
from nextion import Nextion
import asyncio

class Pageswicher:

    pageNamber = 0
    activePage = None
    
    client = None

    def __init__(self, appClient: NextionApp):
        self.client = appClient

    def SetPage(self, value : int):
        print(f"[Pageswicher]: SetPage{value}")
        self.pageNamber = value
        if(self.activePage != None):
            self.activePage.Exit()
        
        page = None
        if (self.pageNamber == 0):
            page = Page0(self.client)
            
        if (self.pageNamber == 1):
            page = Page1(self.client)
            

        self.activePage = page;   
        self.activePage.Enter()

class Page0:
    __nextionWriter = None
    __dhtReader = None
    __co2Reader = None
    __active = False
    def __init__(self, appClient: NextionApp):
        self.__nextionWriter = Writer(appClient)
        self.__dhtReader = DHTReader()
        self.__co2Reader = CO2()
        appClient.SwichPageTo(0)

        
    def Enter(self):
        print(f"[Page0]: Enter()")
        loop = asyncio.get_running_loop() # asyncio.get_event_loop()
        print(f"[Page0]: Enter() ... 1 ...")
        startTask = loop.create_task(self.__Start())
        print(f"[Page0]: Enter() ... 2")
        # startTask = asyncio.create_task(self.__Start())
             
        
        asyncio.ensure_future(startTask)

    def Exit(self):
        __active = False

    async def __Start(self):
        print(f"[Page0]: __Start() ... 1 ...")
        # await self.__nextionWriter.SendTime()
        
        tasks=[]
        # taskSendDateTime = asyncio.create_task(self.__nextionWriter.SendTime())
        # tasks.append(taskSendDateTime)    
        print(f"[Page0]: __Start() ... 2 ...")

        taskDHT = asyncio.create_task(self.__dhtReader.ReadSensor())
        tasks.append(taskDHT)
        print(f"[Page0]: __Start() ... 3 ...")
        taskSendDHT = asyncio.create_task(self.SendDHT())
        tasks.append(taskSendDHT)
        print(f"[Page0]: __Start() ... 4 ...")

        # taskCO2 = asyncio.create_task(self.__co2Reader.Start())
        # tasks.append(taskCO2)

        # taskSendCO2 = asyncio.create_task(self.SendCO2())
        # tasks.append(taskSendCO2)
        try:                
            print(f"[Page0]: __Start() ... 5 ...")
            await asyncio.gather(tasks)
            print(f"[Page0]: __Start() ... 6")
                    
        except RuntimeError as error:
            print(f"[Page0]: __Start() RuntimeError: {error.args[0]}")
        except Exception as error:                
            print(f"[Page0]: __Start() Exception: {error.args[0]}")
            
        
    async def SendDHT(self):
        while self.__active:
            dht = self.__dhtReader.GetCurrentDHT()
            await self.__nextionWriter.SendTemperatura(dht[0])
            await self.__nextionWriter.SendHumidity(dht[1])
            await asyncio.sleep(3)

    async def SendCO2(self):
        while self.__active:
            co2 = self.__co2Reader.GetCurrentCO2()
            await self.__nextionWriter.SendCO2(co2[0])
            await asyncio.sleep(3)

class Page1:
    __active = False
    def __init__(self, appClient: NextionApp):        
        appClient.SwichPageTo(1)

    def Enter(self):
        __active = True

    def Exit(self):
        __active = False   