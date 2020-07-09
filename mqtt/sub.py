import paho.mqtt.client as mqtt
import os, django
from datetime import datetime, date

os.environ["DJANGO_SETTINGS_MODULE"] = 'smart_library.settings'
django.setup()
from django.conf import settings
from library.models import *

# логирование
#def on_log(client, userdata, level, buf):
#    print("log: ",buf)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print('Connected!')
    client.subscribe([
        ('library/device/reader',2)
        #('library/device/display',2)
        #('test',2)
    ])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    message = str(msg.payload).rstrip("'").lstrip("b'").split(',')
    print(message)
    try:
        user = User.objects.get(pk = int(message[0])) #преобразовать в кортеж
        book = Book.objects.get(pk = int(message[1]))
    except Exception as e:
        return e.msg
    user.books.append(book)
    user.save()
    '''
    try:  # object not found
        user.save()
    except Exception as e:
        return e.msg
    else:
        return 'good'
    '''
    book.date_start.append(date.today)
    book.date_end.append(return_date_time)
    book.save()


client = mqtt.Client()
#client.on_log=on_log
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('library_user', 'makerspace111')
client.connect('localhost')

client.loop_forever()
