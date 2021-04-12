# PyAudible 0.1.1 documentation

PyAudible is a Python library for sending and receiving data using audible sound. PyAudible includes a transmitter and a receiver module that could be implemented on multiple separate devices, enables the transmission of small amounts of data between devices in the vicinity.  

 * The transmitter module `Transmitter` generates encoded audio waveforms.  
 * The receiver module `Receiver` listens and analyses the audio waveforms captured by microphones.  

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
* **Python** 3.8+  
* **PyAudio** 0.2.11+ (speaker access required for the transmitter, microphone access required for the receiver)  
* **Numpy** 1.18.5+  

#### Installation
With required dependencies installed, use `pip install pyaudible` to download and install PyAudible.


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
To detect and demodulate data, first instantiate a receiver on the desired device by `pyaudiable.Receiver()` with desired parameters (see [Class Receiver](#)). It will initialise a reusable receiver for analysing and demodulating data.

Open the receiver by calling `pyaudible.Receiver.read_block()`, the receiver will stand-by and continuously detecting audio input. The results will be return in a Python list.

Note that the Blocking Mode will block the thread until all the required time have been recorded, therefore not recommend for frame based application. Alternatively, use Callback Mode to process inputs by frames (see next section).

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

In Callback Mode, after the instantiation, the receiver will be repeatedly called each frame by `pyaudible.Receiver.read()`.
Whenever new data is ready, the receiver will return the converted data as string immediately, even if the transmission is not finish. If the log mode is on, the receiver will also return a integer representing the status, to help interacting with the receiver (see [Class Receiver: Callback Mode](#).  

## Class Transmitter

``class pyaudiable.Transmitter``  

Python interface to modulate and transmit data. Provides methods to:  
  * Convert text to modulated audio waveform
  * Write a modulated waveform as a uncompressed WAV file
  * Open PyAudio to stream the modulated audio


#### Transmission Speed
The speed of the transmission should be defined when instantiating the transmitter by `speed` parameter in the instantiation function (see [__ init__()](#)).

Three levels of the speed are specified by ‘slow’, ‘medium’ and ‘fast’. In fast mode, eight channels will be utilised simultaneously for the transmission, and it will provide a speed of 20 bytes per second. Whereas in slow mode, two channels will be utilised for the transmission, and the signal will be copied to the other six channels to improve accuracy.

The following table listed the testing results of the correlation between the transmission speed and the accuracy.



#### Transmission Volume
The volume of the transmission should be defined when instantiating the transmitter by `volume` parameter in the instantiation function (see [__ init__()](#)).

The volume is specified by a float number ranged from 0 to 1, where 0 represents quiet and 1 represent full amplitude of the waveform.

#### Overview
`text_to_bin(), modulate(), modulate_to_file(), modulate_and_play()`

#### Details  

`__init__(speed, volume)`  
###### Parameter
* speed - Specifies the speed of the transmission, type: string
	* ‘slow’
	* ‘medium’
	* ‘fast’  
  Defaults to ‘slow’
* volume - Specifies the loudness of the transmission, type: float ranged form 0 to 1. Defaults to 1.0  

###### Raise
* ParameterError: if the parameter `speed` if invalid.

`text_to_bin(text)`  
Convert ASCII text to binary signal.
###### Parameter
* text - The input text data, type: string

`modulate()`  
Convert text message to a modulated audio waveform.
###### Parameter
* message - The input text data, type: string

###### Return
* waveform - Modulated waveform in array form

`modulate_to_file()`  
Convert text message to a modulated audio waveform and save it as .wav format file.
###### Parameter
* message - The input text data, type: string
* filename - Name of the output wav file, type: string


## Class Receiver
`class pyaudiable.Receiver`

Python interface to detect and demodulate broadcasted audio and convert them into text data.



The receiver should be called only once and it will block until all the required time is recorded. Whereas in the callback mode, the
