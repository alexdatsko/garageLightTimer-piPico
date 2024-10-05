#!/usr/bin/python

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
lasttime = 0

# Set pins on Pi Pico to be used as the output pins to the relays. Default pinout = 24,25,26,27 using the red jumpers CLOSED. (The way the board should arrive)
LightPin1 = Pin('GP18', Pin.OUT)   #Pin24
LightPin2 = Pin('GP19', Pin.OUT)   #Pin25
LightPin3 = Pin('GP20', Pin.OUT)   #Pin26
LightPin4 = Pin('GP21', Pin.OUT)   #Pin27

# Set pins on Pi Pico to be used for the input pins from the HC-301 sensors
PIRPin1 = Pin('GP2', Pin.IN, Pin.PULL_DOWN) #Pin3
PIRPin2 = Pin('GP3', Pin.IN, Pin.PULL_DOWN) #Pin4
PIRPin3 = Pin('GP4', Pin.IN, Pin.PULL_DOWN) #Pin5
PIRPin4 = Pin('GP5', Pin.IN, Pin.PULL_DOWN) #Pin6

# Set timers to 0
PIRTimer1 = 0
PIRTimer2 = 0
PIRTimer3 = 0
PIRTimer4 = 0

def initPins():
  global PIRPin1,PIRPin2,PIRPin3,PIRPin4,PIRTimer1,PIRTimer2,PIRTimer3,PIRTimer4,LightPin1,LightPin2,LightPin3,LightPin4

  print("LightTimer 0.2 - init")
#  print(f"PIRTimers.len = {len(PIRTimers)}")
#  print(f"PIRPins.len = {len(PIRPins)}")
#  print(f"LightPins.len = {len(LightPins)}")
  PIRTimer1 = time.time() + INITTIMER  # Init = all lights turn on for 3 seconds
  LightPin1.value(1)
  PIRTimer2 = time.time() + INITTIMER
  LightPin2.value(1)
  PIRTimer3 = time.time() + INITTIMER
  LightPin3.value(1)
  PIRTimer4 = time.time() + INITTIMER
  LightPin4.value(1)
  
def checkPIR(GLOBALTIMER):
  global PIRPin1,PIRPin2,PIRPin3,PIRPin4,PIRTimer1,PIRTimer2,PIRTimer3,PIRTimer4,LightPin1,LightPin2,LightPin3,LightPin4
  if (PIRPin1.value()>0):
    print(f"Timer1 triggered")
    PIRTimer1 = time.time() + GLOBALTIMER
    LightPin1.value(1)
  if (PIRPin2.value()>0):
    print(f"Timer2 triggered")
    PIRTimer2 = time.time() + GLOBALTIMER
    LightPin2.value(1)
  if (PIRPin3.value()>0):
    print(f"Timer3 triggered")
    PIRTimer3 = time.time() + GLOBALTIMER
    LightPin3.value(1)
  if (PIRPin3.value()>0):
    print(f"Timer4 triggered")
    PIRTimer4 = time.time() + GLOBALTIMER
    LightPin4.value(1)

def checkTimers(lasttime):
  global PIRPin1,PIRPin2,PIRPin3,PIRPin4,PIRTimer1,PIRTimer2,PIRTimer3,PIRTimer4,LightPin1,LightPin2,LightPin3,LightPin4
#  if (time.time() > lasttime):
#    print(f"PIRTimer1 = {PIRTimer1} {time.time()}")
#    print(f"PIRTimer2 = {PIRTimer2} {time.time()}")
#    print(f"PIRTimer3 = {PIRTimer3} {time.time()}")
#    print(f"PIRTimer4 = {PIRTimer4} {time.time()}")
#    lasttime = time.time()
  if (PIRTimer1 > 0) and (time.time() > PIRTimer1):
    print(f"Timer1 triggered off")
    PIRTimer1 = 0
    LightPin1.value(0)
  if (PIRTimer2 > 0) and (time.time() > PIRTimer2):
    print(f"Timer2 triggered off")
    PIRTimer2 = 0
    LightPin2.value(0)
  if (PIRTimer3 > 0) and (time.time() > PIRTimer3):
    print(f"Timer3 triggered off")
    PIRTimer3 = 0
    LightPin3.value(0)
  if (PIRTimer4 > 0) and (time.time() > PIRTimer4):
    print(f"Timer4 triggered off")
    PIRTimer4 = 0
    LightPin4.value(0)
  return lasttime

initPins()
while True:
  checkPIR(GLOBALTIMER)
  lasttime=checkTimers(lasttime)
  time.sleep(0.5)

