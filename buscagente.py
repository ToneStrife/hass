import bluetooth
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

broker = '192.168.1.5'
loc_dani = 'hass/dani/localizacion'
loc_ana = 'hass/ana/localizacion'

client = mqtt.Client("hass-client-vm42")
client.connect(broker)
#client.loop_start()

result = bluetooth.lookup_name('80:BE:05:69:BE:41', timeout=15)
if (result != None):
	client.publish(loc_dani, 'home', retain=True)
else:
	client.publish(loc_dani, 'not_home', retain=True)
result = bluetooth.lookup_name('A4:9A:58:55:6E:A2', timeout=15)
if (result != None):
	client.publish(loc_ana, 'home', retain=True)
else:
	client.publish(loc_ana, 'not_home', retain=True)


client.disconnect()
