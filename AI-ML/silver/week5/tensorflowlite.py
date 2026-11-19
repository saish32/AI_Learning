# import tensorflow as tf

# model=tf.keras.models.load_model('my_model.h5')  # Load the entire model from the HDF5 file

# #convert the model to TensorFlow Lite format
# converter = tf.lite.TFLiteConverter.from_keras_model(model)
# tflite_model = converter.convert()

# #save the TensorFlow Lite model to a file
# with open('my_model.tflite', 'wb') as f:
#     f.write(tflite_model)

# import numpy as np
# # Load the TensorFlow Lite model
# interpreter = tf.lite.Interpreter(model_path='my_model.tflite')
# interpreter.allocate_tensors()

# #get input and output tensors
# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# #prepare input data (replace this with your actual input data)
# input_data = np.array([[1.0, 2.0, 3.0]], dtype=np.float32)  # Example input data
# output_data = np.array([[0.0, 0.0, 0.0]], dtype=np.float32)  # Example output data

# # Set the input tensor
# interpreter.set_tensor(input_details[0]['index'], input_data)

# # Run the model
# interpreter.invoke()

# # Get the output tensor
# output = interpreter.get_tensor(output_details[0]['index'])