import math
import pyaudio     #sudo apt-get install python-pyaudio

p = pyaudio.PyAudio()     #initialize pyaudio

BITRATE = 16000     #number of frames per second/frameset.      

FREQUENCY = 19950     # Hz, waves per second, 261.63=C4-note.
DURATION = 1     # Seconds to play sound

if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100

NUM_FRAMES = int(BITRATE * DURATION)
REST_FRAMES = NUM_FRAMES % BITRATE
WAVEDATA = ''

# Generating waves
for x in range(NUM_FRAMES):
 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

for x in range(REST_FRAMES): 
 WAVEDATA = WAVEDATA + chr(128)

stream = p.open(format=p.get_format_from_width(1), 
                channels=1, 
                rate=BITRATE, 
                output=True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()
