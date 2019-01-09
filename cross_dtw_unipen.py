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
    ns.load_settings_raw(version, "1d", 50, 2)
    full_data_file = os.path.join("data", version + "-re-data.txt")
    full_label_file = os.path.join("data", version + "-re-labels.txt")
    # load data
    #data_sets = input_data.read_data_sets(full_data_file, full_label_file, ns.IMAGE_SHAPE, test_ratio=0.1,
    #                                      validation_ratio=0.0, pickle=False, boring=False, fold=fold)
    train_data = np.genfromtxt(full_data_file, delimiter=' ').reshape((-1, 50, 2)) / 127.
    train_labels = np.genfromtxt(full_label_file, usecols=(1), delimiter=' ')

    no_classes = ns.NUM_CLASSES
    # print(proto_number)

    #train_data = (data_sets.train.images.reshape((-1, 50, 2)) + 1.) * (127.5 / 127.)  # this input_data assumes images
    #train_labels = data_sets.train.labels

    train_number = np.shape(train_labels)[0]
    #dtw_matrix = np.zeros((train_number, train_number))
    fileloc = os.path.join("data", "all-"+version + "-dtw-matrix.txt")

    with open(fileloc, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, delimiter=" ")
        for t1 in range(train_number):
            writeline = np.zeros((train_number))
            for t2 in range(train_number):
                writeline[t2] = dtw.dtw(train_data[t1], train_data[t2], extended=False)
            writer.writerow(writeline)
            print(t1)

    #np.savetxt(os.path.join("data", "{}_dtw_matrix.txt".format(version)), dtw_matrix, delimiter=' ')
print("Done")