from NextionEdition import NextionApp, Writer
from DHT22Reader import DHTReader
from CO2Reader import CO2
import asyncio
import socket

class Pageswicher:

    pageNamber = 0
    activePage = None
    
    nextionClient = None

    def __init__(self, nextionClient: NextionApp):
        self.nextionClient = nextionClient

    def SetPage(self, value : int):
        print(f"[Pageswicher]: SetPage{value}")
        self.pageNamber = value
        if(self.activePage != None):
            self.activePage.Exit()
        
        page = None
        if (self.pageNamber == 0):
            page = Page0(self.nextionClient)

        if (self.pageNamber == 1):
            page = Page1(self.nextionClient)
            
        if (self.pageNamber == 2):
            page = Page2(self.nextionClient)
        if (self.pageNamber == 3):
            page = Page3(self.nextionClient)
        if (self.pageNamber == 4):
            page = Page4(self.nextionClient)
            

        self.activePage = page;   
        self.activePage.Enter()

    def OnLightChanged(self, level:int, state: bool):
        
        if(isinstance(self.activePage, Page1)):
            self.activePage.OnLightChanged(level, state)

class Page0: #page_off
    __active = False
    def __init__(self, appClient: NextionApp):        
        appClient.SwichPageTo(0)

    def Enter(self):
        self.__active = True

    def Exit(self):
        self.__active = False   

class Page1: #page_main
    __nextionWriter = None
    __dhtReader = None
    __co2Reader = None
    __active = False    

    def __init__(self, appClient: NextionApp):
        
        self.__nextionWriter = Writer(appClient)        
        self.__dhtReader = DHTReader()        
        self.__co2Reader = CO2()        
        appClient.SwichPageTo(1)        

        
    def Enter(self):        
        self.__active = True        
        asyncio.ensure_future(self.__Start()) 

    def Exit(self):
        self.__active = False
        self.__co2Reader.Stop()
        self.__dhtReader.Stop()

    async def __Start(self):
        # await self.__nextionWriter.SendTime()
        
        tasks=[]
          
        
        taskDHT = asyncio.create_task(self.__dhtReader.Start())
        tasks.append(taskDHT)
        taskSendDHT = asyncio.create_task(self.SendDHT())
        tasks.append(taskSendDHT)
        taskQr = asyncio.create_task(self.SendQr())
        tasks.append(taskQr)

        taskCO2 = asyncio.create_task(self.__co2Reader.Start())
        tasks.append(taskCO2)
        taskSendCO2 = asyncio.create_task(self.SendCO2())
        tasks.append(taskSendCO2)
        try:                
            await asyncio.gather(*tasks)
                    
        except RuntimeError as error:
            print(f"[Page1]: __Start() RuntimeError: {error.args[0]}")
        except Exception as error:                
            print(f"[Page1]: __Start() Exception: {error.args[0]}")            
            
        
    async def SendDHT(self):
        while self.__active:
            dht = self.__dhtReader.GetCurrentDHT()
            print(f"[Page1]: SendDHT() dht = {dht[0]}; {dht[1]}")
            if(dht != None):
                if(dht[0] != None):
                    await self.__nextionWriter.SendTemperatura(dht[0])
                if(dht[1] != None):
                    await self.__nextionWriter.SendHumidity(dht[1])
            
            await asyncio.sleep(3)

    async def SendQr(self):
        # host = socket.getaddrinfo(socket.gethostname(), None)
        # ipv4_addresses = [i[4][0] for i in host if i[0] == socket.AF_INET]
        # print(f"[Page0]: SendQr() ipv4_addresses = {ipv4_addresses}")

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = f"http://{s.getsockname()[0]}:5000" 
        print(f"[Page1]: SendQr() ip = {ip}")
        await self.__nextionWriter.SendQrCode(ip)

    async def SendCO2(self):
        while self.__active:
            co2 = str(self.__co2Reader.GetCurrentCO2())
            print(f"[Page1]: SendCO2() co2 = {co2}")
            await self.__nextionWriter.SendCO2(co2)
            await asyncio.sleep(3)

    def OnLightChanged(self, level:int, state: bool):
        print("========== Call async change button state ============")        
        asyncio.ensure_future(self.__nextionWriter.SetLightLevelButtonState(level, state))            

class Page2: #page_settings
    __active = False
    def __init__(self, appClient: NextionApp):        
        appClient.SwichPageTo(2)

    def Enter(self):
        self.__active = True

    def Exit(self):
        self.__active = False  

class Page3: #page_handle
    __active = False
    def __init__(self, appClient: NextionApp):        
        appClient.SwichPageTo(3)

    def Enter(self):
        self.__active = True

    def Exit(self):
        self.__active = False  


class Page4: #page_graf
    
    __nextionWriter = None
    __dhtReader = None
    
    __active = False    

    def __init__(self, appClient: NextionApp):
        
        self.__nextionWriter = Writer(appClient)        
        self.__dhtReader = DHTReader()        
                
        appClient.SwichPageTo(4)        

        
    def Enter(self):        
        self.__active = True        
        asyncio.ensure_future(self.__Start()) 

    def Exit(self):
        self.__active = False
        
        self.__dhtReader.Stop()

    async def __Start(self):
        # while self.__active:
        print("Page 4 Active...")
        #     await asyncio.sleep(2)
        
        tasks=[]          
        
        taskDHT = asyncio.create_task(self.__dhtReader.Start())
        tasks.append(taskDHT)
        taskSendGrafPoints = asyncio.create_task(self.SendTemperatureGrafPoints())
        tasks.append(taskSendGrafPoints)  
        
        try:                
            await asyncio.gather(*tasks)
                    
        except RuntimeError as error:
            print(f"[Page4]: __Start() RuntimeError: {error.args[0]}")
        except Exception as error:                
            print(f"[Page4]: __Start() Exception: {error.args[0]}")            
            
        
    async def SendTemperatureGrafPoints(self):
        await asyncio.sleep(1)  
        
        while self.__active:
            print("Page 4 SendGrafPoint...")
            dht = self.__dhtReader.GetCurrentDHT()
            # if(dht != None):
            #     if(dht[0] != None):
            try: 
                await self.__nextionWriter.SendTempereGrafPoint(dht[0])
            except Exception as error:                
                print(f"[Page4]: __Start() SendTemperatureGrafPoints: {error.args[0]}") 
            
            await asyncio.sleep(1)    

    