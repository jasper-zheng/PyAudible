#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:58:06 2021

@author: winter_camp
"""

import numpy as np
from math import pi
from scipy.io import wavfile


Fs = 44100 #Sampling Rate

BASE_FREQ = 1238 #Hz
SPACED_FREQ = 21.5 * 2 #Hz

BASE_CH2 = 1971
BASE_CH3 = 2703
BASE_CH4 = 3435
BASE_CH5 = 4124
BASE_CH6 = 4813
BASE_CH7 = 5545
BASE_CH8 = 6277

#BASE_CH_FREQ = [1238,1928,2616,3306,3994,4683,5372,6062]
BASE_CH_FREQ = [1238,1971,2703,3435,4124,4813,5545,6277]

CHANNEL_NUM = 8

#ACTIVE_FREQ = [1185,3984,6740]
ACTIVE_FREQ = [1185,4156,6957]

#ENDING_FREQ = [1206,4048,6740]
ENDING_FREQ = [1206,4222,6957]
TRANS_SPEED = 0.2 #sec
SAMPLE_RATE = 44100

chunk = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

#%%

class Transmitter(object):

    SHARED_CHANNEL = 2
    VOLUME = 1.0
    
    ch_freqs = []
    
    def __init__(self, speed = 'slow', volume = 1.0):
        if speed == 'slow':
            self.SHARED_CHANNEL = 2
        elif speed == 'medium':
            self.SHARED_CHANNEL = 4
        elif speed == 'fast':
            self.SHARED_CHANNEL = 8
        else:
            raise ParameterError
            
        self.VOLUME = volume
        
        for i in range(CHANNEL_NUM):
            channel_freq = []
            for n in range(16):
                channel_freq.append(BASE_CH_FREQ[i] + n * SPACED_FREQ)
            self.ch_freqs.append(channel_freq)
        
    def __str__(self):
        return ' - PyAudiable Transmitter - \nShared Channel: {}\nTransmitting Volume: {}'.format(self.SHARED_CHANNEL, self.VOLUME)
    
    
    
    def ch_freq_seq(self, binary_message, ch_number):
        adjusted_message = np.copy(binary_message)
        if (len(binary_message)%4 != 0):
            for i in range(4-len(binary_message)%4):
                adjusted_message = np.append(adjusted_message, [0])
        #print('original shape: %d' % (binary_message.shape)) 
        #print('adjusted shape: %d' % (adjusted_message.shape)) 
        
        freq_seq = []
        
        #print('adjusted_message: ')
        #print(np.array2string(adjusted_message.astype(int),max_line_width=np.inf,separator=''))
        for i in range(int(len(adjusted_message)/4)):
            this_chunk = np.array2string(adjusted_message.astype(int),max_line_width=np.inf,separator='')[1+i*4:1+(i+1)*4]

            for n in range(len(chunk)):             
                if (this_chunk == chunk[n]):
                    freq_seq.append(self.ch_freqs[ch_number][n])
        return freq_seq
    
    def text_to_bin(self, text):
        res = bin(int.from_bytes(text.encode(), 'big')).replace('b', '')
        m = np.zeros(len(res))
        for i in range(len(res)):
            m[i] = int(res[i])
        return m
    
    def fill_empty_bits(self, message):
        minimum_block_length = self.SHARED_CHANNEL * 4
        full_length = (int((len(message)-1) / minimum_block_length) + 1) * minimum_block_length
        return np.concatenate((message, np.zeros(full_length - len(message))), axis=None)
    
    def modulate(self, message):
        '''
        Generate a modulated audio waveform in ndarray format.

        Parameters
        ----------
        message : string
            The message you would like to modulate to audio.

        Returns
        -------
        fsk : ndarray
            Modulated waveform

        '''
        sym_num = len(self.text_to_bin(message))
        message = self.fill_empty_bits(self.text_to_bin(message))
        
        
        
        freq_seqs = []
        ch_msg = [] #2d array with [1,0,0,1,0....,0,1]
        #print(message)
        print(len(message))
        
        #create empty freqency channel
        for i in range(self.SHARED_CHANNEL):
            msg = np.zeros(int(len(message)/self.SHARED_CHANNEL))
            ch_msg.append(msg)
        '''
        #assign binary seqence to empty freqency channel
        for i in range(int(len(message)/4)):
            turn = (int(len(message)/4)-i) % self.SHARED_CHANNEL
            print('turn:{}'.format(turn))
            for n in range(4):
                ch_msg[turn][ int((i-turn)/self.SHARED_CHANNEL*4) + n ] = message[i*4+n]
        
        '''
        for i in range(int(len(message)/4)):
            turn = i % self.SHARED_CHANNEL
            for n in range(4):
                ch_msg[turn][ int(i/self.SHARED_CHANNEL)*4 + n ] = message[i*4+n]
        #print('ch_msg: {}'.format(ch_msg))   
        
        
        #assign freqency in herz into the 8 channels
        track_num = int(CHANNEL_NUM/self.SHARED_CHANNEL)
        for i in range(self.SHARED_CHANNEL):
            for j in range(track_num):
                freq_seqs.append(self.ch_freq_seq(ch_msg[i], j*self.SHARED_CHANNEL+i))
    
        sym_length = int(TRANS_SPEED * SAMPLE_RATE) # 8820
        #sym_num = len(freq_seqs[0]) # 11
        print('sym_num: {}'.format(sym_num))
        activation_info = [int(sym_num/100),int(sym_num%100/10),sym_num%100%10]
        
        T = float(format(((len(freq_seqs[0])+2) * TRANS_SPEED), '.2f')) #the length of the waveform (in sec)
        timeline = np.arange(0,T,1/Fs)
        
        signals = []
        
        for i in range(len(freq_seqs)):
            signal = np.zeros(sym_length*(len(freq_seqs[0])+2))
            if i==0:
                signal[0 : sym_length] = ACTIVE_FREQ[0]
                signal[(len(freq_seqs[0])+1)*sym_length : (len(freq_seqs[0])+2)*sym_length] = ENDING_FREQ[0]
            elif i==1:
                signal[0 : sym_length] = self.ch_freqs[1][activation_info[0]]
                signal[(len(freq_seqs[0])+1)*sym_length : (len(freq_seqs[0])+2)*sym_length] = self.ch_freqs[1][activation_info[0]]
            elif i==2:
                signal[0 : sym_length] = self.ch_freqs[2][activation_info[1]]
                signal[(len(freq_seqs[0])+1)*sym_length : (len(freq_seqs[0])+2)*sym_length] = self.ch_freqs[2][activation_info[1]]
            elif i==3:
                signal[0 : sym_length] = self.ch_freqs[3][activation_info[2]]
                signal[(len(freq_seqs[0])+1)*sym_length : (len(freq_seqs[0])+2)*sym_length] = self.ch_freqs[3][activation_info[2]]
            elif i==4:
                signal[0 : sym_length] = ACTIVE_FREQ[1]
                signal[(len(freq_seqs[0])+1)*sym_length : (len(freq_seqs[0])+2)*sym_length] = ENDING_FREQ[1]
            elif i==5:
                signal[0 : sym_length] = self.ch_freqs[i][self.SHARED_CHANNEL]
            elif i==6:
                signal[0 : sym_length] = self.ch_freqs[i][self.SHARED_CHANNEL]
            elif i==7:
                signal[0 : sym_length] = ACTIVE_FREQ[2]
                signal[(len(freq_seqs[0])+1)*sym_length : (len(freq_seqs[0])+2)*sym_length] = ENDING_FREQ[2]
                
            for n in range(len(freq_seqs[0])):
                signal[(n+1)*sym_length : (n+2)*sym_length] = freq_seqs[i][n]
    
            s = 2*pi * signal * timeline
            signals.append(s)
            
        fsk = np.sin(signals[0])/CHANNEL_NUM
        
        a = 1
        
        for i in range(len(signals)-1):
            fsk += a * np.sin(signals[i+1])/CHANNEL_NUM
            a = a * 0.9
        
        return fsk
    
    def modulate_to_file(self, message, filename):
        '''
        Generate a modulated audio waveform and save it as .wav format to file.

        Parameters
        ----------
        message : string
            The message you would like to modulate to audio.
        filename : string
            Name of the output wav file.

        Returns
        -------
        None.

        '''
        fsk = self.modulate(message)
        wavfile.write(filename, Fs, fsk)
        
    def modulate_and_play(self, message):
        i = 0
    
    
#%% 

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ParameterError(Error):
    
    def __init__(self, message = 'speed could only be slow, medium or fast'):
        self.message = message
        super().__init__(self.message)