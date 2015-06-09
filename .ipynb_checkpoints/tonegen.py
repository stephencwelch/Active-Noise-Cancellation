
#################### Load Libraries #################

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

################ Parameter Specifications ###########

Fs  = 8000  # Set Sampling Rate here
f   = 1000  # Set frequency here
T   = 1     # Set duration of wave to be generated here
pi  = np.pi # Fetch value of pi

################ Generate Time Vector ###############

t= np.arange(0, T, (1.0/Fs) )

################ Generate Output Vector##############

x = np.sin(2 * pi * f * t)

################ Plot Waveform ######################

plt.plot(t, x)
plt.title('Generated Wave')
plt.xlabel('Time(in sec)')
plt.ylabel('Voltage(V)')
plt.show()

################ Save output to file ####################

write('sin1K.wav', Fs, x)

################ End of program ####################
