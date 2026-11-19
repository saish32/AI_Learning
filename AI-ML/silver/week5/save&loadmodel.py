# model.save('my_model.h5')  # Save the entire model to a HDF5 file

# #save model architecture to JSON
# model_json = model.to_json()
# with open("my_model.json", "w") as json_file:
#     json_file.write(model_json)

# # Save the model weights to a HDF5 file
# model.save_weights("my_model_weights.h5")  # Save the model weights to a HDF5 file

# #load the entire model from the HDF5 file
# loaded_model = tf.keras.models.load_model('my_model.h5')

# #load model architecture from JSON
# with open('my_model.json', 'r') as json_file:
#     loaded_model_json = json_file.read()
# loaded_model = tf.keras.models.model_from_json(loaded_model_json)
# loaded_model.load_weights("my_model_weights.h5")  # Load the model weights from the HDF5 file

