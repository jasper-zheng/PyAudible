# PyAudible 0.0.1

A Python library for sending and receiving data using audible sound. PyAudible includes a transmitter and a receiver module that could be implemented on multiple separate devices, enables the transmission of small amounts of data between devices in the vicinity.

## Details
PyAudible includes:  
 - A transmitter module ``PyA_Transmitter`` that generate encoded audio waveforms.  
 - A receiver module ``PyA_Receiver`` that listen and analyse the audio waveforms captured by microphones.  

It allows a configurable transmitting speed between 5 - 20 bytes/sec.  
It uses cyclic redundancy check (CRC) for error detection to improve robustness.  



Possible application scenarios:
 - Smart Home Appliances
 - Data Broadcasting
 - Device Pairing
 - Electronic Ticket
 
## Modes
 
The receiver module provides two receiving modes, in "blocking mode", the receiver blocks until all the requested frame have been recorded; in "callback mode", the receiver is called each frame to allows real-time analysis of recorded audio data.

## Requirements

* **Python** 3.8+
* **PyAudio** 0.2.11+ (speaker access required for the transmitter, microphone access required for the receiver)
* **Numpy** 1.18.5+



## Quickstart

> Tested on Python 3.8 or later  


## Acknowledgment

This project is carry out in comply with the guildlines of COMP390 module, as a key element of the Honours Year Project.








## License
[MIT](https://choosealicense.com/licenses/mit/)