import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("log: "+buf)
    
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print('connected OK')
    else:
        print('Bad connection Returned code=',rc)
        
def on_disconnect(client, userdata, flags, rc=0):
    print('Disconnected result code '+str(rc))
    
def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8","ignore"))
    print("Message received ",m_decode)

broker = "127.0.0.1"

client = mqtt.Client("python1")  #Create new instance

client.on_connect = on_connect #bind call back function
client.on_disconnect = on_disconnect
client.on_log = on_log
client.on_message = on_message

print("Connecting to broker ",broker)
client.connect(broker) #Connect to broker (mosquitto)
client.loop_start()

choice = 'T'
while True:
    if choice == 'F':
        break
    topic = input("Enter topic to subscribe ")
    client.subscribe(topic)
    choice = input("Enter T to continue else F ")

client.publish("Hello World!","This is hello world equivalent of MQTT")
a = 'B'
num = 1213
client.publish("Character Test",a)
client.publish("Numbers",num)
time.sleep(4)
client.loop_stop()
client.disconnect()
