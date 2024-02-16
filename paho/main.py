import paho.mqtt.client as mqtt
import time

def sample_publish_start():
    mqtt_client = mqtt.Client("paho_publisher")
    mqtt_client.username_pw_set("user1","user1")
    mqtt_client.connect("localhost", port=1883)
    for i in range(100):
        time.sleep(0.1)
        mqtt_client.publish("/root/test/helloworld", "hello, world! from paho_mqtt publisher")

def sample_subscribe_start():
    mqtt_client = mqtt.Client("paho_subscriber")
    mqtt_client.username_pw_set("user1","user1")
    mqtt_client.connect("localhost", port=1883)
    mqtt_client.subscribe("/root/test/helloworld")
    mqtt_client.on_message = lambda s, u, msg: print(msg.payload.decode())
    mqtt_client.loop_forever()

if __name__ == "__main__":
    selection = input("1 = publish fire, 2 = subscribe start")
    if selection == '1':
        sample_publish_start()
    else:
        sample_subscribe_start()
