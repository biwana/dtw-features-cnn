import dtw
import time
import numpy as np
#import input_data #_crossvalid as input_data
#import network_settings as ns
import math
import csv
import os
import sys


def get_dtwfeatures(proto_data, proto_number, local_sample):
    local_sample_length = np.shape(local_sample)[0]
    features = np.zeros((local_sample_length, proto_number))
    for prototype in range(proto_number):
        local_proto = proto_data[prototype]
        output, cost, DTW, path = dtw.dtw(local_proto, local_sample, extended=True)

        for f in range(local_sample_length):
            features[f, prototype] = cost[path[0][f]][path[1][f]]
    return features

def read_dtw_matrix(version):
    if not os.path.exists(os.path.join("data", "all-"+version+"-dtw-matrix.txt")):
        exit("Please run cross_dtw.py first")
    return np.genfromtxt(os.path.join("data", "all-"+version+"-dtw-matrix.txt"), delimiter=' ')

def random_selection(proto_number, train_number):
    # gets random prototypes
    return np.random.randint(train_number, size=proto_number)

def center_selection(proto_number, distances):
    # gets the center prototypes
    return np.argsort(np.sum(distances, axis=1))[:proto_number]

def border_selection(proto_number, distances):
    # gets the border prototypes
    return np.argsort(np.sum(distances, axis=1))[::-1][:proto_number]

def spanning_selection(proto_number, distances):
    # gets the spanning prototypes
    proto_loc = center_selection(1, distances)
    choice_loc = np.delete(np.arange(np.shape(distances)[0]), proto_loc, 0)
    for iter in range(proto_number-1):
        d = distances[choice_loc]
        p = np.array([choice_loc[np.argmax(np.min(d[:,proto_loc], axis=1))]])
        proto_loc = np.append(proto_loc, p)
        choice_loc = np.delete(choice_loc, p, 0)
    return proto_loc

def k_centers_selection(proto_number, distances):
    # finds k centers
    no_possible = np.shape(distances)[0]

    # initialize with spanning
    proto_loc = spanning_selection(proto_number, distances)
    for iter in range(1000):
        # assign every point into a group with the centers
        membership = np.zeros(no_possible, dtype=np.int32)
        for i, d in enumerate(distances):
            membership[i] = proto_loc[np.argmin(d[proto_loc])]

        # find center of groups
        was_change = False
        for i, p in enumerate(proto_loc):
            p_group = np.where(membership==p)[0]
            d_matrix = distances[p_group]
            new_center = p_group[center_selection(1, d_matrix[:,p_group])][0]
            if new_center != p:
                proto_loc[i] = new_center
                was_change = True
        if was_change == False:
            print("stopping at {}".format(iter))
            break
    return proto_loc


def selector_selector(selection, proto_number, distances):
    if selection == "random":
        return random_selection(proto_number, distances)
    elif selection == "centers":
        return center_selection(proto_number, distances)
    elif selection == "borders":
        return border_selection(proto_number, distances)
    elif selection == "spanning":
        return spanning_selection(proto_number, distances)
    elif selection == "kcenters":
        return k_centers_selection(proto_number, distances)
    else:
        return random_selection(proto_number)

def param_selector(dataset):
    if dataset == "50words":
        return 50 #270
    if dataset == "Adiac":
        return 37 #176
    if dataset == "ArrowHead":
        return 3 #251
    if dataset == "Beef":
        return 5 #470
    if dataset == "BeetleFly":
        return 2 #512
    if dataset == "BirdChicken":
        return 2 #512
    if dataset == "Car":
        return 4 #577
    if dataset == "CBF":
        return 3 #128
    if dataset == "ChlorineConcentration":
        return 3 #166
    if dataset == "CinC_ECG_torso":
        return 4 #1639
    if dataset == "Coffee":
        return 2 #286
    if dataset == "Computers":
        return 2 #720
    if dataset == "Cricket_X":
        return 12 #300
    if dataset == "Cricket_Y":
        return 12 #300
    if dataset == "Cricket_Z":
        return 12 #300
    if dataset == "DiatomSizeReduction":
        return 4 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return 3 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 2 #80
    if dataset == "DistalPhalanxTW":
        return 6 #80
    if dataset == "Earthquakes":
        return 2 #512
    if dataset == "ECG200":
        return 2 #96
    if dataset == "ECG5000":
        return 5 #140
    if dataset == "ECGFiveDays":
        return 2 #136
    if dataset == "ElectricDevices":
        return 7 #96
    if dataset == "FaceAll":
        return 14 # 131
    if dataset == "FaceFour":
        return 4 # 350
    if dataset == "FacesUCR":
        return 14 # 131
    if dataset == "FISH":
        return 7 # 463
    if dataset == "FordA":
        return 2 #500
    if dataset == "FordB":
        return 2 # 500
    if dataset == "Gun_Point":
        return 2 # 150
    if dataset == "Ham":
        return 2 # 431
    if dataset == "HandOutlines":
        return 2 # 2709
    if dataset == "Haptics":
        return 5 # 1092
    if dataset == "Herring":
        return 2 # 512
    if dataset == "InlineSkate":
        return 7 # 1882
    if dataset == "InsectWingbeatSound":
        return 11 # 256
    if dataset == "ItalyPowerDemand":
        return 2 # 24
    if dataset == "LargeKitchenAppliances":
        return 3 # 720
    if dataset == "Lightning2":
        return 2 # 637
    if dataset == "Lightning7":
        return 7 # 319
    if dataset == "MALLAT":
        return 8 # 1024
    if dataset == "Meat":
        return 3 # 448
    if dataset == "MedicalImages":
        return 10 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return 3 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 2 #80
    if dataset == "MiddlePhalanxTW":
        return 6 #80
    if dataset == "MoteStrain":
        return 2 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return 42 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return 42 #750
    if dataset == "OliveOil":
        return 4 #570
    if dataset == "OSULeaf":
        return 6 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 2 #80
    if dataset == "Phoneme":
        return 39 #1024
    if dataset == "Plane":
        return 7 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return 3 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 2 #80
    if dataset == "ProximalPhalanxTW":
        return 6 #80
    if dataset == "RefrigerationDevices":
        return 3 #720
    if dataset == "ScreenType":
        return 3 #720
    if dataset == "ShapeletSim":
        return 2 #500
    if dataset == "ShapesAll":
        return 60 # 512
    if dataset == "SmallKitchenAppliances":
        return 3 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return 2 #65
    if dataset == "SonyAIBORobotSurface":
        return 2 #70
    if dataset == "StarLightCurves":
        return 3 #1024
    if dataset == "Strawberry":
        return 2 #235
    if dataset == "SwedishLeaf":
        return 15 # 128
    if dataset == "Symbols":
        return 6 #398
    if dataset == "synthetic_control":
        return 6 #60
    if dataset == "ToeSegmentation1":
        return 2 #277
    if dataset == "ToeSegmentation2":
        return 2 #343
    if dataset == "Trace":
        return 4 #275
    if dataset == "TwoLeadECG":
        return 2 #82
    if dataset == "Two_Patterns":
        return 4 #128
    if dataset == "uWaveGestureLibrary_X":
        return 8 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return 8 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return 8 # 315
    if dataset == "UWaveGestureLibraryAll":
        return 8 # 945
    if dataset == "wafer":
        return 2 #152
    if dataset == "Wine":
        return 2 #234
    if dataset == "WordSynonyms":
        return 25 #270
    if dataset == "Worms":
        return 5 #900
    if dataset == "WormsTwoClass":
        return 2 #900
    if dataset == "yoga":
        return 2 #426
    exit('missing dataset')

def class_modifier_add(dataset):
    if dataset == "50words":
        return -1 #270
    if dataset == "Adiac":
        return -1 #176
    if dataset == "ArrowHead":
        return 0 #251
    if dataset == "Beef":
        return -1 #470
    if dataset == "BeetleFly":
        return -1 #512
    if dataset == "BirdChicken":
        return -1 #512
    if dataset == "Car":
        return -1 #577
    if dataset == "CBF":
        return -1 #128
    if dataset == "ChlorineConcentration":
        return -1 #166
    if dataset == "CinC_ECG_torso":
        return -1 #1639
    if dataset == "Coffee":
        return 0 #286
    if dataset == "Computers":
        return -1 #720
    if dataset == "Cricket_X":
        return -1 #300
    if dataset == "Cricket_Y":
        return -1 #300
    if dataset == "Cricket_Z":
        return -1 #300
    if dataset == "DiatomSizeReduction":
        return -1 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return -1 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 0 #80
    if dataset == "DistalPhalanxTW":
        return -3 #80
    if dataset == "Earthquakes":
        return 0 #512
    if dataset == "ECG200":
        return 1 #96
    if dataset == "ECG5000":
        return -1 #140
    if dataset == "ECGFiveDays":
        return -1 #136
    if dataset == "ElectricDevices":
        return -1 #96
    if dataset == "FaceAll":
        return -1 # 131
    if dataset == "FaceFour":
        return -1 # 350
    if dataset == "FacesUCR":
        return -1 # 131
    if dataset == "FISH":
        return -1 # 463
    if dataset == "FordA":
        return 1 #500
    if dataset == "FordB":
        return 1 # 500
    if dataset == "Gun_Point":
        return -1 # 150
    if dataset == "Ham":
        return -1 # 431
    if dataset == "HandOutlines":
        return 0 # 2709
    if dataset == "Haptics":
        return -1 # 1092
    if dataset == "Herring":
        return -1 # 512
    if dataset == "InlineSkate":
        return -1 # 1882
    if dataset == "InsectWingbeatSound":
        return -1 # 256
    if dataset == "ItalyPowerDemand":
        return -1 # 24
    if dataset == "LargeKitchenAppliances":
        return -1 # 720
    if dataset == "Lightning2":
        return 1 # 637
    if dataset == "Lightning7":
        return 0 # 319
    if dataset == "MALLAT":
        return -1 # 1024
    if dataset == "Meat":
        return -1 # 448
    if dataset == "MedicalImages":
        return -1 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return -1 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 0 #80
    if dataset == "MiddlePhalanxTW":
        return -3 #80
    if dataset == "MoteStrain":
        return -1 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return -1 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return -1 #750
    if dataset == "OliveOil":
        return -1 #570
    if dataset == "OSULeaf":
        return -1 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 0 #80
    if dataset == "Phoneme":
        return -1 #1024
    if dataset == "Plane":
        return -1 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return -1 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 0 #80
    if dataset == "ProximalPhalanxTW":
        return -3 #80
    if dataset == "RefrigerationDevices":
        return -1 #720
    if dataset == "ScreenType":
        return -1 #720
    if dataset == "ShapeletSim":
        return 0 #500
    if dataset == "ShapesAll":
        return -1 # 512
    if dataset == "SmallKitchenAppliances":
        return -1 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return -1 #65
    if dataset == "SonyAIBORobotSurface":
        return -1 #70
    if dataset == "StarLightCurves":
        return -1 #1024
    if dataset == "Strawberry":
        return -1 #235
    if dataset == "SwedishLeaf":
        return -1 # 128
    if dataset == "Symbols":
        return -1 #398
    if dataset == "synthetic_control":
        return -1 #60
    if dataset == "ToeSegmentation1":
        return 0 #277
    if dataset == "ToeSegmentation2":
        return 0 #343
    if dataset == "Trace":
        return -1 #275
    if dataset == "TwoLeadECG":
        return -1 #82
    if dataset == "Two_Patterns":
        return -1 #128
    if dataset == "uWaveGestureLibrary_X":
        return -1 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return -1 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return -1 # 315
    if dataset == "UWaveGestureLibraryAll":
        return -1 # 945
    if dataset == "wafer":
        return 1 #152
    if dataset == "Wine":
        return -1 #234
    if dataset == "WordSynonyms":
        return -1 #270
    if dataset == "Worms":
        return -1 #900
    if dataset == "WormsTwoClass":
        return -1 #900
    if dataset == "yoga":
        return -1 #426
    exit('missing dataset')

def class_modifier_multi(dataset):
    if dataset == "50words":
        return 1 #270
    if dataset == "Adiac":
        return 1 #176
    if dataset == "ArrowHead":
        return 1 #251
    if dataset == "Beef":
        return 1 #470
    if dataset == "BeetleFly":
        return 1 #512
    if dataset == "BirdChicken":
        return 1 #512
    if dataset == "Car":
        return 1 #577
    if dataset == "CBF":
        return 1 #128
    if dataset == "ChlorineConcentration":
        return 1 #166
    if dataset == "CinC_ECG_torso":
        return 1 #1639
    if dataset == "Coffee":
        return 1 #286
    if dataset == "Computers":
        return 1 #720
    if dataset == "Cricket_X":
        return 1 #300
    if dataset == "Cricket_Y":
        return 1 #300
    if dataset == "Cricket_Z":
        return 1 #300
    if dataset == "DiatomSizeReduction":
        return 1 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return 1 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 1 #80
    if dataset == "DistalPhalanxTW":
        return 1 #80
    if dataset == "Earthquakes":
        return 1 #512
    if dataset == "ECG200":
        return 0.5 #96
    if dataset == "ECG5000":
        return 1 #140
    if dataset == "ECGFiveDays":
        return 1 #136
    if dataset == "ElectricDevices":
        return 1 #96
    if dataset == "FaceAll":
        return 1 # 131
    if dataset == "FaceFour":
        return 1 # 350
    if dataset == "FacesUCR":
        return 1 # 131
    if dataset == "FISH":
        return 1 # 463
    if dataset == "FordA":
        return 0.5 #500
    if dataset == "FordB":
        return 0.5 # 500
    if dataset == "Gun_Point":
        return 1 # 150
    if dataset == "Ham":
        return 1 # 431
    if dataset == "HandOutlines":
        return 1 # 2709
    if dataset == "Haptics":
        return 1 # 1092
    if dataset == "Herring":
        return 1 # 512
    if dataset == "InlineSkate":
        return 1 # 1882
    if dataset == "InsectWingbeatSound":
        return 1 # 256
    if dataset == "ItalyPowerDemand":
        return 1 # 24
    if dataset == "LargeKitchenAppliances":
        return 1 # 720
    if dataset == "Lightning2":
        return 0.5 # 637
    if dataset == "Lightning7":
        return 1 # 319
    if dataset == "MALLAT":
        return 1 # 1024
    if dataset == "Meat":
        return 1 # 448
    if dataset == "MedicalImages":
        return 1 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return 1 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 1 #80
    if dataset == "MiddlePhalanxTW":
        return 1 #80
    if dataset == "MoteStrain":
        return 1 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return 1 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return 1 #750
    if dataset == "OliveOil":
        return 1 #570
    if dataset == "OSULeaf":
        return 1 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 1 #80
    if dataset == "Phoneme":
        return 1 #1024
    if dataset == "Plane":
        return 1 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return 1 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 1 #80
    if dataset == "ProximalPhalanxTW":
        return 1 #80
    if dataset == "RefrigerationDevices":
        return 1 #720
    if dataset == "ScreenType":
        return 1 #720
    if dataset == "ShapeletSim":
        return 1 #500
    if dataset == "ShapesAll":
        return 1 # 512
    if dataset == "SmallKitchenAppliances":
        return 1 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return 1 #65
    if dataset == "SonyAIBORobotSurface":
        return 1 #70
    if dataset == "StarLightCurves":
        return 1 #1024
    if dataset == "Strawberry":
        return 1 #235
    if dataset == "SwedishLeaf":
        return 1 # 128
    if dataset == "Symbols":
        return 1 #398
    if dataset == "synthetic_control":
        return 1 #60
    if dataset == "ToeSegmentation1":
        return 1 #277
    if dataset == "ToeSegmentation2":
        return 1 #343
    if dataset == "Trace":
        return 1 #275
    if dataset == "TwoLeadECG":
        return 1 #82
    if dataset == "Two_Patterns":
        return 1 #128
    if dataset == "uWaveGestureLibrary_X":
        return 1 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return 1 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return 1 # 315
    if dataset == "UWaveGestureLibraryAll":
        return 1 # 945
    if dataset == "wafer":
        return 0.5 #152
    if dataset == "Wine":
        return 1 #234
    if dataset == "WordSynonyms":
        return 1 #270
    if dataset == "Worms":
        return 1 #900
    if dataset == "WormsTwoClass":
        return 1 #900
    if dataset == "yoga":
        return 1 #426
    exit('missing dataset')

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Error, Syntax: {0} [version] [prototype selection] [classwise/independent] [prototype number]".format(sys.argv[0]))
        exit()
    version = sys.argv[1]
    selection = sys.argv[2]
    classwise = sys.argv[3]
    proto_number = int(sys.argv[4])

    print("Starting: {}".format(version))

    # load settings
    full_train_file = os.path.join("data", version + "_TRAIN")
    full_test_file = os.path.join("data", version + "_TEST")
    # load data
    full_train = np.genfromtxt(full_train_file, delimiter=',')
    full_test = np.genfromtxt(full_test_file, delimiter=',')

    no_classes = param_selector(version)
    # print(proto_number)

    train_data = full_train[:,1:]
    train_labels = (full_train[:,0] + class_modifier_add(version))*class_modifier_multi(version)

    train_number = np.shape(train_labels)[0]

    test_data = full_test[:,1:]
    test_labels = (full_test[:,0] + class_modifier_add(version))*class_modifier_multi(version)

    test_number = np.shape(test_labels)[0]
    seq_length = np.shape(test_data)[1]

    train_data = train_data.reshape((-1,seq_length, 1))
    test_data = test_data.reshape((-1, seq_length, 1))

    distances = train_number if selection == "random" else read_dtw_matrix(version)

    if classwise == "classwise":
        proto_loc = np.zeros(0, dtype=np.int32)
        proto_factor = int(proto_number / no_classes)
        for c in range(no_classes):
            cw = np.where(train_labels == c)[0]
            if selection == "random":
                cw_distances = []
            else:
                cw_distances = distances[cw]
                cw_distances = cw_distances[:,cw]
            cw_proto = selector_selector(selection, proto_factor, cw_distances)
            proto_loc = np.append(proto_loc, cw[cw_proto])
    else:
        proto_loc = selector_selector(selection, proto_number, distances)

    proto_data = train_data[proto_loc]
    print(proto_loc)
    #exit()
    #print("Selection Done.")

    # sorts the prototypes so deletion happens in reverse order and doesn't interfere with indices
    proto_loc[::-1].sort()

    # remove prototypes from training data
    for pl in proto_loc:
        train_data = np.delete(train_data, pl, 0)
        train_labels = np.delete(train_labels, pl, 0)

    # start generation
    test_label_fileloc = os.path.join("data", "all-test-label-{}-{}-{}-{}.txt".format(version, selection, classwise, proto_number))
    test_raw_fileloc = os.path.join("data", "all-raw-test-data-{}-{}-{}-{}.txt".format(version, selection, classwise, proto_number))
    test_dtw_fileloc = os.path.join("data", "all-dtw_features-test-data-{}-{}-{}-{}.txt".format(version, selection, classwise, proto_number))
    test_combined_fileloc = os.path.join("data", "all-dtw_features-plus-raw-test-data-{}-{}-{}-{}.txt".format(version, selection, classwise, proto_number))
    train_label_fileloc = os.path.join("data", "all-train-label-{}-{}-{}-{}.txt".format(version, selection, classwise, proto_number))
    train_raw_fileloc = os.path.join("data", "all-raw-train-data-{}-{}-{}-{}.txt".format(version, selection, classwise, proto_number))
    train_dtw_fileloc = os.path.join("data", "all-dtw_features-train-data-{}-{}-{}-{}.txt".format(version, selection, classwise, proto_number))
    train_combined_fileloc = os.path.join("data", "all-dtw_features-plus-raw-train-data-{}-{}-{}-{}.txt".format(version, selection, classwise, proto_number))

    # test set
    with open(test_label_fileloc, 'w') as test_label_file, open(test_raw_fileloc, 'w') as test_raw_file, open(
            test_dtw_fileloc, 'w') as test_dtw_file, open(test_combined_fileloc, 'w') as test_combined_file:
        writer_test_label = csv.writer(test_label_file, quoting=csv.QUOTE_NONE, delimiter=" ")
        writer_test_raw = csv.writer(test_raw_file, quoting=csv.QUOTE_NONE, delimiter=" ")
        writer_test_dtw = csv.writer(test_dtw_file, quoting=csv.QUOTE_NONE, delimiter=" ")
        writer_test_combined = csv.writer(test_combined_file, quoting=csv.QUOTE_NONE, delimiter=" ")

        for sample in range(test_number):
            local_sample = test_data[sample]
            features = get_dtwfeatures(proto_data, proto_number, local_sample)

            # set the range from 0-255 for the input_data file (the input_data file was made for images and changes it back down to -1 to 1
            features = features * 255.
            local_sample = local_sample * 255.
            class_value = test_labels[sample]

            # write files
            feature_flat = features.reshape(seq_length * proto_number)
            local_sample_flat = local_sample.reshape(seq_length)
            writer_test_raw.writerow(local_sample_flat)
            writer_test_dtw.writerow(feature_flat)
            writer_test_combined.writerow(np.append(local_sample_flat, feature_flat))
            writer_test_label.writerow(["{}-{}_test.png".format(class_value, sample), class_value])
    print("{}: Test Done".format(version))

    # train set
    with open(train_label_fileloc, 'w') as train_label_file, open(train_raw_fileloc, 'w') as train_raw_file, open(
            train_dtw_fileloc, 'w') as train_dtw_file, open(train_combined_fileloc, 'w') as train_combined_file:
        writer_train_label = csv.writer(train_label_file, quoting=csv.QUOTE_NONE, delimiter=" ")
        writer_train_raw = csv.writer(train_raw_file, quoting=csv.QUOTE_NONE, delimiter=" ")
        writer_train_dtw = csv.writer(train_dtw_file, quoting=csv.QUOTE_NONE, delimiter=" ")
        writer_train_combined = csv.writer(train_combined_file, quoting=csv.QUOTE_NONE, delimiter=" ")

        for sample in range(train_number - proto_number):
            local_sample = train_data[sample]
            features = get_dtwfeatures(proto_data, proto_number, local_sample)

            # set the range from 0-255 for the input_data file (the input_data file was made for images and changes it back down to -1 to 1
            features = features * 255.
            local_sample = local_sample * 255.
            class_value = train_labels[sample]

            # write files
            feature_flat = features.reshape(seq_length * proto_number)
            local_sample_flat = local_sample.reshape(seq_length)
            writer_train_raw.writerow(local_sample_flat)
            writer_train_dtw.writerow(feature_flat)
            writer_train_combined.writerow(np.append(local_sample_flat, feature_flat))
            writer_train_label.writerow(["{}-{}_train.png".format(class_value, sample), class_value])

            if sample % 1000 == 0:
                print("{}: Training < {} Done".format(version, str(sample)))
    print("{}: Training Done".format(version))


print("Done")
