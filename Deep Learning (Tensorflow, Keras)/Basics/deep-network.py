'''
input -> weight -> hidden layer 1 (activation function)
-> weigths -> hidden layer 2 (activation function) -> weights
-> output layer
this called feed forward

compare output to intended output -> cost or loss function (cross entropy)
-> optimization function (optimizer) -> minimize cost (AdamOptimizer, SDG, AdaGrad, ...)
this called backpropagation

feed forward + backprop = epoch


biases:
(input_data * weights) + biases
idea: some neurons can fire even if weights are 0
'''
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# one hot = only one runs rest are off
mnist = input_data.read_data_sets('/tmp/data', one_hot=True)

# 10 classes, 0-9
'''
one_hot makes this:
0 = [1,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0] and so on
'''
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
y = tf.placeholder('float',)


def neural_network_model(data):
    # create a tensor(big array) with random weights
    hidden_1_layer = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl1))}

    hidden_2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl2))}

    hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl3))}

    output_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
        'biases': tf.Variable(tf.random_normal([n_classes]))
    }

    # input_data * weights + biases
    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    # pass through activation function
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

    return output


