class GrowingController:
    def __init__(self):
        self._schedule:SceduleItem
    
class SceduleItem:
    def __init__(self):
        self._weeks: GrowingWeek[2]

class GrowingWeek:
    def __init__(self):
        self.watering:Watering
        self.lighting:Lighting
        self.mixstureUnit:MixstureUnit

class HousMinutes:
    def __init__(self):
        self.Hour:int = 0
        self.Minutes:int = 0

class Watering:   
    def __init__(self):
        self.durationSeconds:int = 180
        self._startTimes:HousMinutes[0]

class Lighting:
    def __init__(self):
        self.durationSeconds:int = 180
        self._startTimes:HousMinutes[0]

class MixstureUnit:
    pass