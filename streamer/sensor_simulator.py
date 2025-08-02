import random

def generateSensorData():
    return {
        "temperature": round(random.uniform(-10.0, 40.0), 2),
        "humidity": round(random.uniform(0.0, 100.0), 2),
    }

if __name__ == "__main__":
    data = generateSensorData()