from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def index():
    temperatureFile = open('/home/pi/Documents/Project1/Data/temperature.txt', 'r')
    temperature = temperatureFile.readline()
    temperatureFile.close()
    humidityFile = open('/home/pi/Documents/Project1/Data/humidity.txt', 'r')
    humidity = humidityFile.readline()
    humidityFile.close()
    co2File = open('/home/pi/Documents/Project1/Data/CO2.txt', 'r')
    co2 = co2File.readline()
    co2File.close()
    return render_template('index.html', temperatureValue = temperature, humidityValue = humidity, co2Value = co2)

def Start(): 
    app.run(host = "0.0.0.0", port=5000, debug=True)
    

        

if __name__ == "__main__":   
    
    Start()