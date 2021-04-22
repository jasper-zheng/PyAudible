#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:19:52 2021

@author: winter_camp
"""

import tkinter as tk
import tkinter.scrolledtext as st

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

from pyaudible import receiver

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


class App(object):
    
    display = ''
    notification = ''
    notification_framecount = 0
    received = []

    
    def activate(self):
        if self.status==-1:
            self.btn_activate.config(text="Stop",fg='red')
            self.status = 0
        else:
            self.btn_activate.config(text="Activate",fg='black')
            self.status = -1
            self.lbl_display['text'] = ''
            self.display = ''
        print('activate')
        return 0
    
    def __init__(self):
        self.status=-1
        self.root = tk.Tk()
        self.root.wm_title("Receiver GUI Demo")
        
        self.text_area = st.ScrolledText(self.root,
                                         width = 5,
                                         height = 20)
        self.text_area.pack(fill=tk.X)
        
        self.text_area.configure(state ='disabled')
        
        self.btn_activate = tk.Button(master=self.root, text="Activate", command=self.activate)
        self.btn_activate.pack(fill=tk.X)
        
        self.lbl_status = tk.Label(master=self.root, text="Click the button to start receiver")
        self.lbl_status.pack(fill=tk.X)
        self.lbl_display = tk.Label(master=self.root, text="", fg="grey")
        self.lbl_display.pack(fill=tk.X)
        
        self.fig, self.ax2 = plt.subplots(figsize=(4,1.5))
        x = np.arange(0, 2 * CHUNK, 2)
        x_fft = np.linspace(0, RATE, CHUNK)
        self.line_fft, = self.ax2.semilogx(x_fft, np.zeros(CHUNK), '-', lw = 0.5,color="black")
        self.ax2.set_xlim(20, RATE/2)
        self.ax2.set_ylim(0, 5)
        self.ax2.set_facecolor((0.925,0.925,0.925))
        self.fig.patch.set_facecolor((0.925,0.925,0.925))
        plt.axis('off')
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.fig.canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def handle_status(self, data,received_data):
        if self.status == 0:
            self.lbl_status['text'] = 'Waiting for a transmission...'
        elif self.status == 1:
            self.lbl_display['text'] = ''
            self.display = ''
            self.notification_framecount = 0
            self.lbl_status['text'] = 'Connecting...'
           
        elif self.status == 3:
            self.notification = 'Connection Failed, increase volume'
            self.notification_framecount = 1
        
        elif self.status == 4:
            if data:
                self.display += data
            self.lbl_status['text'] = 'Listening...'
            self.lbl_display['text'] = self.display
        elif self.status == 5:
            self.notification = 'Text Received Successfully!'
            self.notification_framecount = 1
            self.received.append((received_data[-1],time.asctime( time.localtime(time.time()) )))
            
            self.update_text()
            
        elif self.status == 6:
            self.notification = 'Transmission failed, try again'
            self.notification_framecount = 1
            
        if self.notification_framecount>0 and self.notification_framecount<60:
            self.lbl_status['text'] = self.notification
            self.notification_framecount += 1
        elif self.notification_framecount >=60:
            self.notification_framecount = 0
            self.lbl_display['text'] = ''
            self.display = ''
        
        return 0
    
    def update_text(self):
        texts = ''
        texts += self.received[-1][1] + '\n' + self.received[-1][0] + '\n\n'
        
        self.text_area.configure(state ='normal')
        self.text_area.insert(tk.INSERT,texts)
        self.text_area.configure(state ='disabled')
        return 0

frame_count = 0
frame_num = 0
start_time = time.time()
frame_start_time = time.time()

frame_time = time.time()

rx = receiver.Receiver()

app = App()

while (True):
#while (time.time()-start_time < 60):

    data = ''
    if app.status !=-1:
        data, app.status = rx.read_frame(log = True)
        
        
        if (time.time()-frame_time >= 0.2):
            y_fft = rx.get_fft()
            app.line_fft.set_ydata(np.abs(y_fft[0:CHUNK]) * 2 / (256 * CHUNK) )
        
            app.ax2.draw_artist(app.ax2.patch)
            app.ax2.draw_artist(app.line_fft)
            
            app.fig.canvas.blit()
    
            app.fig.canvas.flush_events()
            
            frame_time = time.time()

        frame_count += 1
        
    app.root.update_idletasks()
    app.root.update()
    app.handle_status(data,rx.get_received_data())
    #app.update_text(rx.get_received_data())

print(frame_count/60)

