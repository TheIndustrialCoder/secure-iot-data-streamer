import paho.mqtt.client as mqtt
import sensor_simulator as sensor
import time

def publish_sensor_data():
    client = mqtt.Client()
    client.connect("broker.hivemq.com", 1883, 60)

    while True:
        data = sensor.generateSensorData()
        client.publish("mahmoud/test", str(data))
        print("Published:", data)
        time.sleep(5)

if __name__ == "__main__":
    publish_sensor_data()
