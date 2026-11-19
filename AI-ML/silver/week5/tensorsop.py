import tensorflow as tf

# tensor1 = tf.constant([[1, 2], [3, 4]])
# tensor2 = tf.constant([[5, 6], [7, 8]])

# # Basic arithmetic operations
# result=tf.add(tensor1, tensor2)
# subtraction=tf.subtract(tensor1, tensor2)
# multiplication=tf.multiply(tensor1, tensor2)
# division=tf.divide(tensor1, tensor2)

# # Element-wise operations
# result_square=tf.square(tensor1)
# result_sqrt=tf.sqrt(tf.cast(tensor1, tf.float32))
# result_exp=tf.exp(tf.cast(tensor1, tf.float32))
# result_log=tf.math.log(tf.cast(tensor1, tf.float32))

# # Reduction operations
# result_sum=tf.reduce_sum(tensor1)
# result_mean=tf.reduce_mean(tensor1)
# result_max=tf.reduce_max(tensor1)

# # Matrix operations
# result_matrix_multiplication=tf.matmul(tensor1, tensor2)
# result_transpose=tf.transpose(tensor1)
# result_inverse=tf.linalg.inv(tensor1)

# #acessing specific elements
# element_1=tf.gather(tensor1, 0)  # Accessing the first
# element_2=tf.gather(tensor1, 1)  # Accessing the second

# #slicing
# slice_1=tf.slice(tensor1, [0, 0], [1, 2])  # Slicing the first row

# #broadcasting
# tensor3 = tf.constant([[1], [2]])
# result_broadcasting=tf.add(tensor1, tensor3)  # Broadcasting addition