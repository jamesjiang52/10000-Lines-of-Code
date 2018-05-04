import numpy as np
import tensorflow as tf
import get_data

train_data = get_data.train_data
train_chord_roots = get_data.train_chord_roots
test_data = get_data.test_data
test_chord_roots = get_data.test_chord_roots

num_hidden_1 = 1024
num_hidden_2 = 1024
batch_size = 1000
learning_rate = 0.0001
beta_1 = 0.9
beta_2 = 0.999
epsilon = 1e-8

data = tf.placeholder(tf.float32, shape=[None, get_data.len_data])
labels_chord_roots = tf.placeholder(tf.float32, shape=[None, 12])
keep_prob = tf.placeholder(tf.float32)

weights_chord_roots_hidden_1 =  tf.Variable(tf.random_normal([get_data.len_data, num_hidden_1], stddev=1/np.sqrt(get_data.len_data)), name="weights_chord_roots_hidden_1")
weights_chord_roots_hidden_2 =  tf.Variable(tf.random_normal([num_hidden_1, num_hidden_2], stddev=1/np.sqrt(num_hidden_1)), name="weights_chord_roots_hidden_2")
weights_chord_roots_out = tf.Variable(tf.random_normal([num_hidden_2, 12], stddev=1/np.sqrt(num_hidden_2)), name="weights_chord_roots_out")
biases_chord_roots_hidden_1 = tf.Variable(tf.zeros(num_hidden_1), name="biases_chord_roots_hidden_1")
biases_chord_roots_hidden_2 = tf.Variable(tf.zeros(num_hidden_2), name="biases_chord_roots_hidden_2")
biases_chord_roots_out = tf.Variable(tf.zeros(12), name="biases_chord_roots_out")

layer_chord_roots_1 = tf.nn.relu(tf.matmul(data, weights_chord_roots_hidden_1) + biases_chord_roots_hidden_1)
layer_dropout_chord_roots_1 = tf.nn.dropout(layer_chord_roots_1, keep_prob)
layer_chord_roots_2 = tf.nn.relu(tf.matmul(layer_dropout_chord_roots_1, weights_chord_roots_hidden_2) + biases_chord_roots_hidden_2)
layer_dropout_chord_roots_2 = tf.nn.dropout(layer_chord_roots_2, keep_prob)
out_chord_roots = tf.matmul(layer_dropout_chord_roots_2, weights_chord_roots_out) + biases_chord_roots_out

predict_chord_roots_op = tf.argmax(tf.nn.softmax(out_chord_roots), axis=1)
loss_chord_roots = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=out_chord_roots, labels=labels_chord_roots))
train_chord_roots_op = tf.train.AdamOptimizer(learning_rate=learning_rate, beta1=beta_1, beta2=beta_2, epsilon=epsilon).minimize(loss_chord_roots)

correct_chord_roots = tf.equal(predict_chord_roots_op, tf.argmax(test_chord_roots, 1))
accuracy_chord_roots = tf.reduce_mean(tf.cast(correct_chord_roots, tf.float32))

saver = tf.train.Saver(max_to_keep=1)
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

counter = 0
while True:
    batch_data, batch_labels_chord_roots = get_data.next_batch(batch_size, train_data, train_chord_roots)
    sess.run(train_chord_roots_op, feed_dict={data: batch_data, keep_prob: 0.5, labels_chord_roots: batch_labels_chord_roots})
    if counter % 10000 == 0:
        saver.save(sess, "model/chord_roots/chord_roots_model", write_meta_graph=False)
        total_accuracy_chord_roots = sess.run(accuracy_chord_roots, feed_dict={data: test_data, keep_prob: 1, labels_chord_roots: test_chord_roots})
        print("Training step: ", counter)
        print("Evaluation accuracy: ", str(round(100*total_accuracy_chord_roots, 1)) + "%\n")
        if total_accuracy_chord_roots > 0.95:
            break
    counter += 1

saver.save(sess, "model/chord_roots/chord_roots_model", write_meta_graph=False)
sess.close()
