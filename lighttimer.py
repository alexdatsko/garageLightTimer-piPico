from machine import Pin, Timer
import time

GLOBALTIMER = 180
# Set all lights to turn on for 3 minutes at a time
INITTIMER = 3
# all lights turn on for 3 seconds on startup

LightPins = []
PIRPins = []
PIRTimers = []

LightPins[0] = Pin('GP18', Pin.OUT)   #24
LightPins[1] = Pin('GP19', Pin.OUT)   #25
LightPins[2] = Pin('GP20', Pin.OUT)   #26
LightPins[3] = Pin('GP21', Pin.OUT)   #27

PIRPins[0] = Pin('GP6', Pin.IN, Pin.PULL_DOWN) #9
PIRPins[1] = Pin('GP7', Pin.IN, Pin.PULL_DOWN) #10
PIRPins[2] = Pin('GP8', Pin.IN, Pin.PULL_DOWN) #11 
PIRPins[3] = Pin('GP9', Pin.IN, Pin.PULL_DOWN) #12

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


