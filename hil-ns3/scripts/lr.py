#!/usr/bin/python3

'''
Run Linear Regression to process data on Photon
Work on Python 3.5.3 of Raspberry Pi 3B+
To test this module with 100MB input and 80kB output for 10 times:
    python3 lr.py -i 100000 -o 80 -t 10

Author: Xiaofan Yu
Date: 10/29/2019
'''
import numpy as np
import argparse
import time
import socket

class LinearRegression():
    def __init__(self, in_size, out_size):
        self.in_size = in_size
        self.out_size = out_size

        self.GenerateRandomWeights(in_size, out_size)

    def GenerateRandomWeights(self, row, col):
        self.w = np.random.normal(size=(row, col))

    def run(self, list_in):
        array_in = np.array(list_in)
        array_in = np.reshape(array_in, (-1))
        array_out = np.dot(array_in, self.w)
        return list(array_out.reshape(-1))

    def MAC(self):
        '''
        Calculate the number of MAC operations.
        '''
        return self.in_size * self.out_size

