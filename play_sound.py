import pyaudio
import wave
import sys

CHUNK = 1024

if len(sys.argv) < 2:
    print(f"Plays a wav file. Usage: `python {sys.argv[0]} filename.wav`")
    sys.exit(-1)
    
FILENAME = sys.argv[1]
    
with wave.open(FILENAME, 'rb') as wf:
    # Instantiate PyAudio and initialize PortAudio system resources
    p = pyaudio.PyAudio()
    
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    while len(data := wf.readframes(CHUNK)):
        stream.write(data)
    
    
    stream.close()
    p.terminate()