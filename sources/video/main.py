from get_video import get_video, remove_avi, remove_npy
from predict_tflite import predict_model
from preprocess_video import Save2Npy

model = "model.tflite"
avi_dir = '../../media/Images/AVI'
npy_dir = "../../media/Images/NPY"

get_video()
Save2Npy(file_dir=avi_dir, save_dir=npy_dir)
predictions = predict_model(model, npy_dir)
remove_avi()
remove_npy()
