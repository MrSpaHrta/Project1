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
        week1_data = self._data.GetWeekData(1)
        week2_data = self._data.GetWeekData(2)
        week3_data = self._data.GetWeekData(3)
        week4_data = self._data.GetWeekData(4)
        self._weeks = [GrowingWeek(week1_data), GrowingWeek(week2_data),GrowingWeek(week3_data),GrowingWeek(week4_data)]
        self._actualWeek = 0

    def IsTimeToWater(self):
        return self._weeks[self._actualWeek].IsTimeToWater()

    def IsTimeToLighting(self, level:int):
        return self._weeks[self._actualWeek].IsTimeToLighting(level)

class GrowingWeek:
    def __init__(self, data):
        self.watering = Watering(data.get("PumpDurations"), data.get("PumpStartHours"), data.get("PumpStartMinutes"))
        self.lighting = Lighting(data)
        self.mixstureUnit = MixstureUnit()

    def IsTimeToWater(self):
        return self.watering.IsTimeToWater()

    def IsTimeToLighting(self, level:int):
        return self.lighting.IsTimeToLigghting(level)

class Watering:   

    _devIsTimeToWater = False

    def __init__(self, durations, startHours, startMinutes):       
        self._startTimes = [HoursMinutes(0, 0, 0)] * len(startHours) #задаём длинну и тип данных массива
              
        try:
            for id in range(len(self._startTimes)):    #заполняем массив
                self._startTimes[id] = HoursMinutes(startHours[id], startMinutes[id], durations[id])
        except RuntimeError as error:
            print(error.args[0])
        except Exception as error:              
            
            print(error.args[0])
            raise error
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
    
    def __init__(self, data):                

        self._lastStart = HoursMinutes(0, 0, 0)  

        self.startHours_1 = [HoursMinutes(0, 0, 0)] * len(data.get("LightLight_1_StartHours"))
        self.startHours_2 = [HoursMinutes(0, 0, 0)] * len(data.get("LightLight_2_StartHours"))
        self.startHours_3 = [HoursMinutes(0, 0, 0)] * len(data.get("LightLight_3_StartHours"))

        for id in range(len(self.startHours_1)):
             self.startHours_1[id] = HoursMinutes(data.get("LightLight_1_StartHours")[id], data.get("LightLight_1_StartMinutes")[id], data.get("LightLight_1_DurationMinutes")[id])

        for id in range(len(self.startHours_2)):
             self.startHours_2[id] = HoursMinutes(data.get("LightLight_2_StartHours")[id], data.get("LightLight_2_StartMinutes")[id], data.get("LightLight_2_DurationMinutes")[id])

        for id in range(len(self.startHours_3)):
             self.startHours_3[id] = HoursMinutes(data.get("LightLight_3_StartHours")[id], data.get("LightLight_3_StartMinutes")[id], data.get("LightLight_3_DurationMinutes")[id])        

        # self._level_0_startTimes = HoursMinutes(data.get("LightLight_1_StartHours"), data.get("LightLight_1_StartMinutes"), data.get("LightLight_1_DurationMinutes"))
        # self._level_1_startTimes = HoursMinutes(data.get("LightLight_2_StartHours"), data.get("LightLight_2_StartMinutes"), data.get("LightLight_2_DurationMinutes"))
        # self._level_2_startTimes = HoursMinutes(data.get("LightLight_3_StartHours"), data.get("LightLight_3_StartMinutes"), data.get("LightLight_3_DurationMinutes"))

    def IsTimeToLigghting(self, level:int):
        now = datetime.now()
        hour = now.hour
        minute = now.minute

        result = False
        
        levelTimes = [HoursMinutes(0, 0, 0) ]
        
        if(level == 0):
            levelTimes = self.startHours_1
        elif(level == 1):
            levelTimes = self.startHours_2
        elif(level == 2):
            levelTimes = self.startHours_3  

        for item in levelTimes:
            if(hour == item.Hour):                
                startMinute = item.Minute
                stopMinute = item.Minute+item.Duration            
                if(startMinute <= minute and stopMinute > minute):
                    result = True
        
        # for item in levelTimes:
        #     if(hour == item.Hour):  
        #         startMinute = item.Minute
        #         stopMinute = item.Minute+self.durationMinutes             
        #         if(startMinute <= minute and stopMinute > minute):
        #             result = True
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
        
