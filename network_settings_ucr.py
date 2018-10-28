import math
# ---------GENERIC--------------

C1_LAYER_SIZE = 64
C2_LAYER_SIZE = 128
C3_LAYER_SIZE = 256
C4_LAYER_SIZE = 512
FC_LAYER_SIZE = 1024

NUM_ITER = 100000
BATCH_SIZE = 50
DROPOUT_RATE = 0.5
LEARNING_RATE = 0.0001

def load_settings_mid(dataset, dimen, input_len, input_depth1, input_depth2, input_method, num_classes):
    global TRAINING_FILE1
    global TEST_FILE1
    global TRAINING_LABEL1
    global TEST_LABEL1
    global IMAGE_SHAPE1

    global TRAINING_FILE2
    global TEST_FILE2
    global TRAINING_LABEL2
    global TEST_LABEL2
    global IMAGE_SHAPE2

    global CONV_OUTPUT_SHAPE
    global NUM_CONV

    global NUM_CLASSES
    global MPOOL_SHAPE

    TRAINING_FILE1 = "data/all-raw-train-data-{}-{}-{}.txt".format(dataset, input_method, input_depth2)
    TEST_FILE1 = "data/all-raw-test-data-{}-{}-{}.txt".format(dataset, input_method, input_depth2)
    TRAINING_LABEL1 = "data/all-train-label-{}-{}-{}.txt".format(dataset, input_method, input_depth2)
    TEST_LABEL1 = "data/all-test-label-{}-{}-{}.txt".format(dataset, input_method, input_depth2)

    TRAINING_FILE2 = "data/all-dtw_features-train-data-{}-{}-{}.txt".format(dataset, input_method, input_depth2)
    TEST_FILE2 = "data/all-dtw_features-test-data-{}-{}-{}.txt".format(dataset, input_method, input_depth2)
    TRAINING_LABEL2 = "data/all-train-label-{}-{}-{}.txt".format(dataset, input_method, input_depth2)
    TEST_LABEL2 = "data/all-test-label-{}-{}-{}.txt".format(dataset, input_method, input_depth2)

    NUM_CLASSES = num_classes
    NUM_CONV = int(round(math.log(input_len, 2))-3)
    print("number of conv layers: %s" % str(NUM_CONV))

    output_shape_factor = input_len
    for i in range(NUM_CONV):
        output_shape_factor = math.ceil(output_shape_factor / 2.)
    output_shape_factor = int(output_shape_factor)

    if dimen == '1d':
        CONV_OUTPUT_SHAPE = output_shape_factor * 2  # 50 25 13 7
        MPOOL_SHAPE = 2
        IMAGE_SHAPE1 = (input_len, input_depth1)
        IMAGE_SHAPE2 = (input_len, input_depth2)
    else:
        MPOOL_SHAPE = (2, 1)
        IMAGE_SHAPE1 = (input_len, input_depth1, 1)
        IMAGE_SHAPE2 = (input_len, input_depth2, 1)
        CONV_OUTPUT_SHAPE = (output_shape_factor * input_depth1) + (output_shape_factor * input_depth2)

