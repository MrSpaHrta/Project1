from datetime import datetime
import ScheduleData

class GrowingController:
    def __init__(self):
        self._schedule = SceduleItem()
        

    def CreateDefaulSchedule():
        pass

    def IsTimeToWater(self):
        return self._schedule.IsTimeToWater()

    def IsTimeToLighting(self, level:int):
        return self._schedule.IsTimeToLighting(level)
    
class SceduleItem:
    
    def __init__(self):
        self._data = ScheduleData.DataContainer()
        week1_data = self._data.Load(1)
        week2_data = self._data.Load(2)
        week3_data = self._data.Load(3)
        week4_data = self._data.Load(4)
        self._weeks = [GrowingWeek(week1_data), GrowingWeek(week2_data),GrowingWeek(week3_data),GrowingWeek(week4_data)]
        self._actualWeek = 0

    def IsTimeToWater(self):
        return self._weeks[self._actualWeek].IsTimeToWater()

    def IsTimeToLighting(self, level:int):
        return self._weeks[self._actualWeek].IsTimeToLighting(level)

class GrowingWeek:
    def __init__(self, data):
        self.watering = Watering()
        self.lighting = Lighting()
        self.mixstureUnit = MixstureUnit()

    def IsTimeToWater(self):
        return self.watering.IsTimeToWater()

    def IsTimeToLighting(self, level:int):
        return self.lighting.IsTimeToLigghting(level)

class Watering:

    _devIsTimeToWater = False

    def __init__(self):
        self.durationMinutes = 1
        self._startTimes = [HousMinutes(11, 30), HousMinutes(11, 32), HousMinutes(11, 34)]
        self._lastStart = HousMinutes(0, 0)

    def IsTimeToWater(self):
        # self._devIsTimeToWater = not self._devIsTimeToWater
        # return self._devIsTimeToWater
        
        result = False
        now = datetime.now()
        hour = now.hour
        minute = now.minute

        for item in self._startTimes:
            if(hour == item.Hour):
                i_minute = item.Minute
                if(i_minute <= minute and i_minute+self.durationMinutes > minute):
                    result = True
        print(f"=========\n[Watering]: IsTimeToWater() result: {result}")
        return result
            
   

class Lighting:
    _devIsTimeTo = False
    def __init__(self):
        self.durationMinutes = 2

        self._level_0_startTimes = [HousMinutes(9, 51), HousMinutes(10, 55)]
        self._level_1_startTimes = [HousMinutes(9, 52), HousMinutes(10, 56)]
        self._level_2_startTimes = [HousMinutes(9, 53), HousMinutes(10, 57)] 

    def IsTimeToLigghting(self, level:int):
        now = datetime.now()
        hour = now.hour
        minute = now.minute

        result = False
        
        if(level == 0):
            levelTimes = self._level_0_startTimes
        elif(level == 1):
            levelTimes = self._level_1_startTimes
        elif(level == 2):
            levelTimes = self._level_2_startTimes        
        
        for item in levelTimes:
            if(hour == item.Hour):  
                startMinute = item.Minute
                stopMinute = item.Minute+self.durationMinutes             
                if(startMinute <= minute and stopMinute > minute):
                    result = True
        print(f"=========\n[Ligghting]: IsTimeToLigghting({level}) : {result}") 
        return result 

class MixstureUnit:
    pass

class HousMinutes:
    Hour = 0
    Minute = 0 
    def __init__(self, hour:int, minute:int):
        self.Hour = hour
        self.Minute = minute
