# Converts from .TXT to .WAV format
# Bruce MacKinnon 9-Nov-2023
#
import scipy.io.wavfile as wavfile
import numpy as np

#in_fn = "demo-750.txt"
#out_fn = "demo-750.wav"
#in_fn = "../hello-scamp/scamp-fsk-slow-demo-0.txt"
in_fn = "../hello-scamp/bin/scamp-fsk-demo-2.txt"
out_fn = "scamp-fsk-demo-2.wav"
#samplerate = 2000; 
samplerate = 44100; 

with open(in_fn, "r") as txt_file:
    data = np.array([int(line) for line in txt_file])
    noise = np.random.normal(0, 1, data.size) * 50
    #noise = noise.astype(int)
    #print(data)
    #print(noise)
    #both = np.add(data, noise)
wavfile.write(out_fn, samplerate, data.astype(np.int16))

"""
# Writing
fs = 750
t = np.linspace(0.0, 4.0, samplerate * 4)
amplitude = np.iinfo(np.int16).max
data = amplitude * np.sin(2.0 * np.pi * fs * t)
with open("demo-750.txt", "w") as txt_file:
    for d in data:
        txt_file.write(str(int(d)) + "\n")
"""

