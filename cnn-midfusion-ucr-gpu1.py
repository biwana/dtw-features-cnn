import input_data
import tensorflow as tf
import time
import numpy as np
import network_settings_ucr as ns

import os
os.environ["CUDA_VISIBLE_DEVICES"]="1"

nowtime = str(time.time())

# -----------------------

print('start')


def cnn_model_1D(features, labels, mode):
    x_1 = tf.reshape(features["x1"], [-1, ns.IMAGE_SHAPE1[0], ns.IMAGE_SHAPE1[1]])
    x_2 = tf.reshape(features["x2"], [-1, ns.IMAGE_SHAPE2[0], ns.IMAGE_SHAPE2[1]])

    # variable conv layer
    for n in range(ns.NUM_CONV):
        c_1 = tf.layers.conv1d(inputs=x_1, filters=ns.C3_LAYER_SIZE, kernel_size=conv_shape, padding='SAME', activation=tf.nn.relu)
        x_1 = tf.layers.max_pooling1d(inputs=c_1, pool_size=ns.MPOOL_SHAPE, strides=ns.MPOOL_SHAPE, padding='SAME')

        c_2 = tf.layers.conv1d(inputs=x_2, filters=ns.C3_LAYER_SIZE, kernel_size=conv_shape, padding='SAME', activation=tf.nn.relu)
        x_2 = tf.layers.max_pooling1d(inputs=c_2, pool_size=ns.MPOOL_SHAPE, strides=ns.MPOOL_SHAPE, padding='SAME')

    # combine
    pool3 = tf.concat([x_1, x_2], 1)

    # densely connected layer

    pool3_flat = tf.reshape(pool3, [-1, ns.CONV_OUTPUT_SHAPE * ns.C3_LAYER_SIZE])
    dense1 = tf.layers.dense(inputs=pool3_flat, units=ns.FC_LAYER_SIZE, activation=tf.nn.relu)
    dropout1 = tf.layers.dropout(inputs=dense1, rate=ns.DROPOUT_RATE, training=mode == tf.estimator.ModeKeys.TRAIN)

    # densely connected layer

    dense2 = tf.layers.dense(inputs=dropout1, units=ns.FC_LAYER_SIZE, activation=tf.nn.relu)
    dropout2 = tf.layers.dropout(inputs=dense2, rate=ns.DROPOUT_RATE, training=mode == tf.estimator.ModeKeys.TRAIN)

    logits = tf.layers.dense(inputs=dropout2, units=ns.NUM_CLASSES)
    predictions = {
        # Generate predictions (for PREDICT and EVAL mode)
        "classes": tf.argmax(input=logits, axis=1),
        # Add `softmax_tensor` to the graph. It is used for PREDICT and by the
        # `logging_hook`.
        "probabilities": tf.nn.softmax(logits, name="softmax_tensor")
    }

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    # Calculate Loss (for both TRAIN and EVAL modes)
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    # Configure the Training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:
        # optimizer = tf.train.GradientDescentOptimizer(learning_rate=LEARNING_RATE)
        optimizer = tf.train.AdamOptimizer(learning_rate=ns.LEARNING_RATE)
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

    # Add evaluation metrics (for EVAL mode)
    eval_metric_ops = {
        "accuracy": tf.metrics.accuracy(
            labels=labels, predictions=predictions["classes"])}
    return tf.estimator.EstimatorSpec(
        mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


def cnn_model_2D(features, labels, mode):
    x_1 = tf.reshape(features["x1"], [-1, ns.IMAGE_SHAPE1[0], ns.IMAGE_SHAPE1[1], ns.IMAGE_SHAPE1[2]])
    x_2 = tf.reshape(features["x2"], [-1, ns.IMAGE_SHAPE2[0], ns.IMAGE_SHAPE2[1], ns.IMAGE_SHAPE2[2]])

    # variable conv layer
    for n in range(ns.NUM_CONV):
        c_1 = tf.layers.conv1d(inputs=x_1, filters=ns.C3_LAYER_SIZE, kernel_size=conv_shape, padding='SAME', activation=tf.nn.relu)
        x_1 = tf.layers.max_pooling1d(inputs=c_1, pool_size=ns.MPOOL_SHAPE, strides=ns.MPOOL_SHAPE, padding='SAME')

        c_2 = tf.layers.conv1d(inputs=x_2, filters=ns.C3_LAYER_SIZE, kernel_size=conv_shape, padding='SAME', activation=tf.nn.relu)
        x_2 = tf.layers.max_pooling1d(inputs=c_2, pool_size=ns.MPOOL_SHAPE, strides=ns.MPOOL_SHAPE, padding='SAME')

    # combine
    pool3 = tf.concat([x_1, x_2], 2)

    # densely connected layer

    pool3_flat = tf.reshape(pool3, [-1, ns.CONV_OUTPUT_SHAPE * ns.C3_LAYER_SIZE])
    dense1 = tf.layers.dense(inputs=pool3_flat, units=ns.FC_LAYER_SIZE, activation=tf.nn.relu)
    dropout1 = tf.layers.dropout(inputs=dense1, rate=ns.DROPOUT_RATE, training=mode == tf.estimator.ModeKeys.TRAIN)

    # densely connected layer

    dense2 = tf.layers.dense(inputs=dropout1, units=ns.FC_LAYER_SIZE, activation=tf.nn.relu)
    dropout2 = tf.layers.dropout(inputs=dense2, rate=ns.DROPOUT_RATE, training=mode == tf.estimator.ModeKeys.TRAIN)

    logits = tf.layers.dense(inputs=dropout2, units=ns.NUM_CLASSES)
    predictions = {
        # Generate predictions (for PREDICT and EVAL mode)
        "classes": tf.argmax(input=logits, axis=1),
        # Add `softmax_tensor` to the graph. It is used for PREDICT and by the
        # `logging_hook`.
        "probabilities": tf.nn.softmax(logits, name="softmax_tensor")
    }

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    # Calculate Loss (for both TRAIN and EVAL modes)
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    # Configure the Training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:
        # optimizer = tf.train.GradientDescentOptimizer(learning_rate=LEARNING_RATE)
        optimizer = tf.train.AdamOptimizer(learning_rate=ns.LEARNING_RATE)
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

    # Add evaluation metrics (for EVAL mode)
    eval_metric_ops = {
        "accuracy": tf.metrics.accuracy(
            labels=labels, predictions=predictions["classes"])}
    return tf.estimator.EstimatorSpec(
        mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


def main(argv):
    if len(argv) < 9:
        print("Error, Syntax: {0} [train/test] [dataset] [conv dim] [conv len] [input len] [input1 depth] [input2 depth] [input method] [num classes]".format(argv[0]))
        exit()
    global conv_shape
    conv_shape = int(argv[4])
    dataset = argv[2]
    conv_dim = argv[3]
    test = argv[1]

    input_len = int(argv[5])
    input_depth1 = int(argv[6])
    input_depth2 = int(argv[7])
    input_method = argv[8]
    num_classes = int(argv[9])

    ns.load_settings_mid(dataset, conv_dim, input_len, input_depth1, input_depth2, input_method, num_classes)

    run_name = "midfusion-fc1024-lr{0}-adam-{1}-{2}conv-{3}-{4}-{5}-all".format(ns.LEARNING_RATE, conv_dim, conv_shape, dataset, input_method, input_depth2)  # +"-"+nowtime

    print(run_name)

    data_sets1 = input_data.read_data_sets(ns.TRAINING_FILE1, ns.TRAINING_LABEL1, ns.IMAGE_SHAPE1, test_file=ns.TEST_FILE1, test_label=ns.TEST_LABEL1, validation_ratio=0.0, pickle=False, boring=False)
    train_data1 = data_sets1.train.images  # Returns np.array
    train_labels = np.asarray(data_sets1.train.labels, dtype=np.int32)
    eval_data1 = data_sets1.test.images  # Returns np.array
    eval_labels = np.asarray(data_sets1.test.labels, dtype=np.int32)

    print(np.shape(train_data1))

    data_sets2 = input_data.read_data_sets(ns.TRAINING_FILE2, ns.TRAINING_LABEL2, ns.IMAGE_SHAPE2, test_file=ns.TEST_FILE2, test_label=ns.TEST_LABEL2, validation_ratio=0.0, pickle=False, boring=False)
    train_data2 = data_sets2.train.images  # Returns np.array
    eval_data2 = data_sets2.test.images  # Returns np.array
    # print(np.reshape(eval_data[0], (50,50))[0,:])
    # print(tf.Session().run(tf.reshape(eval_data[0], (50,50))[0,:]))
    # print(eval_labels[0])
    # exit()

    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.4

    # Create the Estimator
    if conv_dim == "1d":
        classifier = tf.estimator.Estimator(model_fn=cnn_model_1D, model_dir="models/" + run_name, config=tf.estimator.RunConfig(session_config=config))
    else:
        classifier = tf.estimator.Estimator(model_fn=cnn_model_2D, model_dir="models/" + run_name, config=tf.estimator.RunConfig(session_config=config))

    if test == "train":
        # train

        # Set up logging for predictions
        # Log the values in the "Softmax" tensor with label "probabilities"
        tensors_to_log = {"probabilities": "softmax_tensor"}
        logging_hook = tf.train.LoggingTensorHook(
            tensors=tensors_to_log, every_n_iter=100)

        # Train the model
        train_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x1": train_data1, "x2": train_data2},
            y=train_labels,
            batch_size=ns.BATCH_SIZE,
            num_epochs=None,
            shuffle=True)
        classifier.train(
            input_fn=train_input_fn,
            steps=ns.NUM_ITER,
            hooks=[logging_hook])

        # Evaluate the model and print results
        eval_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x1": eval_data1, "x2": eval_data2},
            y=eval_labels,
            num_epochs=1,
            shuffle=False)
        eval_results = classifier.evaluate(input_fn=eval_input_fn)
        print(run_name)
        print(eval_results)
        np.savetxt("output/"+run_name+"-"+str(eval_results["accuracy"]), [eval_results["accuracy"]])
    else:
        # test
        # Evaluate the model and print results
        eval_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x1": eval_data1, "x2": eval_data2},
            y=eval_labels,
            num_epochs=1,
            shuffle=False)
        # eval_results = classifier.evaluate(input_fn=eval_input_fn)

        labels = eval_labels
        predictions = list(classifier.predict(input_fn=eval_input_fn))
        predicted_classes = [p["classes"] for p in predictions]

        from sklearn.metrics import confusion_matrix, classification_report
        print(run_name)

        print(confusion_matrix(labels, predicted_classes))
        print(classification_report(labels, predicted_classes))


if __name__ == "__main__":
    tf.app.run()
