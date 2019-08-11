import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# one hot = only one runs rest are off
mnist = input_data.read_data_sets('/tmp/data', one_hot=True)

# 10 classes, 0-9
# number of nodes in hidden layers
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
# take 100 images at time (has only limited RAM)
batch_size = 100

# matrix is height x width
# flatten the input to array of values
x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float', )

keep_rate = 0.8
keep_prob = tf.placeholder(tf.float32)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def maxpool2d(x):
    # ksize ... size of window
    # strides ... movement of window
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def neural_network_model(x):
    # create a tensor(big array) with random weights
    weights = {
        # 5 * 5 convolution, 1 input, 32 features/ outputs
        'W_conv1': tf.Variable(tf.random_normal([5, 5, 1, 32])),
        # take 32 inputs 5 * 5 and make it to 64
        'W_conv2': tf.Variable(tf.random_normal([5, 5, 32, 64])),
        # take 64 inputs 7 * 7, outputs 1024 nodes
        'W_fc': tf.Variable(tf.random_normal([7 * 7 * 64, 1024])),
        'out': tf.Variable(tf.random_normal([1024, n_classes]))
    }

    biases = {
        'B_conv1': tf.Variable(tf.random_normal([32])),
        'B_conv2': tf.Variable(tf.random_normal([64])),
        'B_fc': tf.Variable(tf.random_normal([1024])),
        'out': tf.Variable(tf.random_normal([n_classes]))
    }

    # reshape flat image inputs to 28*28
    x = tf.reshape(x, shape=[-1, 28, 28, 1])

    conv1 = conv2d(x, weights['W_conv1']) + biases['B_conv1']
    conv1 = maxpool2d(conv1)

    conv2 = conv2d(conv1, weights['W_conv2']) + biases['B_conv2']
    conv2 = maxpool2d(conv2)

    fc = tf.reshape(conv2, [-1, 7 * 7 * 64])
    fc = tf.nn.relu(tf.matmul(fc, weights['W_fc']) + biases['B_fc'])

    fc = tf.nn.dropout(fc, keep_rate)

    output = tf.matmul(fc, weights['out']) + biases['out']

    return output


def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    hm_epochs = 10
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples / batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
                epoch_loss += c
            print("Epoch", epoch, "completed out of", hm_epochs, 'loss:', epoch_loss)

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print("Accuracy: ", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))


train_neural_network(x)
