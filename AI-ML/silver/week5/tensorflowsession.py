import tensorflow as tf


tf.compat.v1.disable_eager_execution()

graph=tf.Graph()

with graph.as_default():
    a=tf.constant([[1,2],[3,4]])
    b=tf.constant([[5,6],[7,8]])
    c=tf.add(a,b)

config=tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth=True
config.log_device_placement=True

with tf.compat.v1.Session(graph=graph,config=config) as sess:
    result=sess.run(c)
    print(result)

# #tensorflow 1.x uses a computational graph and requires a session to evaluate tensors.
# a=tf.constant([[1,2],[3,4]])
# b=tf.constant([[5,6],[7,8]])
# c=tf.add(a,b)

# with tf.compat.v1.Session() as sess:
#     result=sess.run(c)
#     print(result)



# #tensorflow 2.x uses eager execution by default, so we can directly evaluate tensors without creating a session.
# a=tf.constant([[1,2],[3,4]])
# b=tf.constant([[5,6],[7,8]])
# c=tf.add(a,b)

# result=c.numpy
# print(result)