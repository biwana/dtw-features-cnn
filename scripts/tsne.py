import dtw
import time
import numpy as np
import input_data_crossvalid as input_data
import network_settings as ns
import math
import csv
import os
import sys

from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.collections import LineCollection
from sklearn import manifold

def get_dtwfeatures(proto_data, proto_number, local_sample):
    local_sample_length = np.shape(local_sample)[0]
    features = np.zeros((local_sample_length, proto_number))
    for prototype in range(proto_number):
        local_proto = proto_data[prototype]
        output, cost, DTW, path = dtw.dtw(local_proto, local_sample, extended=True)

        for f in range(local_sample_length):
            features[f, prototype] = cost[path[0][f]][path[1][f]]
    return features

def read_dtw_matrix(version, fold):
#    if not os.path.exists(os.path.join("data", "fold"+str(fold)+"-"+version+"-dtw-matrix.txt")):
#        exit("Please run cross_dtw_full.py first")
#    return np.genfromtxt(os.path.join("data", "fold"+str(fold)+"-"+version+"-dtw-matrix.txt"), delimiter=' ')
    if not os.path.exists(os.path.join("..", "data", "all-"+version+"-dtw-matrix.txt")):
        exit("Please run cross_dtw_full.py first")
    full = np.genfromtxt(os.path.join("..", "data", "all-"+version+"-dtw-matrix.txt"), delimiter=' ')
    number = full.shape[0]
    indices = np.arange(number)
    test_ratio = 0.1
    test_start = fold * int(test_ratio * float(number))
    test_end = (fold+1) * int(test_ratio * float(number))
    testset = indices[test_start:test_end]
    testset[::-1].sort()
    for pl in testset:
        indices = np.delete(indices, pl, 0)
    trainset = indices
    ret = full[trainset]
    return ret[:,trainset]

def random_selection(proto_number):
    # gets random prototypes
    return np.arange(proto_number)

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
    if selection == "Random":
        return random_selection(proto_number)
    elif selection == "Centers":
        return center_selection(proto_number, distances)
    elif selection == "Borders":
        return border_selection(proto_number, distances)
    elif selection == "Spanning":
        return spanning_selection(proto_number, distances)
    elif selection == "K-Centers":
        return k_centers_selection(proto_number, distances)
    else:
        exit('missing')

def color_selector(selection):
    if selection == "Random":
        return "r"
    elif selection == "Centers":
        return "y"
    elif selection == "Borders":
        return "g"
    elif selection == "Spanning":
        return "c"
    elif selection == "K-Centers":
        return "b"
    else:
        return ""

def print_samples(sample):
    pass

if __name__ == "__main__":
    version = "1a"

    catarray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #catarray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #catarray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    classwise = "independent"
    proto_number = 10
    fold = 0

    print("Starting: {}".format(version))

    # load settings
    ns.load_settings_raw(version, "1d", 50, 2, fold)
    full_data_file = os.path.join("..", "data", version + "-re-data.txt")
    full_label_file = os.path.join("..", "data", version + "-re-labels.txt")
    # load data
    data_sets = input_data.read_data_sets(full_data_file, full_label_file, ns.IMAGE_SHAPE, test_ratio=0.1,
                                          validation_ratio=0.0, pickle=False, boring=False, fold=fold)

    no_classes = ns.NUM_CLASSES
    # print(proto_number)

    train_data = (data_sets.train.images.reshape((-1, 50, 2)) + 1.) * (
            127.5 / 127.)  # this input_data assumes images
    train_labels = data_sets.train.labels

    train_number = np.shape(train_labels)[0]

    test_data = (data_sets.test.images.reshape((-1, 50, 2)) + 1.) * (127.5 / 127.)  # this input_data assumes images
    test_labels = data_sets.test.labels
    test_number = np.shape(test_labels)[0]

    distances = read_dtw_matrix(version, fold)
    print(np.shape(train_labels))
    print(np.shape(distances))

    from matplotlib import rcParams
    rcParams['font.family'] = 'serif'
    family="serif"
    rcParams['legend.fontsize'] = 18

    neighbors = 10

    # tsne = manifold.TSNE(n_components=2, metric='precomputed', random_state=2)
    # pos = tsne.fit_transform(distances)

    sym_distances = 0.5* ( distances + distances.T )
    mds = manifold.MDS(n_components=2, dissimilarity='precomputed', random_state=2, metric=False, max_iter=50, verbose=1)
    pos = mds.fit_transform(sym_distances)

    plt.figure()
    ax =plt.subplot()
    x = pos[:,0]
    y = pos[:,1]
    cmap =plt.cm.gist_rainbow
    shapes = ["o", "s", ">", "<", "^", "v", "p", "h", "1", "2"]
    scatters = []
    for u in np.arange(no_classes):
        xi = [x[j] for j  in range(len(x)) if train_labels[j] == u]
        yi = [y[j] for j  in range(len(x)) if train_labels[j] == u]
        # ax.scatter(xi, yi, linewidth=0.6, alpha=0.3, c="gray")
        scat = ax.scatter(xi, yi, linewidth=0, alpha=0.8, s = 10, c=cmap((u*1.)/no_classes))#, label=catarray[u]) #, marker='$%s$' % u) #, marker=shapes[u])
        scatters.append(scat)

    # for j in range(len(x)):
    #     ax.text(x[j], y[j], catarray[int(train_labels[j])], color=cmap((train_labels[j]*1.)/no_classes)) #, marker=shapes[u])


    for selection in ["Random", "Centers", "Borders", "Spanning", "K-Centers"]:
        if classwise == "classwise":
            proto_loc = np.zeros(0, dtype=np.int32)
            proto_factor = int(proto_number / no_classes)
            for c in range(no_classes):
                cw = np.where(train_labels == c)[0]
                if selection == "Random":
                    cw_distances = []
                else:
                    cw_distances = distances[cw]
                    cw_distances = cw_distances[:,cw]
                cw_proto = selector_selector(selection, proto_factor, cw_distances)
                proto_loc = np.append(proto_loc, cw[cw_proto])
        else:
            proto_loc = selector_selector(selection, proto_number, distances)

        #proto_data = train_data[proto_loc]
        print(proto_loc)
        #exit()
        #print("Selection Done.")
        cla = train_labels[proto_loc]
        scat = ax.scatter(x[proto_loc], y[proto_loc], c=color_selector(selection),s = 100, label=selection, edgecolor="black") #, marker='$%s$' % cla) #, marker=shapes[u])
        # for p in proto_loc:
        #     ax.text(x[p], y[p], catarray[int(train_labels[p])], color=cmap((train_labels[p]*1.)/no_classes), size=15, weight="bold")
        #for pnum, local_proto in enumerate(train_data[proto_loc]):
        #    fig, ax = plt.subplots()
        #    ax.axis('off')
        #    plt.plot(local_proto[:,0], local_proto[:,1], marker="o",markersize=12, ls='-', linewidth=5, color='k')
        #    plt.ylim(-0.03,1.03)
        #    plt.xlim(-0.03,1.03)
        #    plt.savefig("analysis\\%s-%s_prototype_test.png" % (selection, pnum))
        #    plt.close()
        #    fig, ax = plt.subplots()
        #    ax.axis('off')
        #    plt.plot(local_proto[:,0], local_proto[:,1], marker="o",markersize=12, ls='-', linewidth=5, color='k')
        #    plt.ylim(-0.03,1.03)
        #    plt.xlim(-0.03,1.03)
        #    plt.savefig("analysis\\%s-%s_prototype_test.pdf" % (selection, pnum))
        #    plt.close()

    # plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    #plt.legend(loc="center left", bbox_to_anchor=(.8, 0.1))
    # plt.legend(loc="center left", bbox_to_anchor=(.8, 0.2))

    legend2 = plt.legend([scatters[i] for i in np.arange(10)], catarray, loc=4, bbox_to_anchor=(1.2, 0))
    plt.legend(loc=3, bbox_to_anchor=(-.33, 0))
    ax.add_artist(legend2)


    # cmap =plt.cm.gist_rainbow
    # for i, l in enumerate(labels):
    #     plt.scatter(pos[i,0], pos[i,1], c=cmap(l/10.), label=l)
    # plt.legend(loc=4)

    plt.axis('off')
    plt.tight_layout()
    #plt.show()
    plt.savefig("mds.pdf")
    plt.close()
print("Done")
