import tensorflow as tf
from tensorflow import keras

#load the pre-trained model (e.g., VGG16) without the top classification layer
base_model = keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

#feature extraction: freeze the base model layers to prevent them from being updated during training
base_model.trainable = False
model = keras.Sequential([
    base_model,
    keras.layers.Flatten(),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(10, activation='softmax')  #assuming 10 classes for the new task
])

#fine-tuning: unfreeze some of the top layers of the base model for further training
base_model.trainable = True
for layer in base_model.layers[:-4]:  #freeze all layers except the last 4
    layer.trainable = False

#train the model on the new dataset
model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-4), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(new_train_data, new_train_labels, epochs=10, batch_size=32, validation_data=(new_val_data, new_val_labels))
test_loss, test_acc = model.evaluate(new_test_data, new_test_labels, verbose=2)
print(f"Test accuracy: {test_acc}")
print(f"Test loss: {test_loss}")