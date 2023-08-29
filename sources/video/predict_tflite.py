import tensorflow as tf
import tflite_runtime.interpreter as tflite
# from tensorflow.lite.python.interpreter import OpResolverType
from tflite_functions import DataGenerator_tflite
# from tensorflow.keras.mixed_precision import global_policy, set_global_policy, Policy
# import traceback
# policy = global_policy()
# if policy.name == 'float32':
#     policy = Policy('mixed_float16')
# set_global_policy(policy)

model = "model.tflite"
npy_dir = "../../media/Images/NPY"

batch_size = 2
dataset = 'ViolentFlow-opt'

interprete = tf.lite.Interpreter(model_path=model, experimental_preserve_all_tensors=True)

#interprete = Interpreter(model_path=model) # ,
#                                 model_content=None,
#                                 experimental_delegates=None,
#                                 num_threads=1,
#                                 experimental_op_resolver_type=OpResolverType.AUTO,
#                                 experimental_preserve_all_tensors=False)

input_shape = interprete.get_input_details()[0]['shape']
interprete.resize_tensor_input(0, input_shape, strict=True)

input_details = interprete.get_input_details()[0]
output_details = interprete.get_output_details()[0]
print(input_details)
print(output_details)

interprete.allocate_tensors()

# Generate input
input_model = DataGenerator_tflite(directory=npy_dir.format(dataset),
                                   batch_size_data=batch_size,
                                   data_augmentation=False)

batch_x, batch_y = input_model.__getitem__(0)  # Use index 0 to get the first batch

interprete.set_tensor(input_details['index'], batch_x)

interprete.invoke()
# delta_time = time() - time_before
# print("Tiempo de predicción: ", delta_time)

predictions = interprete.get_tensor(output_details['index'])

print(predictions)
