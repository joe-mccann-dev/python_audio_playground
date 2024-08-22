import os
import pyaudio
import wave
import sys

CHUNK = 1024
SAMPLE_FORMAT = pyaudio.paInt16
CHANNELS = 1
FS = 44100
SECONDS = 10

if len(sys.argv) < 2:
    print(f"Records a stream to wav. Usage: `python {sys.argv[0]} output_filename.wav`")
    sys.exit(-1)
    
audio_dir = r'./audio_files'
if not os.path.exists(audio_dir):
    os.makedirs(audio_dir)
    
FILENAME = f'{audio_dir}/{sys.argv[1]}'

p = pyaudio.PyAudio()

print('Recording audio . . .')

stream = p.open(
    format=SAMPLE_FORMAT,
    channels=CHANNELS,
    rate=FS,
    frames_per_buffer=CHUNK,
    input=True,
    # my microphone is 1, audio interface is 2
    input_device_index=2
)

frames = []

for i in range(0, int(FS / CHUNK * SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    
stream.stop_stream()
stream.close()
p.terminate()

with wave.open(FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(SAMPLE_FORMAT))
    wf.setframerate(FS)
    wf.writeframes(b''.join(frames))
    
print('Finished recording audio.')