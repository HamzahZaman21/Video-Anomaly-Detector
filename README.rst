======================
Video Anomaly Detector
======================

The supplemental notebook contains each step that was necessary to make the model.

The sample video was first split into individual frames using the convert_video_to_images function
The images were then loaded, normalized and reshaped to enable learning using the load_images function.

An autoencoder model was then created and trained.
The model included 3 encoding layers and 3 decoding layers
The model used Mean Squared Error (mse) as the loss function
The loss function was then plotted to find the optimum threashold
The  model was then saved

The predict function takes a frame as an input, loads the saved model and outputs if it is an anomaly or not.

Anamoly Detector file contains just the predict function, allowing it to be run seperately.