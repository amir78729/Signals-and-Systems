from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.fftpack import fftfreq
import sys
import warnings
from matplotlib import style


def sample_wave(sample, x, y):
    file_name = 'wav_files/sample_{}.wav'.format(sample)
    sample_rate, signal = wavfile.read(file_name)
    ff_transform = fft(signal)
    # n = signal.shape[0]
    # t = 1 / sample_rate
    # frequencies = fftfreq(n, t)
    # amplitude = (2.0 / n * ff_transform)

    duration = len(signal)/sample_rate
    time = np.arange(0,duration,1/sample_rate) 

    time_plots[sample - 1].plot(time, signal, color=color[sample - 1])
    time_plots[sample - 1].set_title(file_name)

    frequency_plots[sample - 1].plot(ff_transform, color=color[sample - 1])
    frequency_plots[sample - 1].set_title(file_name)
    
    # plt.ylabel("amplitude")
    # plt.xlabel("Frequency")

    # area = np.real(amplitude[(frequencies >= x) & (frequencies <= y)])
    code = []
    for i in range(300000, 300641, 10):
    # for i in range(5, len(area), 10):
        if ff_transform[i] < 0:
            code.append('0')
        if ff_transform[i] >= 0:
            code.append('1')
    print("sample", sample, ':',
          chr(int("".join(code[0:8]), 2)),
          chr(int("".join(code[8:16]), 2)),
          chr(int("".join(code[16:24]), 2)),
          chr(int("".join(code[24:32]), 2)),
          chr(int("".join(code[32:40]), 2)),
          chr(int("".join(code[40:48]), 2)),
          chr(int("".join(code[48:56]), 2)),
          chr(int("".join(code[56:64]), 2)))


if not sys.warnoptions:
    warnings.simplefilter("ignore")
style.use('dark_background')
title = 'Signals and Systems (Fall 2020) - Amirhossein Alibakshi (9731096)\nHomework 4'
edge = [
    [12964.5, 12992.2],
    [10840.5, 10863.2],
    [14990.15, 15022.41],
    [20059.5, 20102.3],
    [12323.6, 12350.4]
]
color = ['red', 'orange', 'gold', 'yellow', 'white']
ff, frequency_plots = plt.subplots(5, 1)
ft, time_plots = plt.subplots(5, 1)
# ft.suptitle(title + " - time")
# ff.suptitle(title + " - frequency")
for s in range(5):
    sample_wave(s + 1, edge[s][0], edge[s][1])
plt.show()
