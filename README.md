# Lighting Timer Project for Pi Pico

This project will allow you to create an smart lighting system which can light any space based on your movement in the room.  The idea is to save electricity thats not needed when you are not active in the space, such as a garage.  If you frequently enter the space and sit still for long periods of time, you may want to turn the timer up to a much higher number of seconds such as 900 (15 minutes) or 1800 (30 minutes) to not be annoyed as often when the lights shut off.  This project could work well for a security lighting system wired outside of the 4 corners of your garage or house, for example, but at that point, you might as well just buy 4 security lights, unless you really love this kind of DIY project.

The project is a basic simple timer system written in MicroPython, so once you enter the room, the lights turn on for a specified time, and turn off after the timer counts down, unless further movement is detected.

It uses a Raspberry Pi Pico and a SB Components Pi Relay board, and up to 4 low cost PIR sensors to be mounted around the lights.  It requires high voltage wiring from the lights and PIR sensors back to a central enclosure where you will safely mount and wire all AC wiring and electronics, up to NEC code or whatever your regions electrical code requires!

WARNING: This project requires AC electrical wiring knowledge and skills, do NOT attempt if you are completely new to electronics, touching AC wires could potentially kill you or burn your house down!

## Project Requirements:

### Part list for controller/sensors: 

```
[1] Raspberry Pi Pico RP2040 Microcontroller - ~$8
    https://www.raspberrypi.com/products/raspberry-pi-pico/
[1] SB Components Pi Pico Relay Board - ~$21
    https://shop.sb-components.co.uk/products/raspberry-pi-pico-relay-board
[4] HC-501SR Sensor (5pack) - ~$10
    https://www.amazon.com/DIYmall-HC-SR501-Motion-Infrared-Arduino/dp/B012ZZ4LPM 
[1] Dual USB3.0 + 2.4amp charging adapters (3pack) - ~$16
    https://www.amazon.com/Charger-Costyle-Adaptive-Charging-Compatible/dp/B07YDJ73HB
[1] MicroUSB to Terminal Block adapter - ~$8 
    https://www.amazon.com/Qaoquda-Terminal-Solderless-Converter-Extension/dp/B07PLZS74V
[2] MicroUSB to USB type A cables (older phone charger cables) - ~$6
    https://www.amazon.com/Charging-Transfer-Android-Trustable-MYFON/dp/B098DW7485

Total Cost: ~$70 + shipping
```


## The relay board specs:

```
https://learn.sb-components.co.uk/Pico-Relay-Board
 - Loads up to 250V AC@ 7A, 30V DC@ 10A
 - Optocoupler (CTR: 50~600% at IF =5ma, VCE =5v)
   Allows the circuit to transmit an electrical signal between two isolated circuits through light energy
 - Indication LEDs for Relay output status
```

## You supply (AC related components/wiring):

```
[1] Project box with sufficient space for the SBComponents Relay board and some wiring terminals
[2-3] Wiring terminal blocks - 3 8-conductor?  For this you are want 300v rated at (at least7 to match relay board) at least 7 amps for each light:
                                               120v (US) X 7amp = 840w rated, my lights are 2x35w so 70watts, 1.5x your light rating in total watts should 
                                               be safe for voltage spikes, so for me, this is 10x+ is definitely overkill)
Nonfused:      https://www.amazon.com/Blue-Sea-Systems-20A-Terminal/dp/B000S5Q2VS - ~$10 per
Fused:         https://www.amazon.com/Dinkle-DP4-TFU-5X20-Connection-Connector/dp/B0BW5VL3V1 - ~$22 per
[up to 4] Existing LED/incandescent/Compact Fluorescent lights installed
          Power for each light should be ran directly back to your project box, up to NEC code (14-3 romex, in conduit?), and routed through sufficiently 
          gauged, fused terminal blocks (1.5 times the rated current value of the smallest wire in the circuit) before connecting them your relays.
[1] Recommend a small UPS/Battery backup to keep microcontroller from entering a glitched state from brownouts etc
```

## Links:
`https://github.com/sbcshop/Raspberry-Pi-Pico-Relay-Board`
