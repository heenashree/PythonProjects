# this code is used to create beep sound 
# it is added to the code just to know when the code finishes
# below code runs on windows platform

import winsound
duration = 1000  # millisecond
freq = 440  # Hz
winsound.Beep(freq, duration)
