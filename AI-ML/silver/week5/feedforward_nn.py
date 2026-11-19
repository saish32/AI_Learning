import tensorflow as tf

#define the architecture of the feedforward neural network
input_size=784 #number of input features (28x28 pixels for MNIST)
hidden_size=128 #number of neurons in the hidden layer
output_size=10 #number of output classes (digits 0-9)

#specify the input and output feature 
x=tf.placeholder(tf.float32,[None,input_size],name='x') #input placeholder
y=tf.placeholder(tf.float32,[None,output_size],name='y') #output placeholder

#configure te hidden layer 
hidden_layer=tf.layers.dense(inputs=x,units=hidden_size,activation=tf.nn.relu,name='hidden_layer')

#configure the output layer
output_layer=tf.layers.dense(inputs=hidden_layer,units=output_size,activation=None,name='output_layer')

#define the loss function and optimizer
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y,logits=output_layer))

#select the optimizer and learning rate
optimizer=tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

#initialize the variables
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

#train the model
for epoch in range(num_epochs):
    current_loss= sees.run([train_op,loss],feed_dict={x:train_images,y:train_labels})
    print(f"Epoch {epoch+1}, Loss: {current_loss}")

#evaluate the model on the test set
test_accuracy=sess.run(accuracy,feed_dict={x:test_images,y:test_labels})
print(f"Test Accuracy: {test_accuracy}")
