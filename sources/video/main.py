from get_video import get_video, remove_avi, remove_npy
from predict_tflite import predict_model
from preprocess_video import Save2Npy
#from pi_UART import UART_init,UART_print
import time


model = "model_111023_HybridQuantization.tflite"
avi_dir = '../../media/Images/AVI'
npy_dir = "../../media/Images/NPY"

#UART_init()



for i in range(10):
    print("remove_avi")
    remove_avi()
    print("remove_npy")
    remove_npy()
    print("Get_video")
    get_video()
    print("Save2Npy")
    Save2Npy(file_dir=avi_dir, save_dir=npy_dir)
    print("predict_model")
    inicio = time.time()
    predictions = predict_model(model, npy_dir)
    tiempo_transcurrido = time.time() - inicio
    print(tiempo_transcurrido)
    #UART_print(predictions)
    print("  --  \n")
