# PyAudible 1.1.0 Evaluation

### Key Takeaway  

The evaluations of the system were conducted along with the development.

 * [Phase I Evaluation: Noise Resistance Mechanism Reliability](#)
   * [Experiment Design](#)
     * [Test 1.1: Flatter Continuous Noise](#)
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

###### Test 1.1: Flatter Continuous Noise
This is the situation where the noise remains constant and stable over the transmission periods, such as ambient noise in office, city traffic, or white noise in a plane. Continuous noise can affect the signal to noise ratio ![equation](https://latex.codecogs.com/gif.download?SNR) between the power of modulated signal ![equation](https://latex.codecogs.com/gif.download?P_%7Bsignal%7D) and the background noise ![equation](https://latex.codecogs.com/gif.download?P_%7Bnoise%7D).  
