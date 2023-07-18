import cv2
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras

model_path = 'Keras_Model'
frame_path = "Image Folder\\frame0850.jpg"
frame = Image.open(frame_path)

def predict(frame):
    """
    Argument
    --------
    frame : Video frame with shape == (44, 60, 3) and dtype == float.
    Return
    anomaly : A boolean indicating whether the frame is an anomaly or not.
    Rough Estimates:
        threashold for max sensitivity = 0.0010316
        threashold for max specificity = 0.0011981
        avg threashold = 0.0011485
    ------
    """
    im_array = np.array(frame.resize((60, 44)))
    im = im_array.astype(np.float32) / 255.
    im = im.reshape((1, -1))
    loaded_model = tf.keras.models.load_model(model_path)
    loss = loaded_model.evaluate(im, im, verbose = 0)
    anomaly = False
    if loss>0.0011485:
        anomaly = True

    # Your fancy computations here!!
    return anomaly

predict(frame)