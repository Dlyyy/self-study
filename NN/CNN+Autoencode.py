# -*- coding: utf-8 -*-

#https://www.jianshu.com/p/3e18a1b5d5a6
import tensorflow as tf
import random
import numpy as np
import time

BASIC_HOME = "/Users/allwefantasy/Downloads"
WORD_VECTOR_FILE = BASIC_HOME + '/laiwen/zhuhl_laiwen_word_embedding'
WORD_FILE = BASIC_HOME + '/laiwen/zhuhl_laiwen_keywords2'
WORD_RESULT_VECTOR_FILE = BASIC_HOME + '/laiwen/WORD_RESULT_VECTOR_FILE4'
MODEL_SAVE_DIR = BASIC_HOME + '/laiwen/model/autoencoder'

VOCAB_SIZE = 100
SEQUENCE_LENGTH = 59
VOCAB_WINDOW = 3

USE_CNN = True

RANGE_SIZE = 60
PRE_FETCH_SIZE = 10000
TRAINING_BATCH_SIZE = 200


def next_batch(batch_num, batch_size, word_vec_dict):
    with open(WORD_FILE) as wf:
        line_num = 0
        start_line_num = batch_num * batch_size
        batch_counter = 0
        result = []
        for words in wf:
            result1 = []
            line_num += 1

            if line_num > start_line_num:
                batch_counter += 1
                for word in words.split(" "):
                    if word in word_vec_dict:
                        result1.append(word_vec_dict[word])
                if len(result1) < SEQUENCE_LENGTH:
                    for i in range(SEQUENCE_LENGTH - len(result1)):
                        result1.append(np.zeros(shape=(VOCAB_SIZE, 1)).tolist())
                result.append([str(line_num), result1[0:SEQUENCE_LENGTH]])
                if batch_counter == batch_size:
                    return result


def read_dict():
    wor_vec_dict = {}

    with open(WORD_VECTOR_FILE) as f:
        content = f.readlines()
        for line in content:
            labelWithVecotr = line.strip().split(" ")
            if len(labelWithVecotr) == 2:
                wor_vec_dict[labelWithVecotr[0]] = [[float(x)] for x in labelWithVecotr[1].split(",")]

    return wor_vec_dict


def conv_layer(input, size_in, size_out, width=VOCAB_SIZE, name="conv"):
    with tf.name_scope(name):
        w = tf.Variable(tf.truncated_normal([VOCAB_WINDOW, width, size_in, size_out], stddev=0.1), name="W")
        b = tf.Variable(tf.constant(0.1, shape={size_out}, name="B"))
        conv = tf.nn.conv2d(input, w, strides=[1, 1, 1, 1], padding="VALID")
        act = tf.nn.relu(conv + b)
        tf.summary.histogram("weights", w)
        tf.summary.histogram("biases", b)
        tf.summary.histogram("activations", act)
        return tf.nn.max_pool(act, ksize=[1, VOCAB_WINDOW, 1, 1], strides=[1, 1, 1, 1], padding="VALID")


# input_encoder_w_b =

# tf.Variable(tf.random_normal([SEQUENCE_LENGTH * VOCAB_SIZE, 256])

encoder_variables_dict = {
    "encoder_w1": tf.Variable(tf.random_normal([51 * 128, 256]), name="encoder_w1") if USE_CNN else tf.Variable(
        tf.random_normal([SEQUENCE_LENGTH * VOCAB_SIZE, 256]), name="encoder_w1"),
    "encoder_b1": tf.Variable(tf.random_normal([256]), name="encoder_b1"),
    "encoder_w2": tf.Variable(tf.random_normal([256, 128]), name="encoder_w2"),
    "encoder_b2": tf.Variable(tf.random_normal([128]), name="encoder_b2")
}


def encoder(x, name="encoder"):
    with tf.name_scope(name):
        encoder_w1 = encoder_variables_dict["encoder_w1"]
        encoder_b1 = encoder_variables_dict["encoder_b1"]

        layer_1 = tf.nn.sigmoid(tf.matmul(x, encoder_w1) + encoder_b1)

        encoder_w2 = encoder_variables_dict["encoder_w2"]
        encoder_b2 = encoder_variables_dict["encoder_b2"]

        layer_2 = tf.nn.sigmoid(tf.matmul(layer_1, encoder_w2) + encoder_b2)
        return layer_2


def decoder(x, name="decoder"):
    with tf.name_scope(name):
        decoder_w1 = tf.Variable(tf.random_normal([128, 256]))
        decoder_b1 = tf.Variable(tf.random_normal([256]))

        layer_1 = tf.nn.sigmoid(tf.matmul(x, decoder_w1) + decoder_b1)

        decoder_w2 = tf.Variable(tf.random_normal([256, 51 * 128])) if USE_CNN else  tf.Variable(
            tf.random_normal([256, SEQUENCE_LENGTH * VOCAB_SIZE]))
        decoder_b2 = tf.Variable(tf.random_normal([51 * 128])) if USE_CNN else tf.Variable(
            tf.random_normal([SEQUENCE_LENGTH * VOCAB_SIZE]))

        layer_2 = tf.nn.sigmoid(tf.matmul(layer_1, decoder_w2) + decoder_b2)
        return layer_2


def laiwen_model(learning_rate, hparam):
    tf.reset_default_graph
    sess = tf.Session()

    input_x = tf.placeholder(tf.float32, [None, SEQUENCE_LENGTH, VOCAB_SIZE, 1], name="input_x")

    conv1 = conv_layer(input_x, 1, 64, VOCAB_SIZE, "conv1")
    conv_out = conv_layer(conv1, 64, 128, 1, "conv2")
    tf.add_to_collection('conv_c', conv_out)
    flattened = tf.reshape(conv_out, [-1, 51 * 128]) if USE_CNN else tf.reshape(input_x,
                                                                                [-1, SEQUENCE_LENGTH * VOCAB_SIZE])

    encoder_op = encoder(flattened)

    tf.add_to_collection('encoder_op', encoder_op)

    y_pred = decoder(encoder_op)

    y_true = flattened

    with tf.name_scope("xent"):
        # xent =tf.reduce_sum(tf.cos([y_true, y_pred]), name="xent")

        consine = tf.div(tf.reduce_sum(tf.multiply(y_pred, y_true)),
                         tf.multiply(tf.sqrt(tf.reduce_sum(tf.multiply(y_pred, y_pred))),
                                     tf.sqrt(tf.reduce_sum(tf.multiply(y_true, y_true)))))
        xent = tf.reduce_sum(tf.subtract(tf.constant(1.0), consine))
        tf.summary.scalar("xent", xent)

    with tf.name_scope("train"):
        # train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(xent)
        train_step = tf.train.RMSPropOptimizer(learning_rate).minimize(xent)

    summ = tf.summary.merge_all()

    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()

    word_vec_dict = read_dict()

    saver.save(sess, MODEL_SAVE_DIR)

    for i in range(RANGE_SIZE):

        ticks = time.time()
        batch = next_batch(i, PRE_FETCH_SIZE, word_vec_dict)
        ticks2 = time.time()
        sub_batch_num = int(len(batch) / TRAINING_BATCH_SIZE)
        print('load training data consume time: %d, size in memory: %d, total rounds: %d ' % (
            ticks2 - ticks, len(batch), sub_batch_num))

        if i % 10 == 0:
            print(' i==%d then save  model to %s' % (i,MODEL_SAVE_DIR))
            saver.save(sess, MODEL_SAVE_DIR)
        if i == (RANGE_SIZE - 1):
            print('save to /tmp/cnn/my_test_model')
            saver.save(sess, MODEL_SAVE_DIR)
            print('begin to output....')
            with open(WORD_RESULT_VECTOR_FILE, "w") as f:
                with open(WORD_FILE) as wf:
                    line_num = 0
                    for words in wf:
                        print('processed %d' % line_num)
                        result1 = []
                        for word in words.split(" "):
                            if word in word_vec_dict:
                                result1.append(word_vec_dict[word])

                        if len(result1) < SEQUENCE_LENGTH:
                            for i in range(SEQUENCE_LENGTH - len(result1)):
                                result1.append(np.zeros(shape=(VOCAB_SIZE, 1)).tolist())

                        line_num += 1
                        x_in = result1[0:SEQUENCE_LENGTH]
                        s = sess.run(encoder_op, feed_dict={input_x: [x_in]})
                        f.write('%s %s' % (str(line_num), ",".join([str(f) for f in s.tolist()[0]])))
                        f.write("\n")

        for j in range(sub_batch_num):
            sub_batch_data = batch[TRAINING_BATCH_SIZE * j: TRAINING_BATCH_SIZE * (j + 1)]
            batdch_data = [x[1] for x in sub_batch_data]

            if i % 5 == 0:
                [s, _] = sess.run([xent, summ], feed_dict={input_x: batdch_data})
                print('step %d, sub step %d ,batch size %d,cost %g' % (i, j, len(batdch_data), s))

            sess.run(train_step, feed_dict={input_x: batdch_data})


def main():
    for learning_rate in [1E-4]:
        laiwen_model(learning_rate, "jack")


if __name__ == '__main__':
    main()