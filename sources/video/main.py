from get_video import get_video, remove_avi, remove_npy
from predict_tflite import predict_model
from preprocess_video import Save2Npy
#from pi_UART import UART_init,UART_print


model = "model.tflite"
avi_dir = '../../media/Images/AVI'
npy_dir = "../../media/Images/NPY"

#UART_init()

for i in range(3):
    print("Get_video")
    get_video()
    print("Save2Npy")
    Save2Npy(file_dir=avi_dir, save_dir=npy_dir)
    print("predict_model")
    predictions = predict_model(model, npy_dir)
    print("remove_avi")
    remove_avi()
    print("remove_npy")
    remove_npy()
    #UART_print(predictions)
    print("  --  \n")