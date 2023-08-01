# Object-Detection-API
# Face/Eye Detection Web Application

This is a software that is a python based web application that performs face and eyee detection using OpenCV and Flask framework. This application captures live video from the camera, detects motion in the video stream and identifies faces and eyes in real time.

## Prerequisites 

In order to run this application, make sure you have the following on your computer:

1. The latest version of python instaled on your computer
2. Installation of Flask which is a lightweight web framework for python. it can be installed using the following command:

      pip install Flask

3. Installation of OpenCV, which is an open source vision library. It can be installed using the following command: 
    
    pip install opencv-python

4. Download the Haar cascades. This face/eye detection web application uses Haar cascades for face and eye detection and the required XML files are included in the OpenCv package so they don't need to be downloaded seperately. 

## Understanding the code: 
The first thing I did was initialize the camera using the 'cv2.VideoCapture()' function. If you havbe more thann oe camera, you have to djust the camera index. 0 will be for the laptop camera and 1 for the USB camera. 

- The motion detection algorithm calculates the absolute difference between consecutive grayscale frames to detect changes. 

- The face and eye detection algorithms utilize Haar cascades that are provided by OpenCV the detected faces are then enclosed in green rectangles while the detected eyes areenclosed in blue rectangles.  

- This application uses Flask to create a web server and serve the video stream to the user interface. OpenCV is then used to capture video from the camera, process the frames, and perform face and eye detecton using the Haar cascades. 

- Once the user is logged in, the user can view the vdeo stream fro the cmamera. The appliation continuously captures frames from the camera and then processes it. It then performs motion detection by calculating the absolute difference between consecutive frames and applies thresholding to highlight regions with significant differences. 

## How to use the application. 
After the code is run, the user will be prompted for the username and password to log in. for this code, the username is "admin", while the password is "password."

Once the user is logged in, you can view the video stream and observe the motion detection & face and eye detection in real time.

If the face and eyes are detected simultaneously, the application will prompt the user to enter the username and password.If the correct credentials are provided, the login will be successful, and the user will gain access. 

The application will also terminate after three unsuccessful login attempts or when you press the 'q' key on the video stream window. 

## DISCLAIMER
This application serves as a demonstration of motion detection as well as face and eye detection using OpenCV and Flask. It uses a basic login mechanism and is only beig used for demonstratin purposes and not for secure real world cases. For production applications, a more secure authentication mechanism should be implemented. 
