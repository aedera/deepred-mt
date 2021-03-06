# read homologs
import sys
import random
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras

def read_windows(infile):
    """read nucleotide windows along with their editing extents. Nucleotides are
    encoded as integers: 0:A 1:C 2:G 3:T 4:e 5:E
    """
    labels = []
    wins = [] # window sequences
    exts = []
    cps = []
    keys = []
    data = []
    with open(infile) as f:
        for a in f:
            b = a.strip().split('\t')
            # label
            label = int(b[0])
            # window key
            key = b[1]
            # nucleotide window
            win = list(map(int, b[2]))
            # alignment key
            hg_key = b[3]
            # editing extent
            ext = float(b[4])
            # codon position
            cp = int(b[5]) - 1
            # save data
            ext = [1.0 - ext, ext]
            data.append((label, np.array(win), ext, cp, key))
    return np.array(data)

def train_test_split(wins, percentage=.8, seed=1234):
    idxs = list(range(len(wins)))
    rnd = random.Random()
    rnd.seed(seed)
    rnd.shuffle(idxs)
    thr = int(len(idxs) * percentage)
    train_idxs = idxs[0:thr]
    valid_idxs = idxs[thr:]
    return [wins[i] for i in train_idxs], [wins[i] for i in valid_idxs]

def read_long_windows(infile):
    """read nucleotide windows along with their editing extents. Nucleotides are
    encoded as integers: 0:A 1:C 2:G 3:T 4:e 5:E
    """
    wins = {} # window sequences
    with open(infile) as f:
        for a in f:
            b = a.strip().split('\t')
            # window key
            key = b[0]
            # nucleotide window
            win = list(b[1])
            wins[key] = win
    return wins
