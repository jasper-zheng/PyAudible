# PyAudible 1.1.0 Evaluation

### Key Takeaway  

The evaluations of the system were conducted along with the development.

 * [Phase I Evaluation: Noise Resistance Mechanism Reliability](#phase-i-evaluation-noise-resistance-mechanism-reliability)
   * [Experiment Design](#experiment-design)
     * [Test 1.1: Flatter Continuous Noise](#test-11-flatter-continuous-noise)
     * [Test 1.2: Sudden Disruptive Noise](#)
   * [Result and Analysis](#)  
 * [Phase II Evaluation: System Reliability vs. Speed and Noise Conditions](#)
   * [Experiment Design](#)
     * [Test 1.2: System Reliability](#)
   * [Result and Analysis](#)  

## Phase I Evaluation: Noise Resistance Mechanism Reliability  
The goal of Phase I evaluation is to assess the reliability of the noise resistance mechanism, including Sound Mark Integrity Check and Error Detecting Code. As a part of the transmission protocol, noise resistance mechanism should be able to tolerant to unpredictable background noise.   

To detect and recover from the noise, the receiver assess the sound marks to decide whether the current noise condition is competent for a successful transmission, and then use error detecting codes to verify transmission integrity. Therefore, to assess the reliability of this mechanism, the following criteria were included:  
 * The probability that the receiver staying inactive when the power of the background noise is strong enough to disturb the transmission.  
 * The probability that the receiver successfully detect the fault caused by the noise and abort the transmission.  

#### Experiment Design

The test consists of two parts, aims at assess the noise resistance mechanism under two noise conditions: Flatter Continuous Noise and Sudden Disruptive Noise.  

##### Test 1.1: Flatter Continuous Noise  

This is the situation where the noise remains constant and stable over the transmission periods, such as ambient noise in office, city traffic, or white noise in a plane. Continuous noise can affect the signal to noise ratio ![equation](https://latex.codecogs.com/svg.image?SNR) between the power of modulated signal ![equation](https://latex.codecogs.com/svg.image?P_{signal}) and the background noise ![equation](https://latex.codecogs.com/svg.image?P_{noise}) .  

The test was conducted in a transmission system between a MacBook and an iPhone, where the MacBook acted as the receiver and the iPhone acted as the transmitter, with a distance of 2 meters. To control the noise in the environment, the system was implemented in a silent room with acoustic control, a separated speaker was used to produce recorded ambient noise at desired levels.  

The test include three rounds, where the activation sensitivity was set to different levels. In each round, data were transmitted in the same system in turns, but with different settings (with and without noise resistance mechanism implemented).  

In addition, a special handling in the test is that whether the receiver decide to stay inactive or be activated, the system will active the receiver anyway, to verify whether the receiver is making the correct decision on staying inactive.  

Following data were recorded:  
  * **Total Transmission:** Count the total number of transmission.  
  * **Succeed Activation:** Number of times that the receiver was activated.  
  * **Invalid Aborting:** Number of times that the activation was decided abort, however, the receiver still got correct data from the transmission.  
  * **Incorrect Transmission:** Number of times that the receiver got incorrect data, regardless the error report.  
  * **Fault was Detected:** Number of times that the receiver got incorrect data, but the fault was successfully detected and the transmission aborted.
  * **Fault Detection:** Number of times that the data was successfully transmitted, but an error was mistakenly reported.

To improve the generality of the test, each round of test will repeat until 100 incorrect transmissions were made. The reliability `R` of the noise resistance mechanism could be represented as the probability that the receiver aborted the activation or detected the fault, given that the transmission was not successful. Therefore, let `A` denotes the event that an activation was aborted, `D` denotes the event that a fault was detected, `F` denotes the event that a transmission was failed. According to the axioms of probability theory, the reliability  `R` could be calculated by:  

![equation](https://latex.codecogs.com/svg.image?R&space;=&space;P((A&space;\cup&space;D)|F)=\frac{P(A\cup&space;D&space;\cap&space;F)}{P(F)})   

##### Test 1.2: Sudden Disruptive Noise  
In this situation, the noise refers to sudden bursts of sounds happens after the transmission started, such as a cough or sneeze, sudden talks and hand claps, or a falling object hits the floor. Disruptive noise may have destructive affect on the transmission, since the amplitude and frequency of noise may fully cover the transmission channels. Therefore, the error detecting code should be able to identified the fragmentary in the received data.   

The basic set up of the test was the same as **Test 1.1**, however, in addition to the continuous background noise, another sudden bursting noise was triggered after the receiver was activated, the type of bursting noise include random played hand claps, shouts, laughter and clanks.  

Following data was recorded:  

 * **Succeed Transmission:** Number of times that the data was successfully transmitted to the receiver, with no error reported.
 * **Failed Transmission:** Number of times that the receiver got incorrect data, with no error detected.  
 * **Fault was Detected:** Number of times that the receiver got incorrect data, but the fault was successfully detected and the transmission aborted.  

The reliability `R` was be represented as the probability that the receiver detected the fault, given that the transmission was not successful.  

![equation](https://latex.codecogs.com/svg.image?R&space;=&space;P(FaultDetected|TransmissionFailed)&space;=&space;\frac{P(TransmissionFailed\cap&space;FaultDetected)}{P(TransmissionFailed)})  


#### Experiment Results
##### Test 1.1 Results: Flatter Continuous Noise
<table style="font-size:7px">
    <thead>
        <tr>
            <th></th>
            <th>Total Transmission</th>
            <th>Succeed Activation</th>
            <th>Invalid Aborting</th>
            <th>Incorrect Transmission</th>
            <th>Fault was Detected</th>
            <th>Fault Detection</th>
            <th>Reliability</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan=8 align="center">Activation Sensitivity = 3 (Low Sensitivity)</td>
        </tr>
        <tr>
            <td>With Noise Resistance</td>
            <td>129</td>
            <td>50</td>
            <td>12</td>
            <td>100</td>
            <td>26</td>
            <td>1</td>
            <td>0.93</td>
        </tr>
        <tr>
            <td>w/ Noise Resistance</td>
            <td>125</td>
            <td>116</td>
            <td>N/A</td>
            <td>100</td>
            <td>N/A</td>
            <td>N/A</td>
            <td>0.09</td>
        </tr>
        <tr>
            <td colspan=8 align="center">Activation Sensitivity = 2 (Medium Sensitivity)</td>
        </tr>
        <tr>
            <td>With Noise Resistance</td>
            <td>139</td>
            <td>85</td>
            <td>10</td>
            <td>100</td>
            <td>50</td>
            <td>2</td>
            <td>0.94</td>
        </tr>
        <tr>
            <td>w/ Noise Resistance</td>
            <td>125</td>
            <td>111</td>
            <td>N/A</td>
            <td>100</td>
            <td>N/A</td>
            <td>N/A</td>
            <td>0.14</td>
        </tr>
        <tr>
            <td colspan=8 align="center">Activation Sensitivity = 1 (High Sensitivity)</td>
        </tr>
        <tr>
            <td>With Noise Resistance</td>
            <td>123</td>
            <td>99</td>
            <td>5</td>
            <td>100</td>
            <td>62</td>
            <td>1</td>
            <td>0.81</td>
        </tr>
        <tr>
            <td>w/ Noise Resistance</td>
            <td>141</td>
            <td>122</td>
            <td>N/A</td>
            <td>100</td>
            <td>N/A</td>
            <td>N/A</td>
            <td>0.19</td>
        </tr>
    </tbody>
</table>  

**Table 1.1.1: Recorded data for test2.1**

The testing results were recored in **Table 1.1.1** and **Table 1.2.1**, relevant data was calculated. **Figure 1.1.1** shows significant increase in reliability with respect to the noise resistance mechanism, and a modest decrease when raised the activation sensitivity from medium to high. However in **Figure 1.1.2**, it is shown that when the activation sensitivity was low, 75% of failed transmission were prevented in respect of the SNR check, whereas when the activation sensitivity was high, a majority of failed transmission were prevented by the error detecting code.  

 ![Figure 1.1.1 noise resistance mechanism Reliability](https://github.com/jasper-zheng/PyAudible/blob/main/tests/Figures/F_1.1.1.png?raw=true)  

 
