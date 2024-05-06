import tensorflow as tf
from tflite_functions import DataGenerator_tflite, mover_archivo
import os
from get_video import remove_npy
import RPi.GPIO as GPIO
import time
os.environ["OMP_NUM_THREADS"] = "4"  ####################################
GPIO.setmode(GPIO.BCM)
pin_R = 17
pin_Y = 27
pin_G = 22
GPIO.setup(pin_R, GPIO.OUT)
GPIO.setup(pin_Y, GPIO.OUT)
GPIO.setup(pin_G, GPIO.OUT)

def blink_light(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(pin, GPIO.LOW)
#############################

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
    #interprete.set_num_threads(4) ####################################
    input_shape = interprete.get_input_details()[0]['shape']

    # print(input_shape)
    interprete.resize_tensor_input(0, input_shape, strict=True)
    interprete.allocate_tensors()

    input_details = interprete.get_input_details()[0]
    output_details = interprete.get_output_details()[0]
    input_model = DataGenerator_tflite(directory=npy_dir.format(dataset),
                                       batch_size_data=batch_size)
    batch_x = input_model.__getitem__(0)  # Use index 0 to get the first batch
    aux = 0
    for i in range(cant_archivos):
        print('Video: ', i)
        input_ = batch_x[i:i + 1]
        input_.reshape(input_shape)
        interprete.set_tensor(input_details['index'], input_)
        interprete.invoke()
        predictions = interprete.get_tensor(output_details['index'])
        file_name = input_model.dirs[i]

        print("Prob. de Violencia en el video", file_name, "->", predictions)

        # origen = os.path.join(npy_dir, file_name)
        # destino = os.path.join(chau_dir, file_name)

        # resultado = mover_archivo(origen, destino)
        aux = predictions[0][0]*100
        print(aux)
        if aux < 40:
            blink_light(pin_G)
            print('green')
        elif 40 <= aux < 55:
            blink_light(pin_Y)
            print('yellow')
        else:
            blink_light(pin_R)
            print('red')
        return predictions

    return [1,1]

#model = "model.tflite"
#avi_dir = '../../media/Images/AVI'
#npy_dir = "../../media/Images/NPY"


#predictions = predict_model(model, npy_dir)
#print(predictions)