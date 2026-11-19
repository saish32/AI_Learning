import tensorflow as tf

# Build the operations in a graph so they can be executed by a v1 Session.
tf.compat.v1.disable_eager_execution()

a=tf.constant([[1,2],[3,4]])
b=tf.constant([[5,6],[7,8]])
c=tf.multiply(a,b)

print(tf.compat.v1.get_default_graph().as_graph_def())

with tf.compat.v1.Session() as sess:
    writer  = tf.compat.v1.summary.FileWriter('./logs', sess.graph)
    writer.close()
    result=sess.run(c)
    print(result)
    

