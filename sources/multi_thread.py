import threading
import time
import os


def crear_txt(max_files):
    i = 1
    while True:
        # Create a directory if it doesn't exist
        os.makedirs("files", exist_ok=True)

        # Create a text file with a name based on the index
        with open(f"files/archivo{i}.txt", "w") as file:
            file.write(f"Contenido del archivo {i}")
        print(f"archivo{i}.txt creado.")

        i += 1
        if i > max_files:
            i = 1  # Reset the counter if it exceeds max_files

        time.sleep(0.5)


def procesar_txt(max_files, processing_files):
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
    max_files = 8
    processing_files = set()

    # Start the file creation thread
    threading.Thread(target=crear_txt, args=(max_files,)).start()

    # Start the file processing thread
    threading.Thread(target=procesar_txt, args=(max_files, processing_files)).start()
