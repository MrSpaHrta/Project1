from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def index():
    temperatureFile = open('/home/pi/Documents/Project1/Data/temperature.txt', 'r')
    temperature = temperatureFile.readline()
    temperatureFile.close()
    return render_template('index.html', temperatureValue = temperature)

def Start(): 
    app.run(host = "0.0.0.0", port=5000, debug=True)
    

        

if __name__ == "__main__":   
    
    Start()