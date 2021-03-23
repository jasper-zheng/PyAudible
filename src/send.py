#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:41:47 2020

@author: winter_camp
"""
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy.io import wavfile
#import gen_binary as gb
plt.close('all')


def gen_binary(sym_length = 500, sym_num = 16):
    rand_n = np.random.rand(sym_num)
    rand_n[np.where(rand_n >= 0.5)] = 1
    rand_n[np.where(rand_n < 0.5)] = 0
    
    signal = np.zeros(sym_length * sym_num)
    id_n = np.where(rand_n == 1)
    for i in id_n[0]:
        temp = int(i * sym_length)
        signal[temp : temp+sym_length] = 1
    return signal


#
Fs = 44100;
T = 2;
fc = 500; #carrier freq
t = np.arange(0,T,1/Fs) #time axis (s)
#sampleRate = 44100

#generate binary signal waveform
sym_duration = 0.1 #unit duration 单段unit时间间隔 (s)
sym_length = int(sym_duration * Fs) #single unit total samples 单段unit采样量

sym_num = int(np.floor(np.size(t) / sym_length)) #number of units in binary signal 多少段信息unit

binary_signal = gen_binary(sym_length, sym_num) #全部信息unit
binary_signal+=gen_binary(sym_length, sym_num)
binary_signal+=gen_binary(sym_length, sym_num)

binary_signal_2 = gen_binary(sym_length, sym_num) #全部信息unit
binary_signal_2 += gen_binary(sym_length, sym_num)
binary_signal_2 += gen_binary(sym_length, sym_num)


plt.figure(figsize=(16,10))
plt.subplot(211)
plt.title('Random Binary Signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.plot(binary_signal)
plt.show()

plt.figure(figsize=(16,10))
plt.subplot(211)
plt.title('Random Binary Signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.plot(binary_signal_2)
plt.show()

# FSK

f = fc + fc * binary_signal
s = 2*pi * f * t
fsk = np.sin(s)

plt.subplot(212)
plt.title('FSK Signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.plot(t, fsk)
plt.tight_layout()

#wavfile.write('Sine.wav', Fs, fsk)


'''
ascii -> binary message

binary message -> binary signal (flatten)

binary signal -> frequency signal (Hzs)

frequency signal -> angle

angle -> fsk


'''

BASE_FREQ = 1238 #Hz
SPACED_FREQ = 21.5 * 2 #Hz

BASE_CH2 = 1928
BASE_CH3 = 2616
BASE_CH4 = 3306
BASE_CH5 = 3994
BASE_CH6 = 4683
BASE_CH7 = 5372
BASE_CH8 = 6062

BASE_CH_FREQ = [1238,1928,2616,3306,3994,4683,5372,6062]

CHANNEL_NUM = 8

SHARED_CHANNEL = 2

ACTIVE_FREQ = [1185,3984,6740]
ENDING_FREQ = 1142
TRANS_SPEED = 0.2 #s
SAMPLE_RATE = 44100



def generate_random_message(length = 4*8):
    binary_str = gen_binary(1,length)
    return binary_str

def generate_freq_seq(binary_message):
    adjusted_message = np.copy(binary_message)
    if (len(binary_message)%4 != 0):
        for i in range(4-len(binary_message)%4):
            adjusted_message = np.append(adjusted_message, [0])
    print('original shape: %d' % (binary_message.shape)) 
    print('adjusted shape: %d' % (adjusted_message.shape)) 
    freq_seq = []
    freq_seq_ch2 = []
    freq_seq_ch3 = []
    freq_seq_ch4 = []
    
    print('adjusted_message: ')
    print(adjusted_message)
    for i in range(int(len(adjusted_message)/4)):
        #chunk = '' + int(adjusted_message[0 + i*4]) + int(adjusted_message[1 + i*4]) + int(adjusted_message[2 + i*4]) + int(adjusted_message[3 + i*4])
        this_chunk = np.array2string(adjusted_message.astype(int),separator='')[1+i*4:5+i*4]
        #print('chunk: ')
        #print(this_chunk)
        for n in range(len(chunk)):
            if (this_chunk == chunk[n]):
                freq_seq.append(ch1_freq[n])
                freq_seq_ch2.append(ch2_freq[n])
                freq_seq_ch3.append(ch3_freq[n])
                freq_seq_ch4.append(ch4_freq[n])
    return freq_seq, freq_seq_ch2, freq_seq_ch3, freq_seq_ch4, len(binary_message)

def ch_freq_seq(binary_message, ch_number):
    adjusted_message = np.copy(binary_message)
    if (len(binary_message)%4 != 0):
        for i in range(4-len(binary_message)%4):
            adjusted_message = np.append(adjusted_message, [0])
    print('original shape: %d' % (binary_message.shape)) 
    print('adjusted shape: %d' % (adjusted_message.shape)) 
    
    freq_seq = []
    
    print('adjusted_message: ')
    print(np.array2string(adjusted_message.astype(int),max_line_width=np.inf,separator=''))
    for i in range(int(len(adjusted_message)/4)):
        this_chunk = np.array2string(adjusted_message.astype(int),max_line_width=np.inf,separator='')[1+i*4:1+(i+1)*4]
        #print(this_chunk)
        for n in range(len(chunk)):
            
            if (this_chunk == chunk[n]):
                freq_seq.append(ch_freqs[ch_number][n])
                #print(n)
        #print('count')
    return freq_seq

def ascii_to_bin(text):
    res = bin(int.from_bytes(text.encode(), 'big')).replace('b', '')
    m = np.zeros(len(res))
    for i in range(len(res)):
        m[i] = int(res[i])
    return m

def bin_to_ascii(bin_data):
    st = ''
    for i in range(len(message)):
        st += str(int(bin_data[i]))
    st = st[:1]+'b'+st[1:]
    n = int(st, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

chunk = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']


ch_freqs = []

for i in range(CHANNEL_NUM):
    channel_freq = []
    for n in range(16):
        channel_freq.append(BASE_CH_FREQ[i] + n * SPACED_FREQ)
    ch_freqs.append(channel_freq)

'''
for i in range(16):
    ch1_freq.append(BASE_FREQ + i * SPACED_FREQ)
    ch2_freq.append(BASE_CH2 + i * SPACED_FREQ)
    ch3_freq.append(BASE_CH3 + i * SPACED_FREQ)
    ch4_freq.append(BASE_CH4 + i * SPACED_FREQ)
'''

message = generate_random_message(32)
message = np.array([0,0,0,0, 0,0,0,1, 0,0,1,0, 0,0,1,1, 0,1,0,0, 0,1,0,1, 0,1,1,0, 0,1,1,1, 
                    1,0,0,0, 1,0,0,1, 1,0,1,0, 1,0,1,1, 1,1,0,0, 1,1,0,1, 1,1,1,0, 1,1,1,1])
message = ascii_to_bin('world hello')
#message = ascii_to_bin('Documents')

freq_seqs = []
ch_msg = []

#create empty message channel
for i in range(SHARED_CHANNEL):
    msg = np.zeros(int(len(message)/SHARED_CHANNEL))
    ch_msg.append(msg)


for i in range(int(len(message)/4)):
    turn = (int(len(message)/4)-i) % SHARED_CHANNEL
    for n in range(4):
        ch_msg[turn][ int((i-turn)/SHARED_CHANNEL*4) + n ] = message[i*4+n]
        
        
print('stop')


track_num = int(CHANNEL_NUM/SHARED_CHANNEL)
for i in range(SHARED_CHANNEL):
    for j in range(track_num):
        freq_seqs.append(ch_freq_seq(ch_msg[i], j*SHARED_CHANNEL+i))

print('stop')

sym_length = int(TRANS_SPEED * SAMPLE_RATE)
sym_num = len(freq_seqs[0])
activation_info = [int(sym_num/100),int(sym_num%100/10),sym_num%100%10]

T = float(format(((len(freq_seqs[0])+2) * TRANS_SPEED), '.2f'))
timeline = np.arange(0,T,1/Fs)


signals = []
#s_channel = []

for i in range(len(freq_seqs)):
    signal = np.zeros(sym_length*(len(freq_seqs[0])+2))
    if i==0:
        signal[0 : sym_length] = ACTIVE_FREQ[0]
        signal[(len(freq_seqs[0])+1)*sym_length : (len(freq_seqs[0])+2)*sym_length] = ENDING_FREQ
    elif i==1:
        signal[0 : sym_length] = ch_freqs[1][activation_info[0]]
    elif i==2:
        signal[0 : sym_length] = ch_freqs[2][activation_info[1]]
    elif i==3:
        signal[0 : sym_length] = ch_freqs[3][activation_info[2]]
    elif i==4:
        signal[0 : sym_length] = ACTIVE_FREQ[1]
    elif i==7:
        signal[0 : sym_length] = ACTIVE_FREQ[2]
    for n in range(len(freq_seqs[0])):
        signal[(n+1)*sym_length : (n+2)*sym_length] = freq_seqs[i][n]
    s = 2*pi * signal * timeline
    signals.append(s)



'''
for i in range(len(freq_seq)):
    signal[(i+1)*sym_length : (i+2)*sym_length] = freq_seq[i]
    signal_2[(i+1)*sym_length : (i+2)*sym_length] = freq_seq_ch2[i]
    signal_3[(i+1)*sym_length : (i+2)*sym_length] = freq_seq_ch3[i]
    signal_4[(i+1)*sym_length : (i+2)*sym_length] = freq_seq_ch4[i]
    
signal[(len(freq_seq)+1)*sym_length : (len(freq_seq)+2)*sym_length] = ENDING_FREQ
signal_2[(len(freq_seq)+1)*sym_length : (len(freq_seq)+2)*sym_length] = ENDING_FREQ
signal_3[(len(freq_seq)+1)*sym_length : (len(freq_seq)+2)*sym_length] = ENDING_FREQ
signal_4[(len(freq_seq)+1)*sym_length : (len(freq_seq)+2)*sym_length] = ENDING_FREQ

s = 2*pi * signal * timeline
s_2 = 2*pi * signal_2 * timeline
s_3 = 2*pi * signal_3 * timeline
s_4 = 2*pi * signal_4 * timeline
'''
fsk = np.sin(signals[0])/CHANNEL_NUM

for i in range(len(signals)-1):
    fsk += np.sin(signals[i+1])/CHANNEL_NUM
    
    
#fsk = np.sin(signals[0])/2 + np.sin(signals[1])/2 
#fsk = np.sin(signals[0])/2

wavfile.write('Sine05.wav', Fs, fsk)


