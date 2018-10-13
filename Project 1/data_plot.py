#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:02:41 2018

@author: ciobanutudor
"""
import matplotlib.pyplot as plt
import numpy as np
from data_load import dataLoad

def dataPlot(data):
    bacteria = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])
    y_pos = np.arange(len(bacteria))
    bact1 = np.where(data[:,2] == bacteria[0])
    bacteria1 = len(data[:,2][bact1])
    bact2 = np.where(data[:,2] == bacteria[1])
    bacteria2 = len(data[:,2][bact2])
    bact3 = np.where(data[:,2] == bacteria[2])
    bacteria3 = len(data[:,2][bact3])
    bact4 = np.where(data[:,2] == bacteria[3])
    bacteria4 = len(data[:,2][bact4])
    numberOfBacteria = np.array([bacteria1, bacteria2, bacteria3, bacteria4])
    plt.bar(y_pos, numberOfBacteria)
    plt.xticks(y_pos, bacteria)
    plt.ylabel('Number of each type of bacteria')
    plt.title('Number of bacteria')
    plt.show()
    
data = dataLoad('test.txt')
dataPlot(data)