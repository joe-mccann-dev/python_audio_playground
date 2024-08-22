import pyaudio
import wave
import sys

filename = sys.argv[1]

chunk = 1024

wf = wave.open(filename, 'rb')

p = pyaudio.PyAudio()

stream = p.open(
    format = p.get_format_from_width(wf.getsampwidth()),
    channels = wf.getnchannels(),
    rate = wf.getframerate(),
    output = True
)

data = wf.readframes(chunk)

while data != b'':
    stream.write(data)
    data = wf.readframes(chunk)
    
stream.close()
p.terminate()