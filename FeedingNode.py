import ADS1115
import time
import board

ads = ADS1115.ADS1115()

while True:

    volt0 = ads.readADCSingleEnded()

    volt1 = ads.readADCSingleEnded(1)

    volt2 = ads.readADCSingleEnded(2)

    volt3 = ads.readADCSingleEnded(3)

    TDS = int((4400/5000)*volt0)
    PH = int((14/5000)*volt1)
    T = int(((100/5000)*volt2)-20)

    print(TDS, PH, T)
    
    time.sleep(0.1)