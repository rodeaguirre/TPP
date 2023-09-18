import tensorflow as tf
import tflite_runtime.interpreter as tflite
# from tensorflow.lite.python.interpreter import OpResolverType
from tflite_functions import DataGenerator_tflite


model = "model.tflite"
npy_dir = "../../media/Images/NPY"

batch_size = 3
dataset = 'ViolentFlow-opt'
interprete = tf.lite.Interpreter(model)

input_shape = interprete.get_input_details()[0]['shape']

# print(input_shape)
interprete.resize_tensor_input(0, input_shape, strict=True)
interprete.allocate_tensors()

input_details = interprete.get_input_details()[0]
output_details = interprete.get_output_details()[0]


# Generate input
input_model = DataGenerator_tflite(directory=npy_dir.format(dataset),
                                   batch_size_data=batch_size,
                                   data_augmentation=False)
batch_x, batch_y = input_model.__getitem__(0)  # Use index 0 to get the first batch
print(batch_x.shape)


for i in range(batch_size):
    input_ = batch_x[i:i+1]
    print(input_.shape)
    input_.reshape(input_shape)
    interprete.set_tensor(input_details['index'], input_)
    interprete.invoke()
    predictions = interprete.get_tensor(output_details['index'])
    print(predictions)

