# GenesisPicoPad
Project where I connect a Sega Genesis controller to a Pi Pico

# Motivation
I'm a programmer and game developer, with a few titles released on the market. Retro games are my main inspiration, and I'm passionate about gamepads, keeping a diverse collection.</br>

I also enjoy working on small electronics projects. Recently, I started a new project, finally putting my plans into practice.</br>

My personal website with the games I've released on the market, PC and Consoles </br>
https://guimaraf.github.io/projects.html

# Description
I'm using an original Sega Genesis controller connected to a DB9 female interface, which in turn is connected to a Raspberry Pi Pico. With Python, I'm capturing the gamepad's inputs and converting them into keyboard commands, allowing them to be used in games and emulators on the PC. I haven't yet tested the configuration on other devices.

# Connecting DB9 to the Pi Pico
Guide to connections on the board </br>
Separating the connections to make it easier to connect to the Pi Pico without a protoboard </br>

Pin 1 (Up) -> GPIO 2 </br>
Pin 2 (Down) -> GPIO 4 </br>
Pin 3 (Left) -> GPIO 6 </br>
Pin 4 (Right) -> GPIO 8 </br>
Pin 5 (VCC) is not connected to Pico </br>
Pin 6 (Button B) -> GPIO 10 </br>
Pin 7 (Select) -> GPIO 14 </br>
Pin 8 (GND) -> GND of the Raspberry Pi Pico
Pin 9 (Button A / Start) -> GPIO 12 </br>

# What is CircuitPython?
CircuitPython is a simplified version of Python, designed to make programming microcontrollers easier. Developed by Adafruit, it is aimed at beginners and allows them to create electronic projects easily, with a focus on education and accessibility. </br>
https://circuitpython.org </br>

Download CircuitPython for Pi Pico </br>
https://circuitpython.org/board/raspberry_pi_pico/

Learn more about Circuitpython with the official documentation </br>
https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython
</br>

You can use the code editor of your choice and then simply save the file to the CircuitPython virtual disk so that it works automatically.

# Used libraries
board </br>
digitalio </br>
time </br>
usb_hid </br>
adafruit_hid </br>
</br>

### Dependencies

The `adafruit_hid` library is not included natively in CircuitPython. Therefore, you will need to add it manually to the `lib` folder on the CircuitPython virtual disk.

### Installation

1. Download the `adafruit_hid` library from the following link:  
   [Download library](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases/tag/6.1.1).  
   In this project, I'm using the file `“adafruit-circuitpython-hid-9.x-mpy-6.1.1.zip”`.

2. Extract the contents of the zip file and copy the `adafruit_hid` folder to the `lib` directory on the CircuitPython virtual disk.

### Useful links

- [Official repository of the adafruit_hid library](https://github.com/adafruit/Adafruit_CircuitPython_HID)

# Materials used in the project
- Raspberry pi pico development board with soldered pins
- Sega Mega Drive (Genesis) controller
- Db9 Female Connector With Terminal Block
- Jumper Cable 20Cm Male X Female
</br>

![Alt text](/img/pipico.png?raw=true "Raspberry Pi Pico")

![Alt text](/img/genesis6pad.png?raw=true "Sega Genesis 6 buttons")

![Alt text](/img/db9femaleconnector.png?raw=true "DB9 female connector")

![Alt text](/img/pipicopins.png?raw=true "Raspberry Pi Pico Diagram")

</br>