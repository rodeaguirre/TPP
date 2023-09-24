from get_video import get_video, remove_avi, remove_npy
from predict_tflite import predict_model
from preprocess_video import Save2Npy
import threading

RGB_model = "model.tflite"
avi_dir = '../../media/Images/AVI'
npy_dir = "../../media/Images/NPY"


def captura_video(origin_dir, destin_dir):
    get_video()
    Save2Npy(file_dir=origin_dir, save_dir=destin_dir)
    pass


def inferencia_red(origin_dir, destin_dir, model):
    prediction = predict_model(model, npy_dir)
    while True:
        # Llama a la función de inferencia en el hilo/proceso secundario
        threading.Thread(target=captura_video, args=(origin_dir, destin_dir)).start()


captura_video(avi_dir, npy_dir)

# Mantener el programa principal en ejecución
while True:
    inferencia_red(avi_dir, npy_dir, RGB_model)
    pass
