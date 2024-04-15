from get_video import get_video, remove_avi, remove_npy
from predict_tflite import predict_model
from preprocess_video import Save2Npy
#from pi_UART import UART_init,UART_print
import RPi.GPIO as GPIO
import time

########Semaforo###########
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



model = "model.tflite"
avi_dir = '../../media/Images/AVI'
npy_dir = "../../media/Images/NPY"

#UART_init()



for i in range(3):
    print("remove_avi")
    remove_avi()
    print("remove_npy")
    remove_npy()
    print("Get_video")
    get_video()
    print("Save2Npy")
    Save2Npy(file_dir=avi_dir, save_dir=npy_dir)
    print("predict_model")
    predictions = predict_model(model, npy_dir)
    #UART_print(predictions)
    print("  --  \n")

    if predictions[1] < 40:
        blink_light(pin_G)
    elif predictions[1] >= 40 & predictions[1] < 55:
        blink_light(pin_Y)
    else:
        blink_light(pin_R)