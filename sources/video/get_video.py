import subprocess

def get_video():
    comando_video_1 = "libcamera-vid -o ../../media/Images/AVI/video.h264 -t 5000 --width 224 --height 224 --framerate 60"
    subprocess.run(comando_video_1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    comando_video_2 = "ffmpeg -i ../../media/Images/AVI/video.h264 -c:v mpeg4 -b:v 4000k ../../media/Images/AVI/video.avi"
    subprocess.run(comando_video_2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    comando_video_3 = "rm ../../media/Images/AVI/video.h264"
    subprocess.run(comando_video_3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def remove_avi():
    comando_remove = "rm ../../media/Images/AVI/video.avi"
    subprocess.run(comando_remove, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def remove_npy():
    comando_remove = "rm ../../media/Images/NPY/video.npy"
    subprocess.run(comando_remove, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
