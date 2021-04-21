"""PyAudible Example: Receive and Demodulate Data (Blocking Mode)"""

import pyaudible

# instantiate the receiver
rx = pyaudible.Receiver(sensitivity = 'medium', 
                        speed = 'auto')

# active the receiver for 30 seconds
retrieved_data = rx.read_block(30)