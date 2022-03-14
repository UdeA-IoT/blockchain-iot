import paho.mqtt.client as mqtt
import time

client = new MqttClient("tcp://localhost:1883", "XXXX");
client.connect();
MqttMessage message = new MqttMessage();
message.setPayload("Hello World".getBytes());
client.publish("A/a1", message);
client.disconnect();