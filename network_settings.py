import math
# ---------GENERIC--------------

C1_LAYER_SIZE = 64
C2_LAYER_SIZE = 128
C3_LAYER_SIZE = 256
C4_LAYER_SIZE = 512
FC_LAYER_SIZE = 1024
 
NUM_ITER = 100000
BATCH_SIZE = 100
DROPOUT_RATE = 0.5
LEARNING_RATE = 0.0001


def load_settings_raw(dataset, dimen, input_len, input_depth, fold=0):
	global TRAINING_FILE
	global TEST_FILE
	global TRAINING_LABEL
	global TEST_LABEL
	global NUM_CLASSES
	global IMAGE_SHAPE
	global CONV_OUTPUT_SHAPE
	global MPOOL_SHAPE
	
	TRAINING_FILE = "data/fold{0}-raw-train-data-{1}.txt".format(fold, dataset)
	TEST_FILE = "data/fold{0}-raw-test-data-{1}.txt".format(fold, dataset)
	TRAINING_LABEL = "data/fold{0}-train-label-{1}.txt".format(fold, dataset)
	TEST_LABEL = "data/fold{0}-test-label-{1}.txt".format(fold, dataset)

	if dataset == '1a':
		NUM_CLASSES = 10
	else:
		NUM_CLASSES = 26

	output_shape_factor = math.ceil(math.ceil(math.ceil(input_len / 2) / 2) / 2)

	if dimen == '1d':
		CONV_OUTPUT_SHAPE = output_shape_factor #50 25 13 7
		MPOOL_SHAPE = 2
		IMAGE_SHAPE = (input_len, input_depth)
	else:
		CONV_OUTPUT_SHAPE = 7*2 #50 25 13 7
		MPOOL_SHAPE = (2,1)
		IMAGE_SHAPE = (input_len, input_depth, 1)

def load_settings_dtwfeatures(dataset, dimen, input_len, input_depth, input_method, fold=0):
	global TRAINING_FILE
	global TEST_FILE
	global TRAINING_LABEL
	global TEST_LABEL
	global NUM_CLASSES
	global IMAGE_SHAPE
	global CONV_OUTPUT_SHAPE
	global MPOOL_SHAPE

	TRAINING_FILE = "data/fold{0}-dtw_features-train-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth)
	TEST_FILE = "data/fold{0}-dtw_features-test-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth)
	TRAINING_LABEL = "data/fold{0}-train-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth)
	TEST_LABEL = "data/fold{0}-test-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth)

	if dataset == '1a':
		NUM_CLASSES = 10
	else:
		NUM_CLASSES = 26

	output_shape_factor = math.ceil(math.ceil(math.ceil(input_len / 2) / 2) / 2)
	
	if dimen == '1d':
		CONV_OUTPUT_SHAPE = output_shape_factor #50 25 13 7
		MPOOL_SHAPE = 2
		IMAGE_SHAPE = (input_len, input_depth)
	else:
		MPOOL_SHAPE = (2,1)
		IMAGE_SHAPE = (input_len, input_depth, 1)
		CONV_OUTPUT_SHAPE = output_shape_factor*input_depth #50 25 13 7

def load_settings_early(dataset, dimen, input_len, input_depth1, input_depth2, input_method, fold=0):
	global TRAINING_FILE
	global TEST_FILE
	global TRAINING_LABEL
	global TEST_LABEL
	global NUM_CLASSES
	global IMAGE_SHAPE
	global CONV_OUTPUT_SHAPE
	global MPOOL_SHAPE

	TRAINING_FILE = "data/fold{0}-dtw_features-plus-raw-train-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_FILE = "data/fold{0}-dtw_features-plus-raw-test-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TRAINING_LABEL = "data/fold{0}-train-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_LABEL = "data/fold{0}-test-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)

	combo_shape = input_depth1 + input_depth2

	output_shape_factor = math.ceil(math.ceil(math.ceil(input_len / 2) / 2) / 2)

	if dataset == '1a':
		NUM_CLASSES = 10
	else:
		NUM_CLASSES = 26

	if dimen == '1d':
		CONV_OUTPUT_SHAPE = output_shape_factor #50 25 13 7
		MPOOL_SHAPE = 2
		IMAGE_SHAPE = (input_len, combo_shape)
	else:
		MPOOL_SHAPE = (2,1)
		IMAGE_SHAPE = (input_len, combo_shape, 1)
		CONV_OUTPUT_SHAPE = output_shape_factor*combo_shape #50 25 13 7



def load_settings_mid(dataset, dimen, input_len, input_depth1, input_depth2, input_method, fold=0):
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

	global NUM_CLASSES
	global MPOOL_SHAPE

	TRAINING_FILE1 = "data/fold{0}-raw-train-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_FILE1 = "data/fold{0}-raw-test-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TRAINING_LABEL1 = "data/fold{0}-train-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_LABEL1 = "data/fold{0}-test-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)

	TRAINING_FILE2 = "data/fold{0}-dtw_features-train-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_FILE2 = "data/fold{0}-dtw_features-test-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TRAINING_LABEL2 = "data/fold{0}-train-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_LABEL2 = "data/fold{0}-test-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)

	if dataset == '1a':
		NUM_CLASSES = 10
	else:
		NUM_CLASSES = 26

	output_shape_factor = math.ceil(math.ceil(math.ceil(input_len / 2) / 2) / 2)

	if dimen == '1d':
		CONV_OUTPUT_SHAPE = output_shape_factor*2 #50 25 13 7
		MPOOL_SHAPE = 2
		IMAGE_SHAPE1 = (input_len, input_depth1)
		IMAGE_SHAPE2 = (input_len, input_depth2)
	else:
		MPOOL_SHAPE = (2,1)
		IMAGE_SHAPE1 = (input_len, input_depth1, 1)
		IMAGE_SHAPE2 = (input_len, input_depth2, 1)
		CONV_OUTPUT_SHAPE = (output_shape_factor*input_depth1)+(output_shape_factor*input_depth2)



def load_settings_late(dataset, dimen, input_len, input_depth1, input_depth2, input_method, fold=0):
	global TRAINING_FILE1
	global TEST_FILE1
	global TRAINING_LABEL1
	global TEST_LABEL1
	global IMAGE_SHAPE1
	global CONV_OUTPUT_SHAPE1

	global TRAINING_FILE2
	global TEST_FILE2
	global TRAINING_LABEL2
	global TEST_LABEL2
	global IMAGE_SHAPE2
	global CONV_OUTPUT_SHAPE2

	global NUM_CLASSES
	global MPOOL_SHAPE

	TRAINING_FILE1 = "data/fold{0}-raw-train-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_FILE1 = "data/fold{0}-raw-test-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TRAINING_LABEL1 = "data/fold{0}-train-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_LABEL1 = "data/fold{0}-test-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)

	TRAINING_FILE2 = "data/fold{0}-dtw_features-train-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_FILE2 = "data/fold{0}-dtw_features-test-data-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TRAINING_LABEL2 = "data/fold{0}-train-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)
	TEST_LABEL2 = "data/fold{0}-test-label-{1}-{2}-{3}.txt".format(fold, dataset, input_method, input_depth2)

	if dataset == '1a':
		NUM_CLASSES = 10
	else:
		NUM_CLASSES = 26

	output_shape_factor = math.ceil(math.ceil(math.ceil(input_len / 2) / 2) / 2)

	if dimen == '1d':
		CONV_OUTPUT_SHAPE1 = output_shape_factor #50 25 13 7
		CONV_OUTPUT_SHAPE2 = output_shape_factor #50 25 13 7
		MPOOL_SHAPE = 2
		IMAGE_SHAPE1 = (input_len, input_depth1)
		IMAGE_SHAPE2 = (input_len, input_depth2)
	else:
		MPOOL_SHAPE = (2,1)
		IMAGE_SHAPE1 = (input_len, input_depth1, 1)
		IMAGE_SHAPE2 = (input_len, input_depth2, 1)
		CONV_OUTPUT_SHAPE1 = output_shape_factor*input_depth1 #50 25 13 7
		CONV_OUTPUT_SHAPE2 = output_shape_factor*input_depth2 #50 25 13 7


