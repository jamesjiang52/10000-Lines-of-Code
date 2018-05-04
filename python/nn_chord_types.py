import numpy as np
import tensorflow as tf
import translate
import get_data

# James note to self: maybe add keep_prob

train_data = get_data.train_data
train_chord_types = get_data.train_chord_types
test_data = get_data.test_data
test_chord_types = get_data.test_chord_types

num_hidden_1 = 2048
num_hidden_2 = 2048
batch_size = 1000
learning_rate = 0.001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 1e-8

data = tf.placeholder(tf.float32, shape=[None, get_data.len_data])
labels_chord_types = tf.placeholder(tf.float32, shape=[None, translate.NUM_CHORD_TYPES])

weights_chord_types_hidden_1 =  tf.Variable(tf.random_normal([get_data.len_data, num_hidden_1], stddev=1/np.sqrt(get_data.len_data)), name="weights_chord_types_hidden_1")
weights_chord_types_hidden_2 =  tf.Variable(tf.random_normal([num_hidden_1, num_hidden_2], stddev=1/np.sqrt(num_hidden_1)), name="weights_chord_types_hidden_2")
weights_chord_types_out = tf.Variable(tf.random_normal([num_hidden_2, translate.NUM_CHORD_TYPES], stddev=1/np.sqrt(num_hidden_2)), name="weights_chord_types_out")
biases_chord_types_hidden_1 = tf.Variable(tf.zeros(num_hidden_1), name="biases_chord_types_hidden_1")
biases_chord_types_hidden_2 = tf.Variable(tf.zeros(num_hidden_2), name="biases_chord_types_hidden_2")
biases_chord_types_out = tf.Variable(tf.zeros(translate.NUM_CHORD_TYPES), name="biases_chord_types_out")

layer_chord_types_1 = tf.nn.relu(tf.matmul(data, weights_chord_types_hidden_1) + biases_chord_types_hidden_1)
layer_chord_types_2 = tf.nn.relu(tf.matmul(layer_chord_types_1, weights_chord_types_hidden_2) + biases_chord_types_hidden_2)
out_chord_types = tf.matmul(layer_chord_types_2, weights_chord_types_out) + biases_chord_types_out

predict_chord_types_op = tf.argmax(tf.nn.softmax(out_chord_types), axis=1)
loss_chord_types = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=out_chord_types, labels=labels_chord_types))
train_chord_types_op = tf.train.AdamOptimizer(learning_rate=learning_rate, beta1=beta_1, beta2=beta_2, epsilon=epsilon).minimize(loss_chord_types)

correct_chord_types = tf.equal(predict_chord_types_op, tf.argmax(test_chord_types, 1))
accuracy_chord_types = tf.reduce_mean(tf.cast(correct_chord_types, tf.float32))

saver = tf.train.Saver(max_to_keep=1)
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

counter = 0
while True:
    batch_data, batch_labels_chord_types = get_data.next_batch(batch_size, train_data, train_chord_types)
    sess.run(train_chord_types_op, feed_dict={data: batch_data, labels_chord_types: batch_labels_chord_types})
    if counter % 10000 == 0:
        saver.save(sess, "model/chord_types/chord_types_model", write_meta_graph=False)
        total_accuracy_chord_types = sess.run(accuracy_chord_types, feed_dict={data: test_data, labels_chord_types: test_chord_types})
        print("Training step: ", counter)
        print("Evaluation accuracy: ", str(round(100*total_accuracy_chord_types, 1)) + "%")
        if total_accuracy_chord_types > 0.95:
            break
    counter += 1

saver.save(sess, "model/chord_types/chord_types_model", write_meta_graph=False)
sess.close()
