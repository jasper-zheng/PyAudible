# PyAudible 1.1.0  

A Python library for sending and receiving data using audible sound. PyAudible includes a transmitter and a receiver module that could be implemented on multiple devices, enables the transmission of small amounts of data between separated systems in the vicinity.

The library implements a Multi-channel Carrier Modulation protocol, allows a configurable transmitting speed between 5 - 20 bytes/sec. It uses [Cyclic Redundancy Check (CRC)](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) to ensure reliable delivery of data.  

The transmitter and the receiver provide simplified Python interface that could be easily integrated in various other projects, possible scenarios includes:

 - Smart Home Appliances (IoT)  
 - Data Broadcasting  
 - Device Pairing  
 - Electronic Key Sharing  


This README file provides the following information:  
 * [Quickstart](#)
   * [Requirements](#)
   * [Installation](#)
 * [Examples and Demos](#)
 * [Protocol Overview](#)
 * [Documentation](#)
 * [Test and Evaluation](#)
 * [Updates](#)
 * [Acknowledgment](#)
 * [License](#)

## Quickstart  
> Tested on Python 3.8 or later  

#### Requirements

* **Python** 3.8+  
* **PyAudio** 0.2.11+ (speaker access required for the transmitter, microphone access required for the receiver)  
* **Numpy** 1.18.5+  

#### Installation  
With required dependencies installed, use `pip install pyaudible` to download and install PyAudible.  

To validate the installation, run the following code and it should print the version of PyAudible, PyAudio and PortAudio to the console.  
```
import pyaudible
pyaudible.print_version()
```

## Examples and Demos












## Acknowledgment

This project is carry out in comply with the guildlines of COMP390 module, as a key element of the Honours Year Project.

## License
[MIT](https://choosealicense.com/licenses/mit/)
