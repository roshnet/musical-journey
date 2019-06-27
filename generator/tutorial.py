import pyaudio
import sys
import wave

CHUNK_SIZE = 1024

if len(sys.argv) < 2:
    print('Plays a `.wav` file.')
    print('Usage: %s filename.wav' % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# Read data
data = wf.readframes(CHUNK_SIZE)

# Play stream
while len(data) > 0:
    try:
        stream.write(data)
        data = wf.readframes(CHUNK_SIZE)
    except KeyboardInterrupt:
        print('Gracefully stopped playback. Exiting.')
        stream.stop_stream()
        stream.close()
        sys.exit(0)
# Stop stream
stream.stop_stream()
stream.close()

# Close pyaudio
p.terminate()
