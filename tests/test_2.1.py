#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

The goal of Phase II evaluation is to assess the reliability of the noise 
resistance mechanism implemented in the Activating and Terminating Sound 
Marks. The mechanism should be able to tolerant to unpredictable background 
noise. 

"""

import PyA_Transmitter as pyaudible_t
import PyA_Receiver as pyaudible_r
import random
import string 
import time

'''

tx_2 = pyaudible.Transmitter(speed = 'slow', volume = 1.0)

tx_4 = pyaudible.Transmitter(speed = 'medium', volume = 1.0)

tx_8 = pyaudible.Transmitter(speed = 'fast', volume = 1.0)

'''





def generate_random_text(n = 10, min_length = 3, max_length = 20):
    texts = []
    file = open('testing_data.txt', 'a')
    for i in range(n):
        t = ''.join(random.choices(string.ascii_letters+string.digits+'!#$%&()*+,-./:;<=>?@[]^_`{|}~', k=random.randint(min_length, max_length)))
        texts.append(t)
        file.write(t+'\n')
    return texts

def generate_audio(texts, tx):
    for i in range(len(texts)):
        tx.modulate_to_file(texts[i],'test_audio/{:03}.wav'.format(i))


def test_rx(rx, texts, standby = 60, interval = 10):
    test_y = open('testing_data.txt', 'r').readlines()
    for i in range(len(test_y)):
        test_y[i] = test_y[i].strip()
    
    
    text = ''
    succeed_activation = 0
    aborted_activation = 0
    succeed_transmission = 0
    incorrect_transmission = 0
    fault_was_detected = 0
    correct_transmission = 0
    fault_not_detected = 0
    received = []
    
    count = False
    i = 0
    start_time = time.time()
    interval_time = time.time()
    
    while (time.time() - start_time < standby):
        if (time.time() - interval_time >= interval):
            i += 1
            count = False
            interval_time = time.time()
            
        data, status = rx.read_frame(log = True)
        
        
        if status == 2 and count==False:
            succeed_activation += 1
            count = True
        if status == 3:
            aborted_activation += 1
            received.append('')
        elif status == 4:
            if data:
                text += data
                print(data, end=(''))
        elif status == 5:
            text = rx.received_data()[-1]
            received.append(text)
            print('Test Data: {} \t\t Result: {}'.format(test_y[i], text))
            if test_y[i] == text:
                correct_transmission += 1
                print('correct')
            else:
                fault_not_detected += 1
                print('incorrect')
        elif status == 6: 
            print('Fault was detected')
            fault_was_detected += 1
            received.append('')
    
    incorrect_transmission = fault_was_detected + aborted_activation + fault_not_detected
    print('Total Transmission:')


    