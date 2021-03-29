"""PyAudiable Example: Receive and Demodulate Data (Blocking Mode)"""

import PyA_Receiver as pyaudiable

# instantiate the receiver
receiver = pyaudiable.Receiver(actived_channel = 8, 
                               speed = 'medium', 
                               sensitivity = 'medium')

# active the receiver for 30 seconds
retrieved_data = receiver.read_block(30)


