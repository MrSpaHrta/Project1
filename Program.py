import asyncio
import NextionEdition
from PageController import PageControllerApp
import ProgramState
import Rezervuar

_pageControllerApp = None
_nextionApp = None
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
    print("Started")


if __name__ == '__main__': 
    
    _pageControllerApp = PageControllerApp(__OnPageChanged)
    _nextionApp = NextionEdition.NextionApp(_pageControllerApp.SwichPageTo)
    _pageSwicher = ProgramState.Pageswicher(_nextionApp)
    
    loop = asyncio.get_event_loop()
    # for task in asyncio.all_tasks():
    #     task.cancel()

    mainLoopTask = loop.create_task(MainLoop())
    asyncio.ensure_future(mainLoopTask)
    loop.run_forever()
    
