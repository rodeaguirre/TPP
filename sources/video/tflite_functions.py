import os
import cv2
import numpy as np
from tensorflow.keras import utils
from tensorflow.keras.utils import Sequence
import shutil

########################################################
def mover_archivo(origen, destino):
    try:
        # Verificar si el archivo de origen existe
        if not os.path.isfile(origen):
            return f"El archivo {origen} no existe."

        # Mover el archivo al destino
        shutil.move(origen, destino)

        return f"El archivo {origen} se ha movido a {destino} exitosamente."

    except Exception as e:
        return f"Error al mover el archivo: {str(e)}"


class DataGenerator_tflite(Sequence):
    """Data Generator inherited from keras.utils.Sequence
    Args:
        directory: the path of data set, and each sub-folder will be assigned to one class
        batch_size_data: the number of data points in each batch
        shuffle: whether to shuffle the data per epoch
    Note:
        If you want to load file with other data format, please fix the method of "load_data" as you want
    """

    def __init__(self, directory, batch_size_data=1):
        # Initialize the params
        self.dirs = None
        self.batch_size = batch_size_data
        self.directory = directory
        self.x_path = self.search_data()
        self.indexes = np.arange(len(self.x_path))
        self.n_files = len(self.x_path)


    def search_data(self):
        X_path = []
        # list all kinds of sub-folders
        self.dirs = sorted(os.listdir(self.directory))
        folder_path = os.path.join(self.directory)
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            # append each file path, and keep its label
            X_path.append(file_path)
        return X_path


    def __getitem__(self, index):
        """Get the data of each batch
        """
        # get the indexes of each batch
        batch_indexes = self.indexes[index * self.batch_size:(index + 1) * self.batch_size]
        # using batch_indexes to get path of current batch
        batch_path = [self.x_path[k] for k in batch_indexes]
        # get batch data
        batch_x = self.data_generation(batch_path)
        return batch_x

    def data_generation(self, batch_path):
        # load data into memory, you can change the np.load to any method you want
        batch_x = [self.load_data(d) for d in batch_path]
        # transfer the data format and take one-hot coding for labels
        batch_x = np.array(batch_x, dtype=np.float32)

        return batch_x

    def normalize(self, data):
        mean = np.mean(data)
        std = np.std(data)
        return (data - mean) / std


    def load_data(self, path):
        # load the processed .npy files which have 5 channels (1-3 for RGB, 4-5 for optical flows)
        data = np.load(path, mmap_mode='r', allow_pickle=True)  # , allow_pickle=True)  ##########################
        data = self.normalize(data)
        return data

