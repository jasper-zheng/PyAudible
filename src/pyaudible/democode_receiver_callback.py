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