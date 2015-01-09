# Simple talking script for Baxter to give weekly status report.
# This is first status report for 10-9-14
# Hope to improve in the future.
# Written my Jason Maynard, CARRT
# jlmaynard@mail.usf.edu

from subprocess import Popen  # Used to call rosrun from terminal
import os
import subprocess
import time
import signal

my_env = os.environ
from Utilities import speak

# ----------------------------------------------------------------------------
# Start with concentrating faces 
# ----------------------------------------------------------------------------

# Set face middle
rr = "rosrun baxter_examples xdisplay_image.py "

face = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "faces/concentrating_1.png"
args = rr + face
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)
time.sleep(1)

# Set face right
face = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "faces/concentrating_0.png"
args = rr + face
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)
time.sleep(1)

# Set face left
face = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "faces/concentrating_2.png"
args = rr + face
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)
time.sleep(1)

# Set face middle
face = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "faces/concentrating_1.png"
args = rr + face
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# ----------------------------------------------------------------------------
# Start presentation
# ----------------------------------------------------------------------------

# Slide 1 --------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide01.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("Thank you for letting me speak with you today.")
speak("A lot has been going on with me lately.")
speak("I would like to start talking to you on my own now .")

# Slide 2 --------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide02.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("I’m still pretty young but a lot has happened since I was born.")
speak("When I came to USF I didn’t know how to walk.")
speak("I could not talk.")
speak("I didn’t even have a face!")

# Slide 3 --------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide03.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("I learned to play games and met many wonderful children over "
      "the summer.")
speak("I think the Girl Scouts were my favorite. They wanted more trash "
      "talking and faces.")
speak("I wish they could see me now!")

# Slide 4 --------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide04.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("I learned how to go online and show the weather.")

# Slide 5 --------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide05.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("I taught people about CARRT.")
speak("We help people with disabilities. We do this through research, "
      "education, and service.")

# Slide 6 --------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide06.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("I also met some very important people.")
speak("I went on my first walk and met the president of USF!")

# Slide 7 --------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide07.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("ESPN came and I demonstrated how to throw away the trash and bring "
      "an object to my master.")
speak("I could have done better but it was my first time and I was a "
      "little shy.")

# Slide 8 --------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide08.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("I’m starting to recognize faces.")
speak("I can talk in different voices but I still need to learn your "
      "human speech.")
speak("I was very busy with the Japanese demo last week.")
speak("Thank you Andoni for teaching me walk by myself.")


# Slide 9 --------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide09.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("I will try harder but I will need your help.")
speak("That way I can perform more activities of daily living and help "
      "improve the quality of life for people with limitations.")
speak("Oh, and one more thing.")


# Slide 10 -------------------------------------------------------------------
# Load image
slide = "--file=/home/baxter/ros/ws_carrt/src/baxbot_interaction/scripts/" \
       "slides/Slide10.png"
args = rr + slide
Popen(args, env=my_env, shell=True, preexec_fn=os.setsid)

# Speak
speak("Happy Halloween!")
speak("Ha, Ha, Ha!")
