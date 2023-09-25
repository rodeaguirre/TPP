import threading
import time
import os

from get_video import get_video, remove_avi, remove_npy
from predict_tflite import predict_model
from preprocess_video import Save2Npy

RGB_model = "model.tflite"
avi_dir = '../../media/Images/AVI'
npy_dir = "../../media/Images/NPY"

def capture_video(max_files, avi_dir):
    i = 1
    while True:

        # Create a text file with a name based on the index
        with open(f"{avi_dir}/archivo{i}.txt", "w") as file:
            file.write(f"Contenido del archivo {i}")
        print(f"archivo{i}.txt creado.")

        i += 1
        if i > max_files:
            i = 1  # Reset the counter if it exceeds max_files

        time.sleep(30)


def predict_video(max_files, processing_files):
    while True:
        time.sleep(3)  # Simulate processing time

        # Find the latest file to process
        latest_file_index = max_files
        while not os.path.exists(f"files/archivo{latest_file_index}.txt") and latest_file_index > 1:
            latest_file_index -= 1

        if latest_file_index > 1:
            ultimo_archivo = f"files/archivo{latest_file_index}.txt"
            print(f"Procesando archivo {ultimo_archivo}...")

            # Track the file being processed
            processing_files.add(ultimo_archivo)

            # Delete files that are not being processed
            for filename in os.listdir("files"):
                filepath = os.path.join("files", filename)
                if filepath != ultimo_archivo and os.path.isfile(filepath) and filepath not in processing_files:
                    os.remove(filepath)
                    print(f"Archivo {filepath} eliminado.")

            # Remove the processed file from the set
            processing_files.remove(ultimo_archivo)


if __name__ == "__main__":
    max_files = 3
    processing_files = set()

    # Start the file creation thread
    threading.Thread(target=capture_video, args=(max_files,avi_dir)).start()

    # Start the file processing thread
    threading.Thread(target=predict_video, args=(max_files, processing_files)).start()
