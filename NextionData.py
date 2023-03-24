from enum import Enum

class Page_1(Enum): #page_main
    qrID = 0
    settingsButtonID = 1
    handleButtonID = 2
    grafikButtonID = 3

class Page_2(Enum): #page_settings
    backButtonID = 1
    exitButtonID = 6
    dayMinusButtonID = 4
    dayPlusButtonID = 5    

class Page_3(Enum): #page_handle
    backButtonID = 1
    lightButtonID = 3
    pumpButtonID = 5
        

class Page_4(Enum): #page_graf
    backButtonID = 1
    waveFormID = 2    
