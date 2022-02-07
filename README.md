# RaspiCam :movie_camera:

Welcome to RaspiCam!
It's an university-motivated project to learn something about the [raspberry pi](https://www.raspberrypi.com/)

## Features

- The camera transfers the image to a website
- On the website you can control the vertical and horizontal camera direction and if a light should be on or off

## Dependecies

- [Apache Webserver](#apache-webserver)
- Python 3
- Python [PiCamera](#picamera)
- Python [Numpy](#numpy)

## Installation

### **Hardware**

- Raspberry Pi
- [Raspberry Pi camera](#setup-camera)
- [Servo Driver HAT](#setup-servo-driver-hat)
- Two servo motors with frame

#### **Setup Camera and Servo Driver Hat**

1. Ensure your Raspberry Pi is turned off
1. Locate the Camera Module port
1. Gently pull up on the edges of the port’s plastic clip
1. Insert the Camera Module ribbon cable; make sure the connectors at the bottom of the ribbon cable are facing the contacts in the port.
1. Push the plastic clip back into place
   ![alt](https://github.com/felixZmn/RaspiCam/blob/main/imgDocu/connect-camera.gif)
1. Insert the Servo Driver HAT modul in the GPIO pins like on the image
   ![alt](https://github.com/felixZmn/RaspiCam/blob/main/imgDocu/servo-driver.jpg)
1. Start up your Raspberry Pi
1. `sudo raspi-config`
1. Set camera to **enable** and then press **finish**
1. Choose Interfacing Options --> I2C --> yes --> press **finish**
1. `sudo reboot`

For more information about the servo driver, click [here](https://www.waveshare.com/wiki/Servo_Driver_HAT)

#### **Setup servo motors with frame**

- Plug in the vertical servo motor in `pin 2`
- Plug in the horizontal servo motor in `pin 1`

![alt](https://github.com/felixZmn/RaspiCam/blob/main/imgDocu/connect-servo-macro.jpeg)
![alt](https://github.com/felixZmn/RaspiCam/blob/main/imgDocu/connect-servo.jpeg)

```
G = Ground
V = Voltage
S = Signal
```

### **Software**

#### Automatic installation with script

##### **Setup with script** (requires apache webserver)

1. Pull repository to respberry pi
2. Change to `~/RaspiCam/scripts`
3. Execute `sh ./update.sh` to update the server and install all dependency's

**Issues**  
Failed to copy files to `/var/www/html`
- Execute `sudo chown pi /var/www/html`

##### **Update.sh**
pull the repository and start setup.sh

##### **setup.sh**
Install python3 and apache2,
then installs all package extern packages,
then copy the website to the webserver folder,

##### **server.sh**
starts the camera and servo server

#### Manual installation

##### **Apache Webserver**

1. `sudo apt update && sudo apt upgrade`
1. `sudo apt install apache2`

To verify that the Apache web server is running correctly on your Raspberry Pi, you can enter the IP address of the Raspberry Pi into a web browser. You should then see the Apache2 Debian default page site.

3. Change diretory to `/var/www/html/`
4. Replace all files inside this folder with the content from `Website (Folder from the Repo)`

If you enter the IP address from the Raspberry Pi into a web browser now, you should see the camera control website

##### **PiCamera**

`pip install picamera`

##### **Numpy**

`pip install numpy`


## Usage

Enter the IP address of your Raspberry Pi in a web browser. This will take you to the camera's control website where you can control it. Now you can monitor your area and receive the current video with your smartphone.

### Launch application automatic
1. Change directory to `~/RaspiCam/scripts`
1. Execute `sh ./server.sh` to start server

### Launch application manual
1. Change directory to `~/RaspiCam/python-scripts`
1. `python server.py`
