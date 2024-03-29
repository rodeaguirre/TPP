import cv2
import numpy as np
import os
#from tqdm import tqdm


def uniform_sampling(video, target_frames=64):
    # print("uniform_sampling")
    # get total frames of input video and calculate sampling interval
    len_frames = int(len(video))
    interval = int(np.ceil(len_frames / target_frames))
    # init empty list for sampled video and
    sampled_video = []
    for i in range(0, len_frames, interval):
        sampled_video.append(video[i])
        # calculate numer of padded frames and fix it
    num_pad = target_frames - len(sampled_video)
    if num_pad > 0:
        padding = [video[i] for i in range(-num_pad, 0)]
        sampled_video += padding
        # get sampled video
    return np.array(sampled_video, dtype=np.float32)


def Video2Npy(file_path, resize=(224, 224)):
    """Load video and tansfer it into .npy format
    Args:
        file_path: the path of video file
        resize: the target resolution of output video
    Returns:
        frames: gray-scale video
        flows: magnitude video of optical flows
    """
    # Load video
    cap = cv2.VideoCapture(file_path)
    # Get number of frames
    len_frames = int(cap.get(7))  # = cv2.CAP_PROP_FRAME_COUNT
    # Extract frames from video
    try:
        frames = []
        for i in range(len_frames - 1):
            _, frame = cap.read()
            frame = cv2.resize(frame, resize, interpolation=cv2.INTER_AREA)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.reshape(frame, (224, 224, 3))
            frames.append(frame)
    except:
        print("Error: ", file_path, len_frames, i)
    finally:
        frames = np.array(frames)
        cap.release()

    # Get the optical flow of video
    # flows = getOpticalFlow(frames)

    result = np.zeros((len(frames), 224, 224, 3))
    result = frames
    result = uniform_sampling(result)
    return result


def Save2Npy(file_dir, save_dir):
    """Transfer all the videos and save them into specified directory
    Args:
        file_dir: video folder of target videos
        save_dir: destination folder of output .npy files
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    # List the files
    videos = os.listdir(file_dir)
    #for v in tqdm(videos):
    for v in videos:
        # Split video name
        video_name = v.split('.')[0]
        # Get src
        video_path = os.path.join(file_dir, v)
        # Get dest
        save_path = os.path.join(save_dir, video_name + '.npy')
        # Load and preprocess video
        data = Video2Npy(file_path=video_path, resize=(224, 224))
        data = np.uint8(data)
        # Save as .npy file
        np.save(save_path, data)

    return None
