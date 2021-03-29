#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:41:44 2021

@author: winter_camp
"""
import pyaudio
import numpy as np
#import matplotlib.pyplot as plt
import time

from scipy.fftpack import fft

class Receiver(object):
    
    CHUNK = 1024 * 2
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    
    FRAMES_PER_FFT = 16 # FFT takes average across how many frames
    SAMPLES_PER_FFT = CHUNK * FRAMES_PER_FFT
    FREQ_STEP = float(RATE)/SAMPLES_PER_FFT
    
    CHANNEL_NUMBER = 8
    SHARED_CHANNEL = 2
    TRACK_NUM = 4
    
    FRAME_TIME = 0.2
    
    active_freq_bin = [55,185,313]
    ending_freq_bin = [56,188,313]
    ending_channel_num = [0,4,7]
    
    d_channel_1 = [[53,57,58],[59,60],[61,62],[63,64],[65,66],[67,68],[69,70],[71,72],[73,74],[75,76],[77,78],[79,80],[81,82],[83,84],[85,86],[87,88]]
    d_channel_2 = [[89,90],[91,92],[93,94],[95,96],[97,98],[99,100],[101,102],[103,104],[105,106],[107,108],[109,110],[111,112],[113,114],[115,116],[117,118],[119,120]]
    d_channel_3 = [[121,122],[123,124],[125,126],[127,128],[129,130],[131,132],[133,134],[135,136],[137,138],[139,140],[141,142],[143,144],[145,146],[147,148],[149,150],[151,152]]
    d_channel_4 = [[153,154],[155,156],[157,158],[159,160],[161,162],[163,164],[165,166],[167,168],[169,170],[171,172],[173,174],[175,176],[177,178],[179,180],[181,182],[183,184]]
    d_channel_5 = [[185,186],[187,188],[189,190],[191,192],[193,194],[195,196],[197,198],[199,200],[201,202],[203,204],[205,206],[207,208],[209,210],[211,212],[213,214],[215,216]]
    d_channel_6 = [[217,218],[219,220],[221,222],[223,224],[225,226],[227,228],[229,230],[231,232],[233,234],[235,236],[237,238],[239,240],[241,242],[243,244],[245,246],[247,248]]
    d_channel_7 = [[249,250],[251,252],[253,254],[255,256],[257,258],[259,260],[261,262],[263,264],[265,266],[267,268],[269,270],[271,272],[273,274],[275,276],[277,278],[279,280]]
    d_channel_8 = [[281,282],[283,284],[285,286],[287,288],[289,290],[291,292],[293,294],[295,296],[297,298],[299,300],[301,302],[303,304],[305,306],[307,308],[309,310],[311,312,313]]
    d_channel_9 = [[314]]
    
    d_channel = []    
    chunk_list = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    
    activation_info = [[],[],[]]
    received_info = []
    ending_info = [[],[],[],[],[],[],[],[]]
    ending_mark = [0,0] #i0: ending pointer, i1:
    
    status = 0
    
    def __init__(self):
        self.d_channel.append(self.d_channel_1)
        self.d_channel.append(self.d_channel_2)
        self.d_channel.append(self.d_channel_3)
        self.d_channel.append(self.d_channel_4)
        self.d_channel.append(self.d_channel_5)
        self.d_channel.append(self.d_channel_6)
        self.d_channel.append(self.d_channel_7)
        self.d_channel.append(self.d_channel_8)
        self.d_channel.append(self.d_channel_9)
        
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(
            format = self.FORMAT,
            channels = self.CHANNELS,
            rate = self.RATE,
            input = True,
            output = True,
            frames_per_buffer = self.CHUNK
            )
        
        self.current_bins = []
        self.pointers = []
        self.recieved_bins = []
        self.fft = []
        self.retrieved_data = []
        for i in range(self.SHARED_CHANNEL):
            self.pointers.append(0)
            self.current_bins.append([0,0,0,0,0,0,0])
            self.recieved_bins.append([])
        
        print(self.stream)
    
    def callback(self, input_data, frame_count, time_info, flags):
    
        return (input_data, pyaudio.paContinue)

    def read_block(self, standby_time):
        '''
        Read the input audio (Blocking Mode):
            Standby and listen until all the equested frames have been recorded.

        Parameters
        ----------
        standby_time : int
            The requested time (in second).

        Returns
        -------
        retrieved_data: list
            Every retrieved data during the standby time

        '''
        frame_count = 0
        start_time = time.time()
        
        self.current_bins = []
        self.pointers = []
        self.recieved_bins = []

        for i in range(self.SHARED_CHANNEL):
            self.pointers.append(0)
            self.current_bins.append([0,0,0,0,0,0,0])
            self.recieved_bins.append([])

        while (time.time() - start_time < standby_time):
            self.read()
            frame_count += 1
        
        return self.retrieved_data
    
    
    def read(self, log = False):
        '''
        Read the input audio (Callback Mode):
            Called each frame to listen to the audio.

        Parameters
        ----------
        log : bool, optional
            If true, it will add a status flag to the returns, accompany with the retrived result. 
            The default is False.

        Returns
        -------
        retrieved_data: String
            The retrieved and demodulated data, empty if the receiver have not detected anything yet.
        
        status: int
            0: Unactivated
            1: Activating
            2: Activated, preparing
            3: Activation Failed, rollback to unactivated
            4: Listening
            5: Terminated, received auccessfully
            6: Terminated, received failed

        '''
        data = self.stream.read(self.CHUNK, exception_on_overflow = False)
        data_int = np.frombuffer(data, dtype = np.int16)
        self.fft = fft(data_int)
        freq_bins = []
        for i in range(self.SHARED_CHANNEL):
            candidate_freq = []
            for j in range(int(self.CHANNEL_NUMBER/self.SHARED_CHANNEL)):
                freq_bin = np.abs(self.fft[self.d_channel[j*self.SHARED_CHANNEL+i][0][0]:self.d_channel[j*self.SHARED_CHANNEL+i+1][0][0]]).argmax() + self.d_channel[j*self.SHARED_CHANNEL+i][0][0]
                candidate_freq.append(freq_bin)
            freq_bins.append(candidate_freq)
        self.status = self.update_statue(freq_bins,self.status)
        
        
        if log:
            if self.status == 3:
                self.status = 0
                return '', 3
            elif self.status == 5:
                self.status = 0
                return self.retrieved_data[-1], 5
            elif self.status == 6:
                self.status = 0
                return '', 6
            else:
                return '', self.status
        else:
            if self.status == 3:
                self.status = 0
                return ''
            elif self.status == 5:
                self.status = 0
                return self.retrieved_data[-1]
            elif self.status == 6:
                self.status = 0
                return ''
            else:
                return ''
        
        

    def most_frequent(self, List): 
        counter = 0
        num = List[0]
        for i in List: 
            curr_frequency = List.count(i) 
            if(curr_frequency> counter): 
                counter = curr_frequency 
                num = i 
        return num
    def get_bin_num(self, freq_bin,n):
        for i in range(16):
            if freq_bin in self.d_channel[n][i]:
                return i
        print('request {} in number {} channel'.format(freq_bin,n))
        return 99
    
    
    '''
    Status:
        0: Unactivated
        1: Activating
        2: Activated, Preparing
        3: Activation Failed, rollback to unactivated
        4: Listening
            4.5 (Hide): Terminating
        5: Terminated, Received Successfully
        6: Terminated, Received Failed
    '''
    def update_statue(self, freq_bins,status):
         # if the activation frequency is been detected three times, 
        if (status == 0):
            if (freq_bins[0][0] == self.active_freq_bin[0] and freq_bins[0][2] == self.active_freq_bin[1] and freq_bins[1][3] == self.active_freq_bin[2]):
                self.activation_info = [[],[],[]]
                self.received_info = []
                self.pointers[0] = 1
                status = 1
                print('activating...')
                self.activation_info[0].append(freq_bins[1][0])
                self.activation_info[1].append(freq_bins[0][1])
                self.activation_info[2].append(freq_bins[1][1])
        elif (status == 1):
            if (freq_bins[0][0] == self.active_freq_bin[0] and freq_bins[0][2] == self.active_freq_bin[1] and freq_bins[1][3] == self.active_freq_bin[2]):
                self.pointers[0] += 1
                self.activation_info[0].append(freq_bins[1][0])
                self.activation_info[1].append(freq_bins[0][1])
                self.activation_info[2].append(freq_bins[1][1])
                if (self.pointers[0] == 2):
                    self.current_bins = []
                    self.recieved_bins = []
                    for i in range(self.SHARED_CHANNEL):
                        self.current_bins.append([0,0,0,0,0,0,0])
                        self.recieved_bins.append([])
                        self.pointers[i] = 0
                    status = 2
                    #self.pointers[0] = 0
                    print("Activated, on preparing")
            else:
                status = 3
                print('activation failed')
        elif (status == 2):
            if (freq_bins[0][0] != self.active_freq_bin[0] and freq_bins[1][3] != self.active_freq_bin[2]):
                print(self.activation_info)
                self.received_info.append(100*self.get_bin_num(self.most_frequent(self.activation_info[0]),1) + 10*self.get_bin_num(self.most_frequent(self.activation_info[1]),2) + self.get_bin_num(self.most_frequent(self.activation_info[2]),3))
                print('Estimated length: {}'.format(self.received_info[0]))
                print('On recieving...')
                self.d_channel[0][0] = [57,58]
                #self.d_channel[7][15] = [311,312]
                status = self.check_channels(freq_bins)
            else:
                self.activation_info[0].append(freq_bins[1][0])
                self.activation_info[1].append(freq_bins[0][1])
                self.activation_info[2].append(freq_bins[1][1])
                       
        elif (status == 4):
            status = self.check_channels(freq_bins)
            
            if (self.ending_mark[0]>=1):
                self.ending_mark[0] += 1
                self.ending_info[0].append(freq_bins[0][0])
                self.ending_info[1].append(freq_bins[1][0])
                self.ending_info[2].append(freq_bins[0][1])
                self.ending_info[3].append(freq_bins[1][1])
                self.ending_info[4].append(freq_bins[0][2])
                self.ending_info[7].append(freq_bins[1][3])
                
                if self.ending_mark[0] == 5:
                    
                    validated = 0
                    for i in range(3):
                        count = 0
                        for info in self.ending_info[self.ending_channel_num[i]]:
                            if info == self.ending_freq_bin[i]:
                                count += 1
                                if count == 2:
                                    validated += 1
                                    break
                    if validated == 3:
                        #if validated ended
                        print('Recieved: {}, length: {}, {}'.format(self.copy_recieved_bins,len(self.copy_recieved_bins[0]),len(self.copy_recieved_bins[1])))
                        self.d_channel[0][0] = [53,57,58]
                        self.ending_mark[0] = 0
                        if(self.convert_result() == 1):
                            return 5
                        else:
                            return 6
                    else:
                        #if not ended
                        self.d_channel[0][0] = [57,58]
                        self.ending_mark[0] = 0
                
            elif (freq_bins[1][3] == self.ending_freq_bin[2]):
                
                print('detecting ending...')
                #if one of the ending bit appears, expande the fft scope, start monitoring for 5 frames
                #create copy of recieved_bin
                #undo the pointer
                self.ending_mark[0] = 1
                self.d_channel[0][0] = [56,57,58]
                self.ending_info = [[],[],[],[],[],[],[],[]]
                
                self.copy_recieved_bins = []
                for bins in self.recieved_bins:
                    copy_bins = bins.copy()
                    self.copy_recieved_bins.append(copy_bins)
                for pointer, current_bin, recieved_bin in zip(self.pointers, self.current_bins, self.copy_recieved_bins):
                    if pointer >= 3:
                        recieved_bin.append(current_bin[pointer-1])
        return status
    
    def check_channels(self, freq_bins):
        frame_result = []
        for freq_bin, current_bin, recieved_bin,i in zip(freq_bins,self.current_bins,self.recieved_bins,range(self.SHARED_CHANNEL)):
            freq_bin_nums = []
            for j in range(self.TRACK_NUM):
                freq_bin_nums.append(self.get_bin_num(freq_bin[j],j*self.SHARED_CHANNEL+i))
            frame_result.append(freq_bin_nums)
            freq_bin_num = self.most_frequent(freq_bin_nums)
            if (self.pointers[i]==0):
                current_bin[self.pointers[i]] = freq_bin_num
                self.pointers[i] += 1
            elif ( freq_bin_num == current_bin[self.pointers[i]-1]) or (self.pointers[i] < 3):
                #if this bit is the same as the last bit
                current_bin[self.pointers[i]] = freq_bin_num
                self.pointers[i] += 1
                if (self.pointers[i] == 7):
                    recieved_bin.append(current_bin[self.pointers[i]-1])
                    current_bin[0] = freq_bin_num
                    self.pointers[i] = 3
            else:
                #if new bit appears,
                number = self.most_frequent(current_bin[0:self.pointers[i]-1])
                recieved_bin.append(number)
                current_bin[0] = freq_bin_num
                self.pointers[i] = 1
        print(frame_result)
        
        return 4
        
    def bin_to_ascii(self,bin_data):
        st = ''
        for i in range(len(bin_data)):
            st += str(int(bin_data[i]))
        st = st[:1]+'b'+st[1:]
        n = int(st, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    
    def convert_result(self):
        if (len(self.copy_recieved_bins[0]) != len(self.copy_recieved_bins[1])):
            print('recieve failed')
            return 0
        else:
            binary = ''
            for i in range(len(self.copy_recieved_bins[0])):
                for j in range(self.SHARED_CHANNEL):
                    binary += self.chunk_list[self.copy_recieved_bins[j][i]]
            result = self.bin_to_ascii(binary)
            self.retrieved_data.append(result)
            print(result)
            return 1