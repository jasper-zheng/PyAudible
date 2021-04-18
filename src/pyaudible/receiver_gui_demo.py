#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:19:52 2021

@author: winter_camp
"""

import tkinter as tk

import pyaudio
#import matplotlib
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
import time

import numpy as np

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.animation as animation

import PyA_Receiver as pyaudible

#matplotlib.use("TkAgg")

#%matplotlib TkAgg

CHUNK = 1024 * 2
FILTERED_FREQ = 500
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

FRAMES_PER_FFT = 16 # FFT takes average across how many frames
SAMPLES_PER_FFT = CHUNK * FRAMES_PER_FFT
FREQ_STEP = float(RATE)/SAMPLES_PER_FFT

CHANNEL_NUMBER = 4
SHARED_CHANNEL = 2

FRAME_TIME = 0.2




root = tk.Tk()
root.wm_title("Embedding in Tk")

'''
def callback(input_data, frame_count, time_info, flags):
    
    return (input_data, pyaudio.paContinue)
'''
fig, ax2 = plt.subplots(figsize=(4,1.5))
'''
p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
    )
'''
x = np.arange(0, 2 * CHUNK, 2)
x_fft = np.linspace(0, RATE, CHUNK)

line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK), '-', lw = 1)

ax2.set_xlim(20, RATE/2)
ax2.set_ylim(0, 5)
plt.axis('off')

canvas = FigureCanvasTkAgg(fig, master=root)
#plt.show(block=False)
fig.canvas.draw()

frame_count = 0
frame_num = 0
start_time = time.time()
frame_start_time = time.time()
#freqs = fftfreq(CHUNK)

'''
while (time.time()-start_time < 30):
    
        data = stream.read(CHUNK, exception_on_overflow = False)
        data_int = np.frombuffer(data, dtype = np.int16)

        y_fft = fft(data_int)

        line_fft.set_ydata(np.abs(y_fft[0:CHUNK]) * 2 / (256 * CHUNK) )

        ax2.draw_artist(ax2.patch)
        ax2.draw_artist(line_fft)
        
        fig.canvas.blit()

        fig.canvas.flush_events()
        frame_count += 1
    
print(frame_count/30)
'''



canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)


button = tk.Button(master=root, text="Quit", command=root.quit)
button.pack(side=tk.BOTTOM)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

frame_time = time.time()


rx = pyaudible.Receiver()



while (time.time()-start_time < 30):
    '''
    data = stream.read(CHUNK, exception_on_overflow = False)
    data_int = np.frombuffer(data, dtype = np.int16)
    '''
    rx.read_frame()
    y_fft = rx.get_fft()
    #y_fft = fft(data_int)
    #y_fft[0:20] = 0

    while (time.time()-frame_time >= 0.1):
        line_fft.set_ydata(np.abs(y_fft[0:CHUNK]) * 2 / (256 * CHUNK) )
    
        ax2.draw_artist(ax2.patch)
        ax2.draw_artist(line_fft)
        
        fig.canvas.blit()

        fig.canvas.flush_events()
        frame_time = time.time()
        root.update_idletasks()
        root.update()
    
    frame_count += 1
    
    

print(frame_count/30)

