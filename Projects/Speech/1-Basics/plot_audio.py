import wave
import matplotlib.pyplot as plt
import numpy as np

with wave.open('obama.wav', 'rb') as obj:
    sample_freq = obj.getframerate()
    n_samples = obj.getnframes()
    signal_wave = obj.readframes(n_samples)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
t_audio = n_samples / sample_freq

print("Duration of audio:", t_audio, "seconds")

times = np.linspace(0, t_audio, num=len(signal_array))

fig_width = t_audio * 0.5
fig_height = 5

plt.figure(figsize=(fig_width, fig_height))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Amplitude")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()
