import paho.mqtt.client as mqtt
import os, django
#from django.utils import timezone
from datetime import datetime, date

os.environ["DJANGO_SETTINGS_MODULE"] = 'smart_library.settings'
django.setup()
from django.conf import settings
from library.models import *

# логирование, опционально
#def on_log(client, userdata, level, buf):
    # print("log: ",buf)
#    pass

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print('Connected!')
    client.subscribe([
        ('library/device0/readers',2),
        #('library/device1/display')
        ('test',2)
    ])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    user = User.objects.get(id = int(msg.payload))
    book = Book.objects.get(id= int(msg.payload))
    user.books.append(book)
    user.save()
    book.date_start.append(date.today)
    book.date_end.append(date.today)
    book.save()

    #data = str(msg.payload).rstrip("'").lstrip("b'").split(',')
    # print(msg.topic," ",data)
    # print('timestamp', msg.timestamp)
    # print('state', msg.state)
    # print('properties', msg.properties)
    # print('info', msg.info)
    #print('payload', msg.payload)


client = mqtt.Client()
#client.on_log=on_log
client.on_connect = on_connect
client.on_message = on_message

#client.username_pw_set(settings.MQTT['USER'], settings.MQTT['PASSWORD'])
client.username_pw_set('vard0ni', 'karat1st')
client.connect('localhost')

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()
