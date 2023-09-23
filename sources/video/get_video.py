import picamera
import cv2
import numpy as np

resize_dim = (224, 224)
fps = 30
# Configura la cámara de Raspberry Pi
camera = picamera.PiCamera()
camera.resolution = resize_dim

# Inicia la grabación en formato H.264
camera.start_recording('my_video.h264')
camera.wait_recording(60)
camera.stop_recording()

# Convierte el video H.264 a AVI
input_video = cv2.VideoCapture('my_video.h264')
output_video = cv2.VideoWriter('my_video.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, resize_dim)

while True:
    ret, frame = input_video.read()
    if not ret:
        break
    output_video.write(frame)

input_video.release()
output_video.release()

print("Conversión a AVI completa.")

'''
import sys
import os
import shutil
from time import time
import cv2
import datetime



class Ctes:
    DURATION_VIDEO_CUTS = 5

def filename_date():
    # Obtener la fecha y hora actual
    date_hour = datetime.datetime.now()

    # Formatear la fecha y hora actual en "ano_mes_dia_hora_minutos_segundos"
    formato = "%Y-%m-%d_%H-%M-%S"
    formatted_date_hour = date_hour.strftime(formato)

    return formatted_date_hour
def get_camera_fps():
    fps =60
    # Open the camera
    print("Cálculo de fps.")
    cap = cv2.VideoCapture(0)
    # Obtener la velocidad de cuadros por segundo
    fps = cap.get(cv2.CAP_PROP_FPS) or fps
    cap.release()
    print(fps)
    return fps
def getVideo(video_dir, fps):
    """Calculate dense optical flow from the camera feed
    Args:
        --
    Returns:
        flows_x: the optical flow at x-axis, with the shape of [frames,height,width,channel]
        flows_y: the optical flow at y-axis, with the shape of [frames,height,width,channel]
    """
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)

    resize_dim = (224, 224)

    # Calcular la cantidad de cuadros necesarios
    num_frames = int(fps * Ctes.DURATION_VIDEO_CUTS)

    # Especificar el codec de compresión y la configuración del video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec XVID

    file_name = filename_date()
    save_video_path = os.path.join(video_dir, file_name + '.avi')

    # Open the camera
    cap = cv2.VideoCapture(0)
    print("Se enciende la cámara.")

    # Crear un objeto VideoWriter para guardar el video
    out = cv2.VideoWriter(save_video_path, fourcc, fps, resize_dim)

    i = 0
    while i < num_frames:  # - 1:
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.resize(frame, resize_dim, interpolation=cv2.INTER_AREA)
        out.write(frame)
        # Exit the loop if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        i += 1

    # Release the camera and destroy all windows
    cap.release()
    print("Se apaga la cámara.")
    out.release()
    print("Video almacenado.")
    cv2.destroyAllWindows()
    return save_video_path

video_dir = 'AVI'

num_videos = 1
fps = get_camera_fps()

for i in range(1, num_videos + 1):

    time_before = time()
    # Take Video
    video_path = getVideo(video_dir, fps)

    delta_time = time() - time_before
    print("Tiempo de getVideo: ", delta_time)

'''