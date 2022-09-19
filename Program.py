import asyncio
from time import sleep
import NextionEdition
from PageController import PageControllerApp
import CO2Reader
import DHT22Reader

_pageControllerApp = None
_nextionApp = None
_co2Reader = None
_DHTReader = None


def __OnPageChanged(pageId : int):
    print("rastup")
    _nextionApp.SwichPageTo(pageId)

async def MainLoop():
    tasks=[]

    

async def PrintCo2():
    while True:
        print(f"CO2:", _co2Reader.GetCurrentCO2())
        await asyncio.sleep(1)

async def PrintDHT():
    while True:
        dht = _DHTReader.GetCurrentDHT()
        print("Temp:", dht[0])
        print("Humidite:", dht[1])
        await asyncio.sleep(1)


if __name__ == '__main__':
    _pageControllerApp = PageControllerApp(__OnPageChanged)
    _nextionApp = NextionEdition.NextionApp(_pageControllerApp.SwichPageTo)
    _DHTReader = DHT22Reader.DHTReader()  
    _co2Reader = CO2Reader.CO2()
    loop = asyncio.get_event_loop()
    mainLoopTask = loop.create_task(MainLoop())
    asyncio.ensure_future(mainLoopTask)
    loop.run_forever()

    # asyncio.run(MainLoop())
