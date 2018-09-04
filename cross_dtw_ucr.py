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
    length = int(sys.argv[2])

    #for version in ["1a", "1b", "1c"]:
    print("Starting: {}".format(version))
    # load settings

    full_train_file = os.path.join("data", version + "_TRAIN")
    # full_test_file = os.path.join("data", version + "_TEST")
    # load data
    full_train = np.genfromtxt(full_train_file, delimiter=',')[:,1:].reshape((-1, length, 1))

    # print(np.shape(full_train[:,1:]))#.reshape((-1, length, 1))
    # exit()
    # full_test = np.genfromtxt(full_test_file, delimiter=',')

    # print(proto_number)

    #train_data = (data_sets.train.images.reshape((-1, 50, 2)) + 1.) * (127.5 / 127.)  # this input_data assumes images
    #train_labels = data_sets.train.labels

    train_number = np.shape(full_train)[0]
    #dtw_matrix = np.zeros((train_number, train_number))
    fileloc = os.path.join("data", "all-"+version + "-dtw-matrix.txt")

    with open(fileloc, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, delimiter=" ")
        for t1 in range(train_number):
            writeline = np.zeros((train_number))
            for t2 in range(train_number):
                writeline[t2] = dtw.dtw(full_train[t1], full_train[t2], extended=False)
            writer.writerow(writeline)
            print(t1)

    #np.savetxt(os.path.join("data", "{}_dtw_matrix.txt".format(version)), dtw_matrix, delimiter=' ')
print("Done")