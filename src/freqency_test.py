#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:41:44 2021

@author: winter_camp
"""
import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time

from scipy.fftpack import fft, fftfreq

#%matplotlib qt5

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

FRAMES_PER_FFT = 16 # FFT takes average across how many frames
SAMPLES_PER_FFT = CHUNK * FRAMES_PER_FFT
FREQ_STEP = float(RATE)/SAMPLES_PER_FFT

CHANNEL_NUMBER = 4
SHARED_CHANNEL = 2

FRAME_TIME = 0.2

##############



def callback(input_data, frame_count, time_info, flags):
    
    return (input_data, pyaudio.paContinue)


##############

'''
fig, (ax, ax2) = plt.subplots(2)


p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
    )

x = np.arange(0, 2 * CHUNK, 2)
x_fft = np.linspace(0, RATE, CHUNK)

#line, = ax.plot(x, np.random.rand(CHUNK), '-', lw = 1)
line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK), '-', lw = 1)

#ax.set_ylim(-2**15, 2**15)
#ax.set_xlim(0, CHUNK)
ax2.set_xlim(20, RATE/2)
ax2.set_ylim(0, 10)

#plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 2**15])

plt.show(block=False)
fig.canvas.draw()

frame_count = 0
frame_num = 0
start_time = time.time()
frame_start_time = time.time()
freqs = fftfreq(CHUNK)
'''


active_freq_bin = 55
ending_freq_bin = 53
#d_channel = [57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72]
d_channel_1 = [[53,57,58],[59,60],[61,62],[63,64],[65,66],[67,68],[69,70],[71,72],[73,74],[75,76],[77,78],[79,80],[81,82],[83,84],[85,86],[87,88]]
d_channel_2 = [[89,90],[91,92],[93,94],[95,96],[97,98],[99,100],[101,102],[103,104],[105,106],[107,108],[109,110],[111,112],[113,114],[115,116],[117,118],[119,120]]
d_channel_3 = [[121,122],[123,124],[125,126],[127,128],[129,130],[131,132],[133,134],[135,136],[137,138],[139,140],[141,142],[143,144],[145,146],[147,148],[149,150],[151,152]]
d_channel_4 = [[153,154],[155,156],[157,158],[159,160],[161,162],[163,164],[165,166],[167,168],[169,170],[171,172],[173,174],[175,176],[177,178],[179,180],[181,182],[183,184]]
d_channel_5 = [[185,186],[187,188],[189,190],[191,192],[193,194],[195,196],[197,198],[199,200],[201,202],[203,204],[205,206],[207,208],[209,210],[211,212],[213,214],[215,216]]
d_channel_6 = [[217,218],[219,220],[221,222],[223,224],[225,226],[227,228],[229,230],[231,232],[233,234],[235,236],[237,238],[239,240],[241,242],[243,244],[245,246],[247,248]]
d_channel_7 = [[249,250],[251,252],[253,254],[255,256],[257,258],[259,260],[261,262],[263,264],[265,266],[267,268],[269,270],[271,272],[273,274],[275,276],[277,278],[279,280]]
d_channel_8 = [[281,282],[283,284],[285,286],[287,288],[289,290],[291,292],[293,294],[295,296],[297,298],[299,300],[301,302],[303,304],[305,306],[307,308],[309,310],[311,312]]
d_channel_9 = [[313]]

d_channel = []

d_channel.append(d_channel_1)
d_channel.append(d_channel_2)
d_channel.append(d_channel_3)
d_channel.append(d_channel_4)
d_channel.append(d_channel_5)
d_channel.append(d_channel_6)
d_channel.append(d_channel_7)
d_channel.append(d_channel_8)
d_channel.append(d_channel_9)

chunk_list = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

class Reciever(object):
    
    CHUNK = 1024 * 2
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    
    FRAMES_PER_FFT = 16 # FFT takes average across how many frames
    SAMPLES_PER_FFT = CHUNK * FRAMES_PER_FFT
    FREQ_STEP = float(RATE)/SAMPLES_PER_FFT

    CHANNEL_NUMBER = 4
    SHARED_CHANNEL = 2

    FRAME_TIME = 0.2
    
    active_freq_bin = 55
    ending_freq_bin = 53
    
    d_channel_1 = [[53,57,58],[59,60],[61,62],[63,64],[65,66],[67,68],[69,70],[71,72],[73,74],[75,76],[77,78],[79,80],[81,82],[83,84],[85,86],[87,88]]
    d_channel_2 = [[89,90],[91,92],[93,94],[95,96],[97,98],[99,100],[101,102],[103,104],[105,106],[107,108],[109,110],[111,112],[113,114],[115,116],[117,118],[119,120]]
    d_channel_3 = [[121,122],[123,124],[125,126],[127,128],[129,130],[131,132],[133,134],[135,136],[137,138],[139,140],[141,142],[143,144],[145,146],[147,148],[149,150],[151,152]]
    d_channel_4 = [[153,154],[155,156],[157,158],[159,160],[161,162],[163,164],[165,166],[167,168],[169,170],[171,172],[173,174],[175,176],[177,178],[179,180],[181,182],[183,184]]
    d_channel_5 = [[185,186],[187,188],[189,190],[191,192],[193,194],[195,196],[197,198],[199,200],[201,202],[203,204],[205,206],[207,208],[209,210],[211,212],[213,214],[215,216]]
    d_channel_6 = [[217,218],[219,220],[221,222],[223,224],[225,226],[227,228],[229,230],[231,232],[233,234],[235,236],[237,238],[239,240],[241,242],[243,244],[245,246],[247,248]]
    d_channel_7 = [[249,250],[251,252],[253,254],[255,256],[257,258],[259,260],[261,262],[263,264],[265,266],[267,268],[269,270],[271,272],[273,274],[275,276],[277,278],[279,280]]
    d_channel_8 = [[281,282],[283,284],[285,286],[287,288],[289,290],[291,292],[293,294],[295,296],[297,298],[299,300],[301,302],[303,304],[305,306],[307,308],[309,310],[311,312]]
    d_channel_9 = [[313]]
    
    d_channel = []    
    chunk_list = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    
    def __init__(self):
        d_channel.append(d_channel_1)
        d_channel.append(d_channel_2)
        d_channel.append(d_channel_3)
        d_channel.append(d_channel_4)
        d_channel.append(d_channel_5)
        d_channel.append(d_channel_6)
        d_channel.append(d_channel_7)
        d_channel.append(d_channel_8)
        d_channel.append(d_channel_9)
        
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(
            format = self.FORMAT,
            channels = self.CHANNELS,
            rate = self.RATE,
            input = True,
            output = True,
            frames_per_buffer = self.CHUNK
            )
        
    def start_listen(self):
        frame_count = 0
        frame_num = 0
        start_time = time.time()
        frame_start_time = time.time()
        freqs = fftfreq(self.CHUNK)
        
        status = 0
        current_bins = []
        pointers = []
        recieved_bins = []

        for i in range(self.SHARED_CHANNEL):
            pointers.append(0)
            current_bins.append([0,0,0,0,0,0,0])
            recieved_bins.append([])
            
        while (time.time()-start_time < 30):
            while (time.time() - frame_start_time < 0.2):
                frame_num += 1
                data = self.stream.read(self.CHUNK, exception_on_overflow = False)
                data_int = np.frombuffer(data, dtype = np.int16)
                y_fft = fft(data_int)
                freq_bins = []
                '''
                for i in range(SHARED_CHANNEL):
                    freq_bin = np.abs(y_fft[d_channel[i][0][0]:d_channel[i+1][0][0]]).argmax() + d_channel[i][0][0]
                    freq_bins.append(freq_bin)
                    '''
                freq_bin = np.abs(y_fft[30:400]).argmax() + 30
                #freq = freqs[freq_bins[0]]
                freq_in_hertz = abs(freq_bin * RATE)
                frame_count += 1
                print(freq_bin)
                #status = update_statue(freq_bins,status)

            frame_start_time = time.time()
            frame_num = 0
        
        return recieved_bins

    def most_frequent(List): 
        counter = 0
        num = List[0] 

        for i in List: 
            curr_frequency = List.count(i) 
            if(curr_frequency> counter): 
                counter = curr_frequency 
                num = i 

        return num
    
    def get_bin_num(freq_bin,n):
        for i in range(16):
            if freq_bin in d_channel[n][i]:
                return i
        return 99
    
    def update_statue(freq_bins,status):
        if (status == 0):
            if (freq_bins[0] == active_freq_bin):
                current_bins[0][0] = freq_bins[0]
                status = 1
                print('activating...')
                pointers[0] = 1
        elif (status == 1):
            if (freq_bins[0] == active_freq_bin):
                current_bins[0][pointers[0]] = freq_bins[0]
                pointers[0] += 1
                if (pointers[0] == 3):
                    status = 2
                    pointers[0] = 0
                    print("Activated, on preparing")
            else:
                status = 0
                print('activation failed')
        elif (status == 2):
            if (freq_bins[0] != active_freq_bin):
                for i in range(SHARED_CHANNEL):
                    current_bins[i][0] = get_bin_num(freq_bins[i],i)
                    pointers[i] = 1
                status = 3
                #recieved_count = 1
                print('On recieving...')
        elif (status == 3):
            status = check_channels(freq_bins)

        return status
    
    def check_channels(freq_bins):
        #if ending bit appears
        if (freq_bins[0] == ending_freq_bin):

            for pointer, current_bin, recieved_bin in zip(pointers, current_bins, recieved_bins):
                recieved_bin.append(current_bin[pointer-1])

            status = 0
            pointers[0] = 0
            print('Recieved: {}, length: {}'.format(recieved_bins,len(recieved_bins[0])))
            return 0
        
        else:
            for freq_bin, current_bin, recieved_bin,i in zip(freq_bins,current_bins,recieved_bins,range(SHARED_CHANNEL)):   
                freq_bin_num = get_bin_num(freq_bin,i)
                
                if (freq_bin_num == current_bin[pointers[i]-1]) or (pointers[i] < 3):
                    #if this bit is the same as the last bit
                    current_bin[pointers[i]] = freq_bin_num
                    pointers[i] += 1
                    if (pointers[i] == 7):
                        recieved_bin.append(current_bin[pointers[i]-1])
                        current_bin[0] = freq_bin_num
                        pointers[i] = 3

                else:
                    #if new bit appears,
                    number = most_frequent(current_bin[0:pointers[i]-1])
                    recieved_bin.append(number)
                    current_bin[0] = freq_bin_num
                    pointers[i] = 1

            return 3
    

    
    
'''
status:
0: inactive
1: activating
2: on preparing
3: recieving
'''
status = 0
#current_bin = [0,0,0,0,0,0,0]
current_bins = []
#pointer = 0
pointers = []
recieved_bins = []

for i in range(SHARED_CHANNEL):
    pointers.append(0)
    current_bins.append([0,0,0,0,0,0,0])
    recieved_bins.append([])
#print(pointers)

def get_bin_num(freq_bin,n):
    for i in range(16):
        if freq_bin in d_channel[n][i]:
            return i
    return 99

def check_start(freq_bin,status,pointer):
    freq_bin_num = get_bin_num(freq_bin)
    if (status == 0):
        if (freq_bin == active_freq_bin):
            current_bin[0] = freq_bin
            status = 1
            print('activating...')
            pointer = 1
    elif (status == 1):
        if (freq_bin == active_freq_bin):
            current_bin[pointer] = freq_bin
            pointer += 1
            if (pointer == 3):
                status = 2
                pointer = 0
                print("Activated, on preparing")
        else:
            status = 0
            print('activation failed')
    elif (status == 2):
        if (freq_bin != active_freq_bin):
            current_bin[0] = freq_bin_num
            pointer = 1
            status = 3
            #recieved_count = 1
            print('On recieving...')
    elif (status == 3):
        
        if (freq_bin == ending_freq_bin):
            recieved_bin.append(current_bin[pointer-1])
            status = 0
            pointer = 0
            print('Recieved: {}, length: {}'.format(recieved_bin,len(recieved_bin)))
            
        elif (freq_bin_num == current_bin[pointer-1]) or (pointer < 3):
            #if this bit is the same as the last bit
            current_bin[pointer] = freq_bin_num
            pointer += 1
            if (pointer == 7):
                recieved_bin.append(current_bin[pointer-1])
                current_bin[0] = freq_bin_num
                pointer = 3

        else:
            #if new bit appears,
            number = most_frequent(current_bin[0:pointer-1])
            recieved_bin.append(number)
            current_bin[0] = freq_bin_num
            pointer = 1
        #recieved_count += 1
        
    return status,pointer


def update_statue(freq_bins,status):
    if (status == 0):
        if (freq_bins[0] == active_freq_bin):
            current_bins[0][0] = freq_bins[0]
            status = 1
            print('activating...')
            pointers[0] = 1
    elif (status == 1):
        if (freq_bins[0] == active_freq_bin):
            current_bins[0][pointers[0]] = freq_bins[0]
            pointers[0] += 1
            if (pointers[0] == 3):
                status = 2
                pointers[0] = 0
                print("Activated, on preparing")
        else:
            status = 0
            print('activation failed')
    elif (status == 2):
        if (freq_bins[0] != active_freq_bin):
            for i in range(SHARED_CHANNEL):
                current_bins[i][0] = get_bin_num(freq_bins[i],i)
                pointers[i] = 1
            status = 3
            #recieved_count = 1
            print('On recieving...')
    elif (status == 3):
        status = check_channels(freq_bins)
    
    return status
            

def check_channels(freq_bins):
    #if ending bit appears
    if (freq_bins[0] == ending_freq_bin):
        
        for pointer, current_bin, recieved_bin in zip(pointers, current_bins, recieved_bins):
            recieved_bin.append(current_bin[pointer-1])
        
        status = 0
        pointers[0] = 0
        print('Recieved: {}, length: {}'.format(recieved_bins,len(recieved_bins[0])))
        return 0
    else:
        for freq_bin, current_bin, recieved_bin,i in zip(freq_bins,current_bins,recieved_bins,range(SHARED_CHANNEL)):
            freq_bin_num = get_bin_num(freq_bin,i)
            #print(freq_bin_num)
            #print(current_bin[pointers[i]-1])
            #print(pointers[i])
            if (freq_bin_num == current_bin[pointers[i]-1]) or (pointers[i] < 3):
                #if this bit is the same as the last bit
                current_bin[pointers[i]] = freq_bin_num
                pointers[i] += 1
                #print(pointers[i])
                if (pointers[i] == 7):
                    recieved_bin.append(current_bin[pointers[i]-1])
                    current_bin[0] = freq_bin_num
                    pointers[i] = 3
                    
            else:
                #if new bit appears,
                number = most_frequent(current_bin[0:pointers[i]-1])
                recieved_bin.append(number)
                current_bin[0] = freq_bin_num
                pointers[i] = 1
                #print(number)
            #print('---')
        return 3
     
        
r = Reciever()

print("hi")

r.start_listen()
'''
01 update statue
02 if bins[0]==53:
03     result_each_bins = [(SHARED_CHANNEL, Length)
04     for bin in bins:
05          result_each_bins.append(check_channel())
06          

while (time.time()-start_time < 30):
    
    while (time.time() - frame_start_time < 0.2):
        frame_num += 1
        data = stream.read(CHUNK, exception_on_overflow = False)
        #data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype = 'b')[::2] + 128
        data_int = np.frombuffer(data, dtype = np.int16)
        #line.set_ydata(data_int)

        y_fft = fft(data_int)
        
        
        #freq_bin = np.abs(y_fft[52:89]).argmax()+52
        freq_bins = []
        for i in range(SHARED_CHANNEL):
            freq_bin = np.abs(y_fft[d_channel[i][0][0]:d_channel[i+1][0][0]]).argmax() + d_channel[i][0][0]
            freq_bins.append(freq_bin)
        
        freq = freqs[freq_bins[0]]
        freq_in_hertz = abs(freq * RATE)
        line_fft.set_ydata(np.abs(y_fft[0:CHUNK]) * 2 / (256 * CHUNK) )

        #ax.draw_artist(ax.patch)
        #ax.draw_artist(line)
        ax2.draw_artist(ax2.patch)
        ax2.draw_artist(line_fft)
        #ax2.text(5,5,freq_in_hertz)
        print('{} : {:7.2f} Hz {}'.format(frame_num, freq_in_hertz, np.abs(y_fft).argmax()))
        fig.canvas.blit()

        #fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
        
        #status,pointer = check_start(freq_bins[0],status,pointer)
        #status = update_statue(freq_bins,status)
    
    frame_start_time = time.time()
    frame_num = 0

print(frame_count/30)
'''
#data = stream.read(CHUNK)
#data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype = 'b')[::2] + 127

#ax.plot(data_int, '-')
#plt.show()