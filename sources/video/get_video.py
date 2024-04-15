import subprocess
import os


def get_video():
    comando_video_1 = "libcamera-vid -o ../../media/Images/AVI/video.h264 -t 5000 --width 224 --height 224 --framerate 60"
    subprocess.run(comando_video_1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Comando 1")

    if os.path.exists("../../media/Images/AVI/video.h264"):
        comando_video_2 = "ffmpeg -i ../../media/Images/AVI/video.h264 -c:v mpeg4 -b:v 4000k ../../media/Images/AVI/video.avi"
        subprocess.run(comando_video_2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if os.path.exists("../../media/Images/AVI/video.avi"):
            comando_video_3 = "y"
            subprocess.run(comando_video_3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("Comando 3")
        comando_video_4 = "rm ../../media/Images/AVI/video.h264"
        subprocess.run(comando_video_4, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Comando 4")


def remove_avi():
    archivo_a_eliminar = "../../media/Images/AVI/video.avi"
    if os.path.exists(archivo_a_eliminar):
        comando_remove = f"rm {archivo_a_eliminar}"
        subprocess.run(comando_remove, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Archivo {archivo_a_eliminar} eliminado.")
    else:
        print(f"El archivo {archivo_a_eliminar} no existe, no se puede eliminar.")


def remove_npy():
    archivo_a_eliminar = "../../media/Images/NPY/video.npy"

    if os.path.exists(archivo_a_eliminar):
        comando_remove = f"rm {archivo_a_eliminar}"
        subprocess.run(comando_remove, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Archivo {archivo_a_eliminar} eliminado.")
    else:
        print(f"El archivo {archivo_a_eliminar} no existe, no se puede eliminar.")
