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
        week1_data = self._data.LoadWeek(1)
        week2_data = self._data.LoadWeek(2)
        week3_data = self._data.LoadWeek(3)
        week4_data = self._data.LoadWeek(4)
        self._weeks = [GrowingWeek(week1_data), GrowingWeek(week2_data),GrowingWeek(week3_data),GrowingWeek(week4_data)]
        self._actualWeek = 0

    def IsTimeToWater(self):
        return self._weeks[self._actualWeek].IsTimeToWater()

    def IsTimeToLighting(self, level:int):
        return self._weeks[self._actualWeek].IsTimeToLighting(level)

class GrowingWeek:
    def __init__(self, data):
        self.watering = Watering(data.get("PumpDurations"), data.get("PumpStartHours"), data.get("PumpStartMinutes"))
        self.lighting = Lighting()
        self.mixstureUnit = MixstureUnit()

    def IsTimeToWater(self):
        return self.watering.IsTimeToWater()

    def IsTimeToLighting(self, level:int):
        return self.lighting.IsTimeToLigghting(level)

class Watering:
    #==========================================================
    #TODO полив я переделал. ТВОЯ задача - поправить освещение 
    #==========================================================

    _devIsTimeToWater = False

    def __init__(self, durations, startHours, startMinutes):       
        self._startTimes = [HoursMinutes(0, 0, 0)] * len(startHours) #задаём длинну и тип данных массива
              
        for id in range(len(self._startTimes)):    #заполняем массив
            self._startTimes[id] = HoursMinutes(startHours[id], startMinutes[id], durations[id])
        
        self._lastStart = HoursMinutes(0, 0, 0)

    def IsTimeToWater(self):
        # self._devIsTimeToWater = not self._devIsTimeToWater
        # return self._devIsTimeToWater
        
        result = False
        now = datetime.now()
        nowHour = now.hour
        nowMinute = now.minute

        for startTime in self._startTimes:
            if(nowHour == startTime.Hour):                
                if(startTime.Minute <= nowMinute and startTime.Minute+startTime.Duration > nowMinute):
                    result = True
        print(f"=========\n[Watering]: IsTimeToWater() result: {result}")
        return result
            
   

class Lighting:
    #TODO полив я переделал. ТВОЯ задача - поправить освещение 
    _devIsTimeTo = False
    def __init__(self):
        self.durationMinutes = 2

        self._level_0_startTimes = [HoursMinutes(9, 51,0), HoursMinutes(10, 55,0)]
        self._level_1_startTimes = [HoursMinutes(9, 52,0), HoursMinutes(10, 56,0)]
        self._level_2_startTimes = [HoursMinutes(9, 53,0), HoursMinutes(10, 57,0)] 

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

class HoursMinutes:
    Hour = 0
    Minute = 0 
    Duration = 0
    def __init__(self, hour:int, minute:int, duration: int):
        self.Hour = hour
        self.Minute = minute
        self.Duration = duration #да, теперь длительность хранится здесь. Для полива переделал. 
        
