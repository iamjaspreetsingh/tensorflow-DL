import tensorflow as tf
from keras.models import model_from_json

json_file = open('/home/jaspreet/Desktop/keras_to_tensorflow/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("/home/jaspreet/Desktop/keras_to_tensorflow/model.h5")
print("Loaded model from disk")
input_tensors=loaded_model.input
print(input_tensors)
path_to_frozen_graphdef_pb = '/home/jaspreet/Desktop/keras_to_tensorflow/model1.pb'
output_tensors = loaded_model.output
print(output_tensors)

