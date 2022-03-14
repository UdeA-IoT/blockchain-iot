import paho.mqtt.client as mqtt
import time

# Variables de la aplicacion
BROKER_IP = "127.0.0.1"
TOPIC = "A/a1"
mess = "----------------------------------"

# 1. Creacion de la isntanca del cliente
CLIENT_ID = "officeLamp"
mqtt_client=mqtt.Client(client_id=CLIENT_ID)

# 2. Incovacion del metodo connect
mqtt_client.connect(BROKER_IP, 1883, 60)

# 3. Llamando el loop para mantener el flujo de trafico de red en el broker
# 4. No se llevo a cabo en este caso.
mqtt_client.loop_start()
mqtt_client.publish(TOPIC,mess)
mqtt_client.loop_stop()
