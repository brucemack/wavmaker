# Converts from .WAV to .TXT format
# Bruce MacKinnon 9-Nov-2023
#
import scipy.io.wavfile as wavfile
import numpy as np

in_fn = "../hello-scamp/demo/AK1WI-SCAMP-40m.wav"
out_fn = "../hello-scamp/demo/AK1WI-SCAMP-40m.txt"

samplerate, data = wavfile.read(in_fn)

print("Sample Rate (Hz)   ", samplerate)
print("Sample Count       ", data.size)
print("Duration (Seconds) ", data.size / samplerate)
print("Min                ", data.min())
print("Max                ", data.max())
print("Mean               ", data.mean())

# Create a text file
with open(out_fn, "w") as txt_file:
    for x in np.nditer(data):
        txt_file.write(str(x) + "\n")








