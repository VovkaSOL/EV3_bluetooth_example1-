#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color, ImageFile
from pybricks.tools import print,wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from pybricks import ev3brick as brick


from pybricks import ev3brick as brick
import struct
from threading import Thread


def ukus():
     motorA.run(2000)
     wait(700)
     motorA.run_time(-2000, 1500)


joy_left = 0
joy_right = 0
joy_x =0
joy_e =0
joy_sq =0


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.

# images = 'RIGHT FORWARD ACCEPT QUESTION_MARK STOP_1 LEFT DECLINE \
# THUMBS_DOWN BACKWARD NO_GO WARNING STOP_2 THUMBS_UP'.split()
# for image in images:
#   brick.display.clear()
#   brick.display.text(image, (10, 10))
#   brick.display.
#   file = eval('ImageFile.'+image)
#   brick.display.image(file, clear=False)
#   wait(1000)

ev3 = EV3Brick()
# Find the PS3 Gamepad:
# /dev/input/event3 is the usual file handler for the gamepad.
# look at contents of /proc/bus/input/devices if it doesn't work.
infile_path = "/dev/input/event2"

# open file in binary mode
in_file = open(infile_path, "rb")
print(in_file)

# Read from the file
# long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(FORMAT)
# ev3.speaker.play_notes(['C4/4', 'C4/4', 'G4/4', 'G4/4'], tempo=120)
# ev3.speaker.set_volume(100, which='_all_')
# ev3.speaker.set_speech_options(language='en', voice='f1' , speed=None, pitch=None)
# ev3.speaker.play_file(SoundFile.OKAY)
# time.sleep(5000)
motorA=Motor(Port.A)
motorB=Motor(Port.B)
motorD=Motor(Port.D)
# motorB.run_target(10000, 90, then=Stop.HOLD, wait=True)

# Write your program here.
# ev3.speaker.beep()
time.sleep(1)
# Motor(Port.B)
print("Foo3rer")
# ev3.speaker.beep()
# ev3.speaker.beep()
# ev3.speaker.beep()
# ev3.speaker.beep()
# motorB.run(2000)
while True:
  event = in_file.read(EVENT_SIZE)
  # print(event)
  str1="".join("%02x" % b for b in event)

  # print(str1)
  print_joy=0
  
  if str1.find("03001000ffffffff")!=-1:
    joy_left=1;
    print_joy=1
  if str1.find("0300100000000000")!=-1:
    joy_left=0;
    joy_right=0;
    print_joy=1
  if str1.find("0300100001000000")!=-1:
    joy_right=1;
    print_joy=1
  if str1.find("0100300101000000")!=-1:
    joy_x=1;
    print_joy=1
  if str1.find("0100300100000000")!=-1:
    joy_x=0;
    print_joy=1
  if str1.find("0100310101000000")!=-1:
    joy_e=1;
    print_joy=1
  if str1.find("0100310100000000")!=-1:
    joy_e=0;
    print_joy=1
  if str1.find("0100330101000000")!=-1:
    joy_sq=1;
    print_joy=1
  if str1.find("0100330100000000")!=-1:
    joy_sq=0;
    print_joy=1



  # print(str1)
  if print_joy==1: 
    # print(str1)
    # print("joy_right="+str(joy_right)+"joy_left"+str(joy_left)+"joy_x="+str(joy_x)+"joy_e="+str(joy_e)+"joy_sq="+str(joy_sq))
    if joy_x==1: #вперед
    #  print("вперед")
     motorB.run(2000)
    if joy_e==1: #назад
    #  print("назад")
     motorB.run(-2000) 
    if joy_x==0 and joy_e==0 : #стоп
    #  print("стоп вперед назад")
     motorB.stop()

    if joy_left==1: #влево
    #  print("влево")
     motorD.run_time(-500, 300)
    if joy_right==1: #вправо
    #  print("вправо")
     motorD.run_time(500, 300)

    if joy_sq==1: #укус
    #  print("укус")
      ukus_loop = Thread(target=ukus)
      #start the sub program
      ukus_loop.start()
    # if joy_sq==0: #
    #  print("стоп укус")
    #  motorA.hold()



  # b = brick.buttons()
#   print(b)
#   if Button.LEFT in b:
#      brick.light(Color.GREEN)
#   if Button.CENTER in b:
#      brick.light(Color.YELLOW)
#   if Button.RIGHT in b:
#      brick.light(Color.RED)


