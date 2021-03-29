# PyAudiable v1.0.0 documentation
## User Guide

A Python library for sending and receiving data using audible sound. PyAudible includes a transmitter and a receiver module that could be implemented on multiple separate devices, enables the transmission of small amounts of data between devices in the vicinity.  

PyAudible includes:  
 - A transmitter module ``PyA_Transmitter`` that generate encoded audio waveforms.  
 - A receiver module ``PyA_Receiver`` that listen and analyse the audio waveforms captured by microphones.  

It allows a configurable transmitting speed between 5 - 20 bytes/sec.  
It uses cyclic redundancy check (CRC) for error detection to improve robustness.

* [Requirements and Installation](#requirements-and-installation)
* [Getting started with PyAudiable](#)
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
PyAudiable depends on the following dependencies:
* **Python** 3.8+
* **PyAudio** 0.2.11+ (speaker access required for the transmitter, microphone access required for the receiver)
* **Numpy** 1.18.5+

#### Installation
With required dependencies installed, use ``pip install pyaudiable`` to download and install PyAudiable.


## Getting started with PyAudiable
#### Example: Modulate and Transmit Data
