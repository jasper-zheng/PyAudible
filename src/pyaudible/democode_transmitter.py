"""PyAudiable Example: Modulate and Transmit Data"""

import PyA_Transmitter as pyaudiable

# instantiate the transmitter
transmitter = pyaudiable.Transmitter(speed = 'fast', volume = 1.0)

# define the message to be transmitted
message = 'Hello World!'

# define the filename
filename = 'transmitter_sample.wav'

# modulate the message and store the modulated signal to an audio file
transmitter.modulate_to_file(message, filename)

