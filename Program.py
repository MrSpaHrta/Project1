# import keyboard
import asyncio
from time import sleep
import NextionEdition
from PageController import PageControllerApp
import ProgramState

_pageControllerApp = None
_nextionApp = None
_co2Reader = None
_DHTReader = None
_nextionWriter = None
_pageSwicher = None

workEnabled = True


# def StopProgram():
#     workEnabled = False
#     _nextionApp._client.disconnect()

# keyboard.on_press_key("q", StopProgram)


def __OnPageChanged(pageId : int):    
    _pageSwicher.SetPage(pageId)

async def MainLoop():  
    await _nextionApp.Run()    
    __OnPageChanged(0)   
    
    # tasks=[]
    # taskSendDateTime = asyncio.create_task(_nextionWriter.SendTime())
    # tasks.append(taskSendDateTime)    

    # # taskCO2 = asyncio.create_task(_co2Reader.Start())
    # # tasks.append(taskCO2)

    # # taskPrintCo2 = asyncio.create_task(PrintCo2())
    # # tasks.append(taskPrintCo2)

    # taskDHT = asyncio.create_task(_DHTReader.ReadSensor())
    # tasks.append(taskDHT)

    # taskPrintDHT = asyncio.create_task(PrintDHT())
    # tasks.append(taskPrintDHT)

    # await asyncio.gather(tasks)

# async def PrintCo2():
#     while workEnabled:
#         print(f"CO2:", _co2Reader.GetCurrentCO2())
#         await asyncio.sleep(1)

# async def PrintDHT():
#     await asyncio.sleep(30)
#     while workEnabled:
#         dht = _DHTReader.GetCurrentDHT()
#         print("Temp:", dht[0])
#         print("Humidite:", dht[1])
#         await _nextionWriter.SendTemperatura(dht[0])
#         await _nextionWriter.SendHumidity(dht[1])
#         await asyncio.sleep(3)


if __name__ == '__main__':
    _pageControllerApp = PageControllerApp(__OnPageChanged)
    _nextionApp = NextionEdition.NextionApp(_pageControllerApp.SwichPageTo)
    _pageSwicher = ProgramState.Pageswicher(_nextionApp)
    # _DHTReader = DHT22Reader.DHTReader() 
    # _nextionWriter = NextionEdition.Writer(appClient = _nextionApp._client) 
    # _co2Reader = CO2Reader.CO2()
    loop = asyncio.get_event_loop()
    mainLoopTask = loop.create_task(MainLoop())
    asyncio.ensure_future(mainLoopTask)
    loop.run_forever()

    # asyncio.run(MainLoop())
