# Moving_Object_Detection
This Python script utilizes the OpenCV library to perform basic motion detection through webcam input. The application captures consecutive frames, converts them to grayscale, and applies Gaussian blur for noise reduction. It then calculates the absolute difference between consecutive frames, creating a thresholded image to identify moving objects. Detected objects are outlined with rectangles, and a text notification is displayed. The script is equipped with a graphical user interface for real-time monitoring.

Directions:
1. Install required packages: Ensure you have OpenCV and imutils installed. You can install them using the following command:
   ```
   pip install opencv-python imutils
   ```

2. Run the script: Execute the script by running the provided Python code. The webcam will activate, and the application will display a window showing live video feed. Detected moving objects will be outlined with green rectangles, and a notification will appear on the screen.

3. Terminate the application: To exit the application, press the 'q' key. This will release the webcam resources and close the application window.

Note: Adjust the 'area' variable in the code to control the sensitivity of motion detection. Larger values will require larger movements to trigger detection.
