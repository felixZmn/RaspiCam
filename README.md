# RaspiCam :movie_camera:
Welcome to RaspiCam!
It's an university-motivated project to learn something about the [raspberry pi](https://www.raspberrypi.com/)
## Features
## Dependecies
## Installation
### **Hardware**
* Raspberry Pi
* [Raspberry Pi camera](#setup-camera)
* [Servo Driver HAT](#setup-servo-driver-hat)
* Two servo motors with frame

#### **Setup Camera**
1. Ensure your Raspberry Pi is turned off
1. Locate the Camera Module port
1. Gently pull up on the edges of the port’s plastic clip
1. Insert the Camera Module ribbon cable; make sure the connectors at the bottom of the ribbon cable are facing the contacts in the port.
1. Push the plastic clip back into place
![alt](https://github.com/felixZmn/RaspiCam/blob/main/imgDocu/connect-camera.gif)
1. Start up your Raspberry Pi
1. `sudo raspi-config`
1. Set camera to **enable** and then press **finish**
1. `sudo reboot`

#### **Setup Servo Driver HAT**
1. Ensure your Raspberry Pi is turned off
1. Insert the Servo Driver HAT modul in the GPIO pins like on the image
![alt](https://github.com/felixZmn/RaspiCam/blob/main/imgDocu/servo-driver.jpg)
1. Start up your Raspberry Pi
1. `sudo raspi-config`
1. Choose Interfacing Options --> I2C --> yes --> press **finish**
1. `sudo reboot`

For more information about the servo driver, click [here](https://www.waveshare.com/wiki/Servo_Driver_HAT) 


### **Setup servo motors with frame**
* Plug in the vertical servo motor in `pin 0`
* Plug in the vertical servo motor in `pin 1`

```
G = Ground
V = Voltage
S = Signal
```
### **Software**
#### **Apache Webserver**
1. `sudo apt update && sudo apt upgrade`
1. `sudo apt install apache2`

To verify that the Apache web server is running correctly on your Raspberry Pi, you can enter the IP address of the Raspberry Pi into a web browser. You should then see the Apache2 Debian default page site.

3. Change diretory to `/var/www/html/`
4. Replace all files inside this folder with the content from `Website (Folder from the Repo)`

If you enter the IP address from the Raspberry Pi into a web browser now, you should see the camera control website 

## Usage
