# Sixfab_RPi_XBee_Library
It is repository of python library for Raspberry Pi XBee Shield.

# Library Installation
## Manual Installation
```
git clone https://github.com/sixfab/Sixfab_RPi_XBee_Shield.git
cd Sixfab_RPi_XBee_Shield
sudo python3 setup.py install
```

## Test
Enable `serial_hw` and `I2C` interfaces by following instructions below:  
1. Run `sudo raspi-config`
2. Select `5 Interfacing Options`
3. For `P6 Serial`
    * Disable `Login shell to be accessible over serial`
    * Enable `Serial port hardware`
4. Finish
5. Reboot
6. It's done.
```
cd sample
python3 receiver.py  #for receiving data
python3 sender.py  #for sending data
```

# Examples
** [receiver](https://github.com/sixfab/Sixfab_RPi_XBee_Shield/blob/master/sample/receiver.py)  
** [sender](https://github.com/sixfab/Sixfab_RPi_XBee_Shield/blob/master/sample/sender.py)

# Tutorials will be here (very soon)

# Pinout
![Pinout Schematic](https://sixfab.com/wp-content/uploads/2018/10/rpi_xbee_shield_pinout.png)

# Attention
! All data pins work with 3.3V reference. Any other voltage level should harm your hat or RPI.

# Layout
![Layout](https://sixfab.com/wp-content/uploads/2018/10/rpi_xbee_shield_layout-1.png)

