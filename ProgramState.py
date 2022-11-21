from NextionEdition import NextionApp, Writer
from DHT22Reader import DHTReader
from CO2Reader import CO2
import asyncio
import socket

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
        self.__active = True                  
        
        asyncio.ensure_future(self.__Start()) 

    def Exit(self):
        self.__active = False

    async def __Start(self):
        print(f"[Page0]: __Start() ... 1 ...")
        await self.__nextionWriter.SendTime()
        
        tasks=[]
          
        print(f"[Page0]: __Start() ... 2 ...")

        taskDHT = asyncio.create_task(self.__dhtReader.ReadSensor())
        tasks.append(taskDHT)
        print(f"[Page0]: __Start() ... 3 ...")
        taskSendDHT = asyncio.create_task(self.SendDHT())
        tasks.append(taskSendDHT)
        print(f"[Page0]: __Start() ... 4 ...")
        taskQr = asyncio.create_task(self.SendQr())
        tasks.append(taskQr)

        taskCO2 = asyncio.create_task(self.__co2Reader.Start())
        tasks.append(taskCO2)
        print(f"[Page0]: __Start() ... 5 ...")
        taskSendCO2 = asyncio.create_task(self.SendCO2())
        tasks.append(taskSendCO2)
        try:                
            print(f"[Page0]: __Start() ... 6 ...")
            await asyncio.gather(*tasks)
            print(f"[Page0]: __Start() ... 7")
                    
        except RuntimeError as error:
            print(f"[Page0]: __Start() RuntimeError: {error.args[0]}")
        except Exception as error:                
            print(f"[Page0]: __Start() Exception: {error.args[0]}")            
            
        
    async def SendDHT(self):
        while self.__active:
            print(f"[Page0]: SendDHT() ... 1 ...")
            dht = self.__dhtReader.GetCurrentDHT()
            if(dht != None):
                if(dht[0] != None):
                    print(f"[Page0]: SendDHT() ... 2 ...")
                    await self.__nextionWriter.SendTemperatura(dht[0])
                if(dht[1] != None):
                    print(f"[Page0]: SendDHT() ... 3 ...")
                    await self.__nextionWriter.SendHumidity(dht[1])
            
            await asyncio.sleep(3)

    async def SendQr(self):
        # host = socket.getaddrinfo(socket.gethostname(), None)
        # ipv4_addresses = [i[4][0] for i in host if i[0] == socket.AF_INET]
        # print(f"[Page0]: SendQr() ipv4_addresses = {ipv4_addresses}")

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = f"http://{s.getsockname()[0]}:5000" 
        print(f"[Page0]: SendQr() ip = {ip}")
        await self.__nextionWriter.SendQrCode(ip)

    async def SendCO2(self):
        while self.__active:
            print(f"[Page0]: SendCO2()")
            co2 = str(self.__co2Reader.GetCurrentCO2())
            await self.__nextionWriter.SendCO2(co2)
            await asyncio.sleep(3)

class Page1:
    __active = False
    def __init__(self, appClient: NextionApp):        
        appClient.SwichPageTo(1)

    def Enter(self):
        self.__active = True

    def Exit(self):
        self.__active = False   