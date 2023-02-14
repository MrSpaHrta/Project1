from datetime import datetime

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
        self._weeks = [GrowingWeek(), GrowingWeek(),GrowingWeek(),GrowingWeek()]
        self._actualWeek = 0

    def IsTimeToWater(self):
        return self._weeks[self._actualWeek].IsTimeToWater()

    def IsTimeToLighting(self, level:int):
        return self._weeks[self._actualWeek].IsTimeToLighting(level)

class GrowingWeek:
    def __init__(self):
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
        self._durationSeconds = 10

        self._level_0_startTimes = [HousMinutes(0, 0), HousMinutes(0, 0)]
        self._level_1_startTimes = [HousMinutes(0, 0), HousMinutes(0, 0)]
        self._level_2_startTimes = [HousMinutes(0, 0), HousMinutes(0, 0)] 

    def IsTimeToLigghting(self, level:int):
        self._devIsTimeTo = not self._devIsTimeTo
        return self._devIsTimeTo

class MixstureUnit:
    pass

class HousMinutes:
    Hour = 0
    Minute = 0 
    def __init__(self, hour:int, minute:int):
        self.Hour = hour
        self.Minute = minute
