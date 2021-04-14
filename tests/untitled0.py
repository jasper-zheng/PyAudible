#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:16:04 2021

@author: winter_camp
"""
import numpy as np
import matplotlib.pyplot as plt
import PyA_Receiver_ill as pyaudible



rx = pyaudible.Receiver()
rx.read_block(15)
data = rx.get_freq_bins()

dt = 0.04
t = np.arange(0, dt*len(data[0]), dt)



fig, ax = plt.subplots(figsize=(10,9),dpi=200)
#ax.set_ylim(800, 12000)




#ax.semilogy(t,data[0],t,data[1],t,data[2],t,data[3],t,data[4],t,data[5],t,data[6],t,data[7], color=['blue','red'], lw=0.75)

'''
ax.semilogy(t,data[0],color='sandybrown',lw=0.75)
ax.semilogy(t,data[1],color='dodgerblue',lw=0.75)
ax.semilogy(t,data[2],color='sandybrown',lw=0.75)
ax.semilogy(t,data[3],color='dodgerblue',lw=0.75)
ax.semilogy(t,data[4],color='sandybrown',lw=0.75)
ax.semilogy(t,data[5],color='dodgerblue',lw=0.75)
ax.semilogy(t,data[6],color='sandybrown',lw=0.75)
ax.semilogy(t,data[7],color='dodgerblue',lw=0.75)

ax.set_yticks([800,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
ax.set_yticklabels(("800","1k","2k","3k","4k","5k","6k","7k","8k","9k","10k"))
ax.grid(True,lw='0.4')
ax.set_xticks(np.arange(0, dt*len(data[0]), 1))
'''

ax.semilogy(t,data[0],color='sandybrown',lw=0.75)

ax.set_yticks([1000,1100,1200,1300,1400,1500,1600,1700,1800])
ax.set_yticklabels(("1k","1.1k","1.2k","1.3k","1.4k","1.5k","1.6k","1.7k","1.8k"))

ax.grid(True,lw='0.4')
ax.set_xticks(np.arange(0, dt*len(data[0]), 1))