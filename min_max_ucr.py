import dtw
import time
import numpy as np
#import input_data_crossvalid as input_data
import network_settings as ns
import os
import csv
import sys


if __name__ == "__main__":
    version = sys.argv[1]

    #for version in ["1a", "1b", "1c"]:
    print("Starting: {}".format(version))
    # load settings

    full_train_file = os.path.join("data", version + "_TRAIN")
    # full_test_file = os.path.join("data", version + "_TEST")
    # load data
    full_train = np.genfromtxt(full_train_file, delimiter=',')[:,1:]

    print(str(np.max(full_train)))
    print(str(np.min(full_train)))
print("Done")