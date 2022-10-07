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
    await asyncio.sleep(1)    
    __OnPageChanged(0)


if __name__ == '__main__':
    _pageControllerApp = PageControllerApp(__OnPageChanged)
    _nextionApp = NextionEdition.NextionApp(_pageControllerApp.SwichPageTo)
    _pageSwicher = ProgramState.Pageswicher(_nextionApp)
    
    loop = asyncio.get_event_loop()
    mainLoopTask = loop.create_task(MainLoop())
    asyncio.ensure_future(mainLoopTask)
    loop.run_forever()
    
