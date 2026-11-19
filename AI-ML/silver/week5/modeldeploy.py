# #docker pull tensorflow/serving:latest

# import tensorflow as tf

# model=tf.keras.models.load_model('my_model.h5')  # Load the entire model from the HDF5 file
# tf.saved_model.save(model, 'saved_model/my_model')  # Save the model in TensorFlow SavedModel format

# #running the TensorFlow Serving Docker container
# docker run -p 8501:8501 --name=tf_serving_my_model --
# mount type=bind,source=$(pwd)/saved_model/my_model,target=/models/my_model -e MODEL_NAME=my_model -t tensorflow/serving:latest
# -e MODEL_NAME=my_model -t tensorflow/serving:latest

# curl -d '{"instances": [[1.0, 2.0, 3.0]]}' -X POST http://localhost:8501/v1/models/my_model:predict

