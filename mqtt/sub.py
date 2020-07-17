import paho.mqtt.client as mqtt
import os, django
from datetime import datetime, date, timedelta

os.environ["DJANGO_SETTINGS_MODULE"] = 'smart_library.settings'
django.setup()

from django.conf import settings
from library.models import *


# логирование
#def on_log(client, userdata, level, buf):
#    print("log: ",buf)


# канал, для связи с устройством
def on_connect(client, userdata, flags, rc):
    client.subscribe([
    	('library/device/reader',2)
        #('library/device/display',2)
    ])


# получение данных с устройства
# python -m mqtt.sub	
def on_message(client, userdata, msg):
	message = str(msg.payload).rstrip("'").lstrip("b'").split(',')
	print(message)
	try:
		user = User.objects.get(user_id = message[0]) 
		book = Book.objects.get(book_id = message[1])
		#print(user)
		#print(book)
	except Exception:
		client.publish('library/device/display', "Error :(", qos=2)
		client.publish('library/device/display', "showCardWaitScreen", qos=2)
	else:
		if not UserBooks(book_key=book, user_key=user).exists():
			user_book = UserBooks(book_key=book, user_key=user, date_start = date.today(), date_end = return_date_time())
			user_book.save()
			client.publish('library/device/display', "Success!", qos=2)
			client.publish('library/device/display', "showCardWaitScreen", qos=2)


client = mqtt.Client()
#client.on_log=on_log
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('library_user', 'makerspace111')
client.connect('localhost')

client.loop_forever()
