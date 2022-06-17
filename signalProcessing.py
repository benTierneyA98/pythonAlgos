import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt
from scipy.io import wavfile
# ---------------------creating an input signal---------------------------------
plt.close("all")
fa, fs, N = 1000, 8000.0, 256 # Analogue Freq, Sampling Freq, No. of
# display samples
n = np.arange(0, N)
t=n/fs; #Discrete time values
Q=2*np.pi*fa/fs # Normalised frequency
tone=np.sin(n*Q)
plt.figure(1)
plt.plot(t, tone)
plt.title('Sinusoidal Tone')
plt.xlabel('Time (secs)')
plt.ylabel('Amplitude (V)')
plt.grid()
plt.show()
#-------------------Generating the FFT of the signal--------------------------
NFFT=1024 # No. of values in FFT
M = 2*np.abs(scipy.fftpack.fft(tone,NFFT))/N
M = M[0:int(NFFT/2)] #slicing operation to avoid mirroring
freq = np.arange(0,NFFT/2) #frequency vector
freq = freq*fs/NFFT
plt.figure(2)
plt.plot(freq,M)
plt.title('Spectrum of Tone')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (V)')
plt.grid()
plt.show()

fa1, fa2, fa3=500, 1500, 3000
A1, A2, A3= 3, 2, 1

Q1=2*np.pi*fa1/fs # Normalised frequency
Q2=2*np.pi*fa2/fs # Normalised frequency
Q3=2*np.pi*fa3/fs # Normalised frequency

tone1=A1*np.sin(n*Q1)
tone2=A2*np.sin(n*Q2)
tone3=A3*np.sin(n*Q3)

sig=tone1+tone2+tone3

plt.figure(1)
plt.plot(t, sig)
plt.title('Composite Signal (Ben Tierney')
plt.xlabel('Time (secs')
plt.ylabel('Amplitude(V)')
plt.grid()
plt.show()

M = 2*np.abs(scipy.fftpack.fft(sig,NFFT))/N
M = M[0:int(NFFT/2)]
freq = np.arange(0,NFFT/2)
freq =freq*fs/NFFT
plt.figure(6)
plt.plot(freq,M)
plt.title('Spectrum of Composite Signal')
plt.xlabel('Time (secs')
plt.ylabel('Amplitude(V)')
plt.grid()
plt.show()

fs, audio = wavfile.read('C:\Users\Pcuser\Downloads')
NN=len(audio)*1.0
t=np.arange(0,NN)/fs

plt.figure(7)
plt.plot(t,audio)
plt.title('Spectrum of Speech Signal')
plt.xlabel('Time (secs')
plt.ylabel('Amplitude(V)')
plt.grid()
plt.show()

M = 2*np.abs(scipy.fftpack.fft(sig,NFFT))/N
M = M[0:int(NFFT/2)]
freq = np.arange(0,NFFT/2)
freq =freq*fs/NFFT
plt.figure(8)
plt.plot(freq,M)
plt.title('Spectrum of Composite Signal')
plt.xlabel('Time (secs')
plt.ylabel('Amplitude(V)')
plt.grid()
plt.show()

wavfile.write('e:\invspeech_dft.wav',fs,invaudio)

plt.figure(11)
plt.plot(t,[0:1024], audio[0:1024])
plt.title('audio')
plt.xlabel('Time (secs')
plt.ylabel('Amplitude(V)')
plt.grid()
plt.show()

plt.figure(12)
plt.plot(t,[0:1024], invaudio[0:1024])
plt.title('invaudio')
plt.xlabel('Time (secs')
plt.ylabel('Amplitude(V)')
plt.grid()
plt.show()
