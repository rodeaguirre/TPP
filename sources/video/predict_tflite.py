import tensorflow as tf
from tflite_functions import DataGenerator_tflite, mover_archivo
import os
from get_video import remove_npy


def predict_model(model, npy_dir):
    # Obtén la lista de archivos en el directorio npy_dir
    archivos = os.listdir(npy_dir)

    # Usa una comprensión de lista para filtrar solo los archivos (no directorios)
    # archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(npy_dir, archivo))]

    cant_archivos = len(archivos)

    batch_size = cant_archivos
    print(cant_archivos)
    dataset = 'ViolentFlow-opt'

    # Obtén la lista de archivos en el directorio npy_dir

    interprete = tf.lite.Interpreter(model)

    input_shape = interprete.get_input_details()[0]['shape']

    # print(input_shape)
    interprete.resize_tensor_input(0, input_shape, strict=True)
    interprete.allocate_tensors()

    input_details = interprete.get_input_details()[0]
    output_details = interprete.get_output_details()[0]
    input_model = DataGenerator_tflite(directory=npy_dir.format(dataset),
                                       batch_size_data=batch_size)
    batch_x = input_model.__getitem__(0)  # Use index 0 to get the first batch

    for i in range(cant_archivos):
        print('Video: ', i)
        input_ = batch_x[i:i + 1]
        input_.reshape(input_shape)
        interprete.set_tensor(input_details['index'], input_)
        interprete.invoke()
        predictions = interprete.get_tensor(output_details['index'])
        file_name = input_model.dirs[i]

        print("Prob. de Violencia en el video",file_name, "->", predictions)

        # origen = os.path.join(npy_dir, file_name)
        # destino = os.path.join(chau_dir, file_name)

        # resultado = mover_archivo(origen, destino)


