# model-railway
Improved version of the Raspberry Pi Model Railway control

## iot-train

The IOT train directory provides a way to control a model railway using a Raspberry Pi and a web interface.
This can be used with a mobile phone to allow control of the railway.

## Hardware requirements

This is designed for a analogue model railway with DC motors. It could also be used to control other DC motors.

A H-Bridge motor controller is required. A L298N motor controller is recommended, although other controllers can be used depending upon your model railway power requirements.

You will also need a suitable DC power supply. Note if you have a power supply "wallwart" with your existing train set then it may be AC, in which case you would also need a full-bridge rectifier.
Instead I recommend a 12V DC power supply with sufficient current for all your trains (eg. a 2A should be sufficient for running two OO/HO trains). For larger guage model railways then one with a higher voltage and current may be required. I used a 19V laptop power supply for my outdoor railway, but please check you don't exceeded the maximum voltage for your models.

## Wiring

The following pins should be used for connecting to the Raspberry Pi (or updated in traincontrol.py)


| Function   | GPIO numbers   | Physical pin   | Comments                |
| :---       |    :----:      |    :----:      | :---                    |
| Train 1    |    17,18       |    11,12       |                         |
| Train 2    |    22,23       |    15,16       |                         |
| Reed 1     |      4         |      7         | Reed switch for train 1 |
| Reed 2     |      3         |      5         | Reed switch for train 2 |

Each train has 2 gpio numbers. The first is for forward, the second is for reverse. These can be switched depending upon how the motor is wired to the track.

The reed switches provide automated stopping at the station. These are not used with iot-train.py.

![Wiring diagram for Raspberry Pi and L289N motor controller for model railway automation](http://www.penguintutor.com/projects/images/model-railway-wiring.png)

## Installation

The files should downloaded to a directory /opt/iot-train

The directory will need to be created as root. You can then change ownership to your normal username so that root permission is not required.

    sudo mkdir /opt/iot-train
    sudo chown <username>: /opt/iot-train

Transfer all the files into that directory, including the public directory.

### iot-train.py

The iot-train.py executable is the current version. It provides control for one track with web control.

It can be run using
    python3 iot-train.py

### iot-train2.py

The iot-train2.py executable is a development version to allow automation alongside the web control.
This is currently under development.

## Future development

These are still under development at the moment. Future versions may work differently.

## Reverse Proxy option (WiFi unable to connect)

Depending upon your WiFi setup there may be problems when the Raspberry Pi and controller (eg. Phone) are both connected to WiFi. The problem I had is that the phone may switch between 2.5GHz and 5GHz network, when it did it would be unable to connect to the Raspberry Pi. This depends upon your particular Wi-Fi router whether it can provide direct connections between different WiFi frequencies.

One option is to physically connect the Raspberry Pi using an Ethernet cable. If that is not possible an alternative is uing another Raspberry Pi as a Reverse Proxy to provide routing.

The Reverse Proxy should be installed on a different Raspberry Pi which is physically connected to the network using Ethernet. For more details about using a Raspberry Pi as a Reverse Proxy see [Nginx Reverse Proxy on a Raspberry Pi](http://www.penguintutor.com/projects/nginx-reverse-proxy)


## More information

For more information see [Model Railway Projects on Penguintutor.com](http://www.penguintutor.com/projects/model-railway)