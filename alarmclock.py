import datetime
import pyglet
from time import sleep

time_this_moment = datetime.datetime.now()
soundtrack = pyglet.resource.media('woodkid.mp3')
print(time_this_moment)

print ('Day')
day = str(input())
print('Hour')
hour = str(input())
print('Minute')
minute = str(input())

while True:
    time_this_moment = datetime.datetime.now()
    if str(time_this_moment.hour) == hour and str(time_this_moment.minute) == minute and str(time_this_moment.day) == day:
        soundtrack.play()
        break
    sleep(1)
pyglet.app.run()

    
