import pyaudio
import wave

chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100
seconds = 10
filename = 'audio_files/output.wav'

p = pyaudio.PyAudio()

print('Recording audio . . .')

stream = p.open(
    format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True,
    # my microphone is 1, audio interface is 2
    input_device_index=2
)

frames = []

for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)
    
stream.stop_stream()
stream.close()
p.terminate()

print('Finished recording audio.')

wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()