###### PyAudible 1.1.0
# Transmission Protocol Design
This document gives an overview of the technical details in the transmission protocol. It refers the protocol design to a stripped OSI (Open Systems Interconnection) model and analyses the physical and data link layers.  

## Physical Layer: Multi-channel Carrier Modulation

<img src="https://github.com/jasper-zheng/PyAudible/blob/main/documents/Graphics/multi-channel_carrier.png?raw=true" width="400">  

*Figure 1: Multi-channel Carrier Modulation*  

The protocol utilises a [Frequency-Shift Keying (FSK)](https://en.wikipedia.org/wiki/Frequency-shift_keying) technique to modulate the raw data into an eight-channel carrier signal `Channel_01` - `Channel_08`. Each carrier channel transmits data by switching the frequency within a range of 16 candidate frequencies <code>F<sub>C</sub>(0)</code> - <code>F<sub>C</sub>(15)</code> (Shown in **Figure 1**). And each candidate frequency represents a 4-bit chunk `ck_0` - `ck_15`, shown in **Table 1**. Therefore, 8 x 16 = 128 candidate frequencies are equally spaced between `1238 Hz` to `6965 Hz`, divided by `dF = 43.0 kHz`. The original data is converted into binary representations, and then it is encapsulated into packets of 8, 16 or 32 bits per unit time (depended on the transmission rate), then transmitted via 2, 4 or 8 channels.
<table style="font-size:7px">
    <thead>
        <tr>
            <th>Chunk ID</th>
            <th>Binary Representation</th>
            <th>Frequency</th>
            <th>...</th>
            <th>Chunk ID</th>
            <th>Binary Representation</th>
            <th>Frequency</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ck_00</td>
            <td>0000</td>
            <td>1238 + 0 * 43 Hz</td>
            <td>...</td>
            <td>ck_00</td>
            <td>0000</td>
            <td>6277 + 0 * 43 Hz</td>
        </tr>
        <tr>
            <td>ck_01</td>
            <td>0001</td>
            <td>1238 + 1 * 43 Hz</td>
            <td>...</td>
            <td>ck_01</td>
            <td>0001</td>
            <td>6277 + 1 * 43 Hz</td>
        </tr>
        <tr>
            <td>ck_02</td>
            <td>0010</td>
            <td>1238 + 2 * 43 Hz</td>
            <td>...</td>
            <td>ck_02</td>
            <td>0010</td>
            <td>6277 + 2 * 43 Hz</td>
        </tr>
        <tr>
            <td>...</td>
            <td>...</td>
            <td>...</td>
            <td>...</td>
            <td>...</td>
            <td>...</td>
            <td>...</td>
        </tr>
        <tr>
            <td>ck_15</td>
            <td>1111</td>
            <td>1238 + 15 * 43 Hz</td>
            <td>...</td>
            <td>ck_15</td>
            <td>1111</td>
            <td>6277 + 15 * 43 Hz</td>
        </tr>
    </tbody>
</table>    

*Table 1: Chunk - Binary - Frequency*  

If each channel transmits different data simultaneously, it allows a maximum transmission speed of 32 bits per unit. And if the unit time is 0.2 second, the transmission speed can be up to 20 bytes per sec.   

However, a portion of the communication channels could be used as repeat requests for error control to improve robustness. Depending on the setting, the system utilises 0, 4 or 6 carriers to repeat the transmission signal. Error correction is based on the original signal and the repeated signal.   

![image](https://github.com/jasper-zheng/PyAudible/blob/main/documents/Graphics/infoboard-01.png?raw=true)   
*Figure 2: Receiver Data Process Flow*  

For example, in *Figure 2*, the transmission speed set to "slow", therefore, the original binary data will be divided into two splits, the first split will be transmitted through channel 01, 03, 05 and 07, the second split will be transmitted through channel 02, 04, 06 and 08. After demodulating the signal, the receiver will analyse each split of data respectively. Then perform error correction based on the repeated signals. And finally, the receiver will recover the binary data and convert it into text format.  
