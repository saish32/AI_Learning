import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D

#create a simple sequential model
model=Sequential([
    Dense(32,activation='relu',input_shape=(28,28,1)),
    Dense(10,activation='softmax')
])

#compile the model
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])




tf.compat.v1.disable_eager_execution()



# #create a 1d tensors of float 32

# x=tf.compat.v1.placeholder(tf.float32,shape=[3],name='x')
# square_op=tf.square(x)

# with tf.compat.v1.Session() as sess:
#     result=sess.run(square_op,feed_dict={x:[1,2,3]})
#     print(result)

# a=tf.constant(2)
# b=tf.constant(3)
# c=tf.add(a,b)

# tf.compat.v1.disable_eager_execution()
# with tf.compat.v1.Session() as sess:
#     sess.run(tf.compat.v1.global_variables_initializer())
#     print(sess.run(c))


# tf.compat.v1.disable_eager_execution()
# tensor = tf.constant("Hello, TensorFlow!")

# with tf.compat.v1.Session() as sess:
#     print(sess.run(tensor).decode("utf-8"))
