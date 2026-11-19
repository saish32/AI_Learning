import tensorflow as tf

# #constants
# constant_tensor = tf.constant([1,2,3,4,5], dtype=tf.int32)

# #variable
# variable_tensor = tf.Variable([1,2,3,4,5], dtype=tf.int32)
# initial_value = tf.random.normal(shape=(3, 3), mean=0.0, stddev=1.0, dtype=tf.float32)
# variable_tensor2 = tf.Variable(initial_value)

# #new values
# initial_value2 = tf.random.uniform(shape=(3, 3), minval=0, maxval=10, dtype=tf.float32)
# variable_tensor2.assign(initial_value2)

# #create a placeholder for input data(deprecated in TF 2.x, but still available for compatibility)
# x=tf.compat.v1.placeholder(tf.float32, shape=(None, 3), name='input_placeholder')
# y=tf.square(x)

# #tensorflow 2.x approach for placeholders 
# x=tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)
# y=tf.square(x)
