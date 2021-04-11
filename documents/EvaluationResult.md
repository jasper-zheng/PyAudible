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

<table>
    <thead>
        <tr>
            <th></th>
            <th>Layer 2</th>
            <th>Layer 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan=4>L1 Name</td>
        </tr>
    </tbody>
</table>
