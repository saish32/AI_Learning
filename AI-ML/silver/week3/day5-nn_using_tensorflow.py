import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout

# #load mnist dataset
# (x_train,y_train),(x_test,y_test)=mnist.load_data()

# #normalize the data
# x_train=x_train.reshape(-1,28,28,1).astype('float32')/255.0
# x_test=x_test.reshape(-1,28,28,1).astype('float32')/255.0

# #one hot encode the labels
# y_train=to_categorical(y_train,10)
# y_test=to_categorical(y_test,10)

# # print(f"x_train shape: {x_train.shape}")
# # print(f"x_test shape: {x_test.shape}")

# #build the model
# model=Sequential([
#     Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
#     MaxPooling2D((2,2)),
#     Flatten(),
#     Dense(64,activation='relu'),
#     Dropout(0.5),
#     Dense(10,activation='softmax')
# ])

# # print(model.summary())

# #compile the model
# model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

# #train the model
# model.fit(x_train,y_train,epochs=10,batch_size=32,validation_split=0.2)

# #evaluate the model
# test_loss,test_acc=model.evaluate(x_test,y_test)
# print(f"Test loss: {test_loss}, Test accuracy: {test_acc}")

# #save the model
# model.save('mnist_classifier_model.h5')

# #load the model
# from tensorflow.keras.models import load_model
# loaded_model=load_model('mnist_classifier_model.h5')

# #evaluate the loaded model
# loaded_test_loss,loaded_test_acc=loaded_model.evaluate(x_test,y_test)
# print(f"Loaded model test loss: {loaded_test_loss}, Loaded model test accuracy: {loaded_test_acc}")