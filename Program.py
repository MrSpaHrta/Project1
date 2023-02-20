import asyncio
import NextionEdition
from PageModule import PageController
import ProgramState
import LightModule
import Rezervuar
import GrowingSchedule

import RPi.GPIO as GPIO
import sys
import os
import subprocess

_pageControllerApp = None
_lightController =None
_nextionApp = None
_pageSwicher = None
_rezervuar = None
workEnabled = True

# def StopProgram():
#     workEnabled = False
#     _nextionApp._client.disconnect()
# keyboard.on_press_key("q", StopProgram)

def __OnPageChanged(pageId : int):    
    _pageSwicher.SetPage(pageId)

def __OnLightChanged(level:int, state: bool):
    print("========== Call async change button state ============")
    nextionWriter = NextionEdition.Writer(_nextionApp)
    asyncio.ensure_future(nextionWriter.SetLightLevelButtonState(level, state))
    

async def MainLoop():  
    await _nextionApp.Run()
    await asyncio.sleep(1)     
    __OnPageChanged(1)
    print("Program Started")

    try:        
        subprocess.Popen('/bin/python3 /home/pi/Documents/Project1/Site/Server.py', shell=True)        
        
    except Exception as error:
        print("Server starting ERROR!!! :" + error.args[0])    

def Exit():
    GPIO.cleanup()
    sys.exit() 


if __name__ == '__main__':     
    _pageControllerApp = PageController(__OnPageChanged)
    _growingController = GrowingSchedule.GrowingController()
    _lightController = LightModule.LightController(__OnLightChanged, _growingController.IsTimeToLighting)
    _nextionApp = NextionEdition.NextionApp(_pageControllerApp.SwichPageTo, _lightController.SwitchLevel, Exit)
    _pageSwicher = ProgramState.Pageswicher(_nextionApp)
    _rezervuar = Rezervuar.ReservuarController(_growingController.IsTimeToWater, debug=False)
    loop = asyncio.get_event_loop()
    mainLoopTask = loop.create_task(MainLoop())
    asyncio.ensure_future(mainLoopTask)
    loop.run_forever()
    
