# from GrowingSchedule import HousMinutes
import json

class DataContainer:  
# технологическая карта                                                                                                                                                                                                                                                                                 
    
    _day = 1


    Week1data = {"LightLight_1_DurationMinutes": 1,
            "LightLight_StartHour": 12,
            "LightLight_StartMinute": 20, 
                
            "PumpDuration": 1,
            "PumpStartHours": 12,
            "PumpStartMinutes": 21,

            "TemperatureMin": 19,
            "TemperatureMax": 22,
            "HunidityMin": 50,
            "HunidityMax": 90,

            "Co2Max": 800
    }

    Week2data = {"LightLight_1_DurationMinutes": 1,
            "LightLight_StartHour": 12,
            "LightLight_StartMinute": 20, 
                
            "PumpDuration": 1,
            "PumpStartHours": 12,
            "PumpStartMinutes": 21,

            "TemperatureMin": 19,
            "TemperatureMax": 22,
            "HunidityMin": 50,
            "HunidityMax": 90,

            "Co2Max": 800
    }
    Week3data = {"LightLight_1_DurationMinutes": 1,
            "LightLight_StartHour": 12,
            "LightLight_StartMinute": 20, 
                
            "PumpDuration": 1,
            "PumpStartHours": 12,
            "PumpStartMinutes": 21,

            "TemperatureMin": 19,
            "TemperatureMax": 22,
            "HunidityMin": 50,
            "HunidityMax": 90,

            "Co2Max": 800
    }
    Week4data = {"LightLight_1_DurationMinutes": 1,
            "LightLight_StartHour": 12,
            "LightLight_StartMinute": 20, 
                
            "PumpDuration": 1,
            "PumpStartHours": 12,
            "PumpStartMinutes": 21,

            "TemperatureMin": 19,
            "TemperatureMax": 22,
            "HunidityMin": 50,
            "HunidityMax": 90,

            "Co2Max": 800
    }
    

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

    def GetDayNomber(self):
        return self._day

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

    







