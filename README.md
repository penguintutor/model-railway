# model-railway
Improved version of the Raspberry Pi Model Railway control


## iot-train

The IOT train directory provides a way to control a model railway using a Raspberry Pi and a web interface. 
This can be used with a mobile phone to allow control of the railway.

### iot-train.py

The iot-train.py executable is the current version. It provides control for one track with web control.

### iot-train2.py

The iot-train2.py executable is a development version to allow automation alongside the web control. 
This is currently under development.

## Future development

These are still under development at the moment. Future versions may work differently.

## Reverse Proxy option (WiFi unable to connect)

Depending upon your WiFi setup there may be problems when the Raspberry Pi and controller (eg. Phone) are both connected to WiFi. The problem I had is that the phone may switch between 2.5GHz and 5GHz network, when it did it would be unable to connect to the Raspberry Pi. 

I overcame this problem by using a Reverse Proxy which was installed on a different Raspberry Pi which was physically connected to the network. For more details about using a Raspberry Pi as a Reverse Proxy see [Nginx Reverse Proxy on a Raspberry Pi](http://www.penguintutor.com/projects/nginx-reverse-proxy)



## More information

For more information see [Model Railway Projects on Penguintutor.com](http://www.penguintutor.com/projects/model-railway)