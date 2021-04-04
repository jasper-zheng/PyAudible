# PyAudible 0.1.1 documentation

PyAudible is a Python library for sending and receiving data using audible sound. PyAudible includes a transmitter and a receiver module that could be implemented on multiple separate devices, enables the transmission of small amounts of data between devices in the vicinity.  

 - The transmitter module ``PyA_Transmitter`` generates encoded audio waveforms.  
 - The receiver module ``PyA_Receiver`` listens and analyses the audio waveforms captured by microphones.  

It allows a configurable transmitting speed between 5 - 20 bytes/sec.  
It uses cyclic redundancy check (CRC) for error detection to improve robustness.

## User Guide

* [Requirements and Installation](#Requirements-and-Installation)
* [Getting started with PyAudible](#)
  * [Example: Modulate and Transmit Data](#)
  * [Example: Receive and Demodulate Data (Blocking Mode)](#)
  * [Example: Receive and Demodulate Data (Callback Mode)](#)
* [Class Transmitter](#)
  * [Volume](#)
  * [Transmission Speed](#)
* [Class Receiver](#)
  * [Listening Modes](#)
    * [Blocking Mode](#)
    * [Callback Mode](#)
  * [Retrieved Data](#)
  * [System Logs and FFT Logs](#)



## Requirements and Installation

#### Requirements
PyAudible depends on the following dependencies:  
- **Python** 3.8+  
- **PyAudio** 0.2.11+ (speaker access required for the transmitter, microphone access required for the receiver)  
- **Numpy** 1.18.5+  

#### Installation
With required dependencies installed, use ``pip install pyaudible`` to download and install PyAudible.


## Getting started with PyAudible
#### Example: Modulate and Transmit Data
```python
"""PyAudible Example: Modulate and Transmit Data"""

import PyA_Transmitter as pyaudible

# instantiate the transmitter
transmitter = pyaudible.Transmitter(shared_channel = 2,
                                     volume = 1.0)

# define the message to be transmitted
message = 'Hello World!'

# modulate the message
# then store the modulated signal to an audio file
transmitter.modulate_to_file(message, 'transmitter_sample.wav')
```
To convert a message to electrical signals and generate the modulated audio file, first instantiate PyAudible by ``pyaudible.Transmitter()`` with desired parameters (see [Class Transmitter](#)). It will initialise a transmitter for modulating data.   

Modulate a message by calling ``pyaudible.Transmitter.modulate_to_file()`` with input data and the file name, it will modulate the data to audio waveforms and save it to a playable file.

To modulate a message without save it to file, or play the audio right after the modulation, call ``pyaudiable.Transmitter.modulate()`` or ``pyaudiable.Transmitter.modulate_and_play()`` (see [Class Transmitter](#)).

#### Example: Receive and Demodulate Data (Blocking Mode)
```python
"""PyAudiable Example: Receive and Demodulate Data (Blocking Mode)"""

import PyA_Receiver as pyaudiable

# instantiate the receiver
receiver = pyaudiable.Receiver(actived_channel = 8,
                               speed = 'medium',
                               sensitivity = 'medium')

# active the receiver for 30 seconds
retrieved_data = receiver.read_block(30)

```





#### Example: Receive and Demodulate Data (Callback Mode)
```python
"""PyAudiable Example: Receive and Demodulate Data (Callback Mode)"""

import PyA_Receiver as pyaudiable
import time

# instantiate the receiver
receiver = pyaudiable.Receiver(actived_channel = 8,
                               speed = 'medium',
                               sensitivity = 'medium')

# create a empty variable to store the retrieced data
retrieved_data = ''

# create a while loop for 30 seconds
start_time = time.time()
while (time.time() - start_time < 30):

    # call the receiver on each frames
    # the receiver will return received data on the fly
    data, _ = receiver.read(log = True)

    # if retrieced data is not empty, add then to the predefined variable
    if data:
        retrieved_data += data

# Received data will also be stored in a list,
# it contains messages demodulated from each singal during the standby time
message_list = receiver.received_data()
```


## Class Transmitter


``class pyaudiable.Transmitter``  

Python interface to modulate and transmit data. Provides methods to:  
  * Convert text to modulated audio waveform
  * Write a modulated waveform as a uncompressed WAV file
  * Open PyAudio to stream the modulated audio
