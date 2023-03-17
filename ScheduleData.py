# from GrowingSchedule import HousMinutes
import json

class DataContainer:  
# технологическая карта                                                                                                                                                                                                                                                                                 
    _growingWeekNomber = 0


    Week1data = {"LightLight_1_DurationMinutes": [1,1,1],
            "LightLight_1_StartHours": [12,12,12],
            "LightLight_1_StartMinutes": [25,28,31],                    
                
            "LightLight_2_DurationMinutes": [1,1,1],
            "LightLight_2_StartHours": [12,12,12],
            "LightLight_2_StartMinutes": [25,28,31],                    
                
            "LightLight_3_DurationMinutes": [1,1,1],
            "LightLight_3_StartHours": [12,12,12],
            "LightLight_3_StartMinutes": [25,28,31],                    
                
            "PumpDurations": [1,1,1],
            "PumpStartHours": [12,10,10],
            "PumpStartMinutes": [37,39,41],

            "TemperatureMin": 19,
            "TemperatureMax": 22,
            "HunidityMin": 50,
            "HunidityMax": 90,

            "Co2Max": 800




    }
    Week2data = {"LightLight_1_DurationMinutes": [1,1,1],
            "LightLight_1_StartHours": [1,1,1],
            "LightLight_1_StartMinutes": [29,1,1],                    
                
            "LightLight_2_DurationMinutes": [1,1,1],
            "LightLight_2_StartHours": [1,1,1],
            "LightLight_2_StartMinutes": [29,1,1],                    
                
            "LightLight_3_DurationMinutes": [1,2,3],
            "LightLight_3_StartHours": [1,1,1],
            "LightLight_3_StartMinutes": [29,1,1],                    
                
            "PumpDurations": [1,1,1],
            "PumpStartHours": [1,1,1],
            "PumpStartMinutes": [1,1,1]
    }
    Week3data = {"LightLight_1_DurationMinutes": [1,1,1],
            "LightLight_1_StartHours": [1,1,1],
            "LightLight_1_StartMinutes": [29,1,1],                    
                
            "LightLight_2_DurationMinutes": [1,1,1],
            "LightLight_2_StartHours": [1,1,1],
            "LightLight_2_StartMinutes": [29,11,1],                    
                
            "LightLight_3_DurationMinutes": [1,1,1],
            "LightLight_3_StartHours": [1,1,1],
            "LightLight_3_StartMinutes": [29,1,1],                    
                
            "PumpDurations": [1],
            "PumpStartHours": [1],
            "PumpStartMinutes": [1]
    }
    Week4data = {
            "LightLight_1_DurationMinutes": [1,1,1],
            "LightLight_1_StartHours": [1,1,1],
            "LightLight_1_StartMinutes": [29,1,1],                    
                
            "LightLight_2_DurationMinutes": [1,1,1],
            "LightLight_2_StartHours": [1,1,1],
            "LightLight_2_StartMinutes": [29,1,1],                    
                
            "LightLight_3_DurationMinutes": [1,1,1],
            "LightLight_3_StartHours": [11,1,1],
            "LightLight_3_StartMinutes": [29,1,1],                    
                
            "PumpDurations": [1],
            "PumpStartHours": [1],
            "PumpStartMinutes": [1]
    }

    # LightLevel_0_startTimes = [HousMinutes(9, 51), HousMinutes(10, 55)]
    # LightLevel_1_startTimes = [HousMinutes(9, 52), HousMinutes(10, 56)]
    # LightLevel_2_startTimes = [HousMinutes(9, 53), HousMinutes(10, 57)] 

    def Save(self):       
        for item in range(4):
            with open(f"Data/week_{item+1}_data_file.json", "w") as write_file:
                if(item == 0):
                    json.dump(self.Week1data, write_file, indent=4) 
                if(item == 1):
                    json.dump(self.Week2data, write_file, indent=4)
                if(item == 2):
                    json.dump(self.Week3data, write_file, indent=4)
                if(item == 3):
                    json.dump(self.Week4data, write_file, indent=4) 

        with open("Data/currentWeekId.json", "w") as week_file:  
            json.dump(self._growingWeekNomber, week_file, indent=4)          

    def GetWeekData(self, week:int):
        with open(f"Data/week_{week}_data_file.json", "r") as write_file:            
            return json.load(write_file) 

    def GetWeekNomber(self):
        return self._growingWeekNomber

    def Load(self):
        for item in range(4):
            with open(f"Data/week_{item}_data_file.json", "r") as write_file:
                if(item == 0):
                    self.Week1data = json.load(write_file) 

        with open("Data/currentWeekId.json", "r")as week_file:
            data = json.load(week_file) 
            self._growingWeekNomber = data.get("_growingWeek")

if __name__ == '__main__':    
    container = DataContainer()
    container.Save()   
    
    print(f"DataContainer Saved")         

    







