import threading
import time
from get_video import get_video, remove_avi, remove_npy
from predict_tflite import predict_model
from preprocess_video import Save2Npy
'''
# Función que representa la inferencia del modelo en un thread
def inference_thread(model_path, input_data):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_shape = input_details[0]['shape']

    input_data = np.array(input_data, dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print("Output from thread:", output_data)

'''
# Definir la ruta al modelo TensorFlow Lite
model = 'model.tflite'
avi_dir = '../../media/Images/AVI'
npy_dir = "../../media/Images/NPY"

print("remove_avi")
remove_avi()
print("remove_npy")
remove_npy()
print("Get_video")
get_video()
print("Save2Npy")
Save2Npy(file_dir=avi_dir, save_dir=npy_dir)

# Crear y ejecutar los threads
threads = []
inicio = time.time()
for _ in range(4):
    #thread = threading.Thread(target=inference_thread, args=(model_path, input_data))
    thread = threading.Thread(target=predict_model, args=(model, npy_dir))
    threads.append(thread)
    thread.start()
    time.sleep(15)

# Esperar a que todos los threads terminen
for thread in threads:
    thread.join()

print("All threads have finished.")
tiempo_transcurrido = time.time() - inicio
print(tiempo_transcurrido)