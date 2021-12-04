import os
import paho.mqtt.client as mqtt

topic = "pi/emer/"
server = "3.90.5.110"

def on_connect(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic+ " "+str(msg.payload.decode('UTF-8')))
    Save_message = int(msg.payload)

    if(Save_message == 1):
        os.system("python ./Desktop/autotexting/Texting.py")
    
client =mqtt.Client()
client.connect(server, 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
client.subscribe("pi/emer/#")
client.loop_forever()
