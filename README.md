# DellDisplayManagerLite


Linux App with shortcut to easy select preset, entry, and power off a DELL monitor
![alt text](https://raw.githubusercontent.com/ManTreff/DellDisplayManagerLite/main/delldisplaymanagerlitelinux.png)

Because Dell does not give us a Linux version of Dell display manager I wrote this code.
There is already some Windows management app in Linux so this app only manage entry and presets of my Dell monitor with shortcuts.

This code is python and GTK3,

it's based on DDCUTIL:
https://www.ddcutil.com/
https://www.ddcutil.com/config_steps/

this page is very usefull and simple to understand how to use ddcutil:
https://blog.tcharles.fr/ddc-ci-screen-control-on-linux/

Before use this app,
you have to:
-check / install python (https://python-gtk-3-tutorial.readthedocs.io/en/latest/install.html#prebuilt-packages)
-check intsall GTK3 libraries (https://zestedesavoir.com/tutoriels/870/des-interfaces-graphiques-en-python-et-gtk/)

-install ddcutil (https://blog.tcharles.fr/ddc-ci-screen-control-on-linux/ )

-dentify your monitor info : in terminal: ddcutil detect
-find the bus number: #    I2C bus:             /dev/i2c-8 (for me it's 8) (if you dont specify bus number ddcutil works in detect mode and send commands to monitor take a long long time)
-look for features of the monitor and their command code:  in terminal: ddcutil capabilities --bus=8 (8 in my case)
-adapt the code for your monitor:

these ones are for my Model:  DELL U3421WE /  Product code: 41345  (0xa181)

Confort view: ddcutil setvcp F0 0x0C 
Game: ddcutil setvcp DC 0x05 
Standard : ddcutil setvcp DC 0x00 

Switch to usb: ddcutil setvcp 60 0x1b 
power off: ddcutil setvcp D6 0x05 

This app, had only this 5 buttons, but it's simple to add yours.

This is my first code with python / gtk, and I've not enough time to ehance it, so forgive me if it's a bit clubky.





