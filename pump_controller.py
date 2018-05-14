import paho.mqtt.client as mqtt
import time,json

# Configuration values
pump_controller_id = 1
pump_id = 1
response_delay = 3

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("pumpcontroller/" + str(pump_controller_id) + "/" + str(pump_id))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("topic:" + msg.topic + " payload:"+str(msg.payload))
    print("Replying message ...")

    # Get sender
    message_json = json.loads(msg.payload)
    print(message_json['id'])
    print(message_json['sender'])

    # Simulate operation here
    time.sleep(response_delay)
    print("Done!")

    # Generate reply
    reply_json = {}
    reply_json['id'] = message_json['id']
    reply_json['status'] = 'OK'

    # Generate response
    (rc, mid) = client.publish(message_json['sender'], msg.topic + " terminated")



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
