"""
Zeyu Hu, Rice University
Last Modifeid: Apr 12th, 2017
Wave File Fourier Transform Analyzer
This python code is deigned to help analyze the fourier tranform of sound, given a limit on the time intervel(start and end)
It will first plot the time domain of the data in the wav file and then perform the fourier transform. 
The code assits our research "Music and Sound Programming using Mathematical Patterns"
"""

from scipy.fftpack import fft
from scipy.io import wavfile 
import matplotlib.pyplot as plt


def wav_analyze(file_name,time_start=None,time_end=None):
	#first get the array from the sound wave
	array = wavfile.read(file_name)[1]

	#check if the wave file has more than one channel
	#Case1 if there is only one channel, we will just use the only one
	if len(list(array.T[0])) == 1:
		data_interval = array[time_start:time_end]

	#Case2 if there are two or more channled, we will use the very first one
	if len(list(array.T[0])) > 1:
		data_interval = array.T[0][time_start:time_end]

	#Plot the time domain
	plt.plot(data_interval)
	plt.show()

	#normalize the data we have on [-1,1), based on the characteristic that Fourier Transform perform a mirror image
	normalized_data = [(sample/2**8.)*2-1 for sample in data_interval]

	# calculate fourier transform, and we only need half of it
	fourier_trans = fft(normalized_data)
	half_fourier_trans = fourier_trans[0:len(fourier_trans)/2]

	plt.plot((half_fourier_trans),'r') 
	plt.show()

wav_analyze('Korg.wav',1000,1200)
