import ADS1115
import time


ads = ADS1115.ADS1115()  #0x48

# чистая вода DTS [ppm] = 445 
# чистая вода EC (удельная электропроводность) [микросименс/см]  = 649
# k (коэфициент) = 0,68 [445/649=0.68]

# TDS = k * EC
temps = [0]

while True:

    volt0 = ads.readADCSingleEnded(0)

    volt1 = ads.readADCSingleEnded(1)

    volt2 = ads.readADCSingleEnded(2)

    volt3 = ads.readADCSingleEnded(3)

    # TDS = int((4400/5000)*volt1)
    k = 0.68

    TDS_0 = int(k*volt0)
    TDS_1 = int(k*volt1)
    PH = int((14/5000)*volt2)
    # T = int(((24/5000)*volt3))
    T = int(((100/5000)*volt3))
    temps.append(T)

    averageTemp = 0
    summT = 0
    for i in temps:
        summT = summT + i

    averageTemp = summT/ len(temps)   

    print(f"TDS_0: {TDS_0}, TDS_1: {TDS_1}, PH: {PH}, Temperature: {T}")
    # print(f"volt0: {volt0}, volt1: {volt1}, volt2: {volt2}, volt3: {volt3}")
    
    time.sleep(3)