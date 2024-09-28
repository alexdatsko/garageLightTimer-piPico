
########################################################################################
#
# LightTimer.py - Alex Datsko 2024 alexdatsko@gmail.com
# https://github.com/alexdatsko/LightTimer
#   Light Controller project [MicroPython]
#   Raspberry Pi Pico / SB Components Pi Pico Relay Board / HC-501SR PIR sensors
#
#

from machine import Pin, Timer
import time

GLOBALTIMER = 180
# Set all lights to turn on for 3 minutes at a time
INITTIMER = 3
# all lights turn on for 3 seconds on startup

LightPins = []
PIRPins = []
PIRTimers = []

# Set pins on Pi Pico to be used as the output pins to the relays. Default pinout = 24,25,26,27 using the red jumpers CLOSED. (The way the board should arrive)
LightPins[0] = Pin('GP18', Pin.OUT)   #Pin24
LightPins[1] = Pin('GP19', Pin.OUT)   #Pin25
LightPins[2] = Pin('GP20', Pin.OUT)   #Pin26
LightPins[3] = Pin('GP21', Pin.OUT)   #Pin27

# Set pins on Pi Pico to be used for the input pins from the HC-301 sensors
PIRPins[0] = Pin('GP2', Pin.IN, Pin.PULL_DOWN) #Pin3
PIRPins[1] = Pin('GP3', Pin.IN, Pin.PULL_DOWN) #Pin4
PIRPins[2] = Pin('GP4', Pin.IN, Pin.PULL_DOWN) #Pin5
PIRPins[3] = Pin('GP5', Pin.IN, Pin.PULL_DOWN) #Pin6

def initPins():
  global PIRPins,PIRTimers,LightPins
  for i in range(0,3):
    PIRTimers[i] = INITTIMER  # Init = all lights turn on for 3 seconds
    LightPins[i].value(1)
  
def checkPIR():
  global PIRPins,PIRTimers, LightPins
  for i in range(0,3):
    if (PIRPins[i].value):
      PIRTimers[i] = time.time()
      LightPins[i].value(1)

def checkTimers(LightTimer):
  global PIRPins,PIRTimers,LightPins
  for i in range(0,3):
    if (PIRtimers[i] > 0) and (time.time() - PIRTimers[i] > LightTimer):
      PIRTimers[i] = 0
      LightPins[i].value(0)

initPins()
while True:
  checkPIR()
  checkTimers(GlobalTimer)


