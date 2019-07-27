import tensorflow as tf

# tf constants
x1 = tf.constant(5)
x2 = tf.constant(6)

# no computation will take a part, it is only the model
result = tf.multiply(x1, x2)

print(result)
# the actual computation happens here

# bad style
# session = tf.Session()
# print(session.run(result))
# session.close()

# use this
with tf.Session() as sess:
    output = sess.run(result)
    print(output)
