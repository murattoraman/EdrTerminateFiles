import pyaudio
import wave
import time

# Mikrofonu aç
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# 10 saniye ortam dinle
start = time.time()
while time.time() - start < 10:
    # Bir ses örneği al
    data = stream.read(1024)

# Mikrofonu kapat
stream.stop_stream()
stream.close()
p.terminate()

# Ses dosyasını oluştur
wf = wave.open("output.wav", "wb")
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(data)
wf.close()
