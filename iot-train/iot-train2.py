#!/usr/bin/python3
from traincontrol import *
import sys, time, threading
from bottle import Bottle, route, request, response, template, static_file

app = Bottle()

# Change IPADDRESS if access is required from another computer
IPADDRESS = ''
PORT = 8080
# Where the files are stored
DOCUMENT_ROOT = '/home/pi/iot-train'

# public files
# *** WARNING ANYTHING STORED IN THE PUBLIC FOLDER WILL BE AVAILABLE TO DOWNLOAD
@app.route ('/public/<filename>')
def server_public (filename):
    return static_file (filename, root=DOCUMENT_ROOT+"/public")

@app.route ('/')
def server_home ():
    return static_file ('index.html', root=DOCUMENT_ROOT+"/public")

@app.route ('/train2')
def server_home ():
    return static_file ('train2.html', root=DOCUMENT_ROOT+"/public")


@app.route ('/control')
def control_train():
    getvar_dict = request.query.decode()
    speed = int(request.query.speed)
    train = int(request.query.train)
    direction = int(request.query.direction)
    if (speed >=0 and speed <= 10 and direction >= -1 and direction <= 1 and train >=0 and train <= 1):
        command_speed = speed/10
        train_set_speed(command_speed, train, direction)
        return 'Speed for '+str(train+1) + ' is '+str(speed) + " direction " +str(direction)
    else:
        return 'Invalid command'


saved_time = time.time()

#app.run(host=IPADDRESS)
bottle_thread = threading.Thread(target=app.run, kwargs=dict(host=IPADDRESS, port=PORT, debug='True'))
bottle_thread.daemon = True
bottle_thread.start()
while (True):
    #if (saved_time + 5 < time.time()):
    #    saved_time = time.time()
    #    print ("Testing")
    #    train_set_speed(0, 0, 0)
    #time.sleep (5)
    if (check_reed (0, 0)):
        print ("Reed switch 0 triggered")