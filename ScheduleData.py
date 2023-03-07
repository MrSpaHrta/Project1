# from GrowingSchedule import HousMinutes
import json

class DataContainer:                                                                                                                                                                                                                                                                                   
    
    Week1data = {"LightLight_1_DurationMinutes": [1,2,3],
            "LightLight_1_StartHours": [11],
            "LightLight_1_StartMinutes": [29],                    
                
            "LightLight_2_DurationMinutes": [1,2,3],
            "LightLight_2_StartHours": [11],
            "LightLight_2_StartMinutes": [29],                    
                
            "LightLight_3_DurationMinutes": [1,2,3],
            "LightLight_3_StartHours": [11],
            "LightLight_3_StartMinutes": [29],                    
                
            "PumpDurations": [1],
            "PumpStartHours": [10,10,10],
            "PumpStartMinutes": [37,39,41]
    }
    Week2data = {"LightLight_1_DurationMinutes": [1,2,3],
            "LightLight_1_StartHours": [11],
            "LightLight_1_StartMinutes": [29],                    
                
            "LightLight_2_DurationMinutes": [1,2,3],
            "LightLight_2_StartHours": [11],
            "LightLight_2_StartMinutes": [29],                    
                
            "LightLight_3_DurationMinutes": [1,2,3],
            "LightLight_3_StartHours": [11],
            "LightLight_3_StartMinutes": [29],                    
                
            "PumpDurations": [1],
            "PumpStartHours": [1],
            "PumpStartMinutes": [1]
    }
    Week3data = {"LightLight_1_DurationMinutes": [1,2,3],
            "LightLight_1_StartHours": [11],
            "LightLight_1_StartMinutes": [29],                    
                
            "LightLight_2_DurationMinutes": [1,2,3],
            "LightLight_2_StartHours": [11],
            "LightLight_2_StartMinutes": [29],                    
                
            "LightLight_3_DurationMinutes": [1,2,3],
            "LightLight_3_StartHours": [11],
            "LightLight_3_StartMinutes": [29],                    
                
            "PumpDurations": [1],
            "PumpStartHours": [1],
            "PumpStartMinutes": [1]
    }
    Week4data = {"LightLight_1_DurationMinutes": [1,2,3],
            "LightLight_1_StartHours": [11],
            "LightLight_1_StartMinutes": [29],                    
                
            "LightLight_2_DurationMinutes": [1,2,3],
            "LightLight_2_StartHours": [11],
            "LightLight_2_StartMinutes": [29],                    
                
            "LightLight_3_DurationMinutes": [1,2,3],
            "LightLight_3_StartHours": [11],
            "LightLight_3_StartMinutes": [29],                    
                
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
                    json.dump(self.Week1data, write_file) 
                if(item == 1):
                    json.dump(self.Week2data, write_file)
                if(item == 2):
                    json.dump(self.Week3data, write_file)
                if(item == 3):
                    json.dump(self.Week4data, write_file)   

    def LoadWeek(self, week:int):
        with open(f"Data/week_{week}_data_file.json", "r") as write_file:            
            return json.load(write_file)  

    def Load(self):
        for item in range(4):
            with open(f"Data/week_{item}_data_file.json", "r") as write_file:
                if(item == 0):
                    self.Week1data = json.load(write_file) 

if __name__ == '__main__':    
    container = DataContainer()
    container.Save()   
    
    print(f"DataContainer Saved")         

    







