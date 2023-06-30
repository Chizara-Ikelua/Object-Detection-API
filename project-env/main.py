import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# To initialize the camera 
cap = cv2.VideoCapture(0)  # Put 0 for laptop camera and 1 for USB camera (adjust accordingly)

# Read the first frame 
ret, frame = cap.read()

# Convert the frame to grayscale 
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Variables for login state
login_successful = False
login_attempts = 0
max_login_attempts = 3

# Loop through the frame to grayscale 
while True:
    # Read the next frame 
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray_next = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    #Detect eyes 
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Calculate the absolute difference between the current and previous frame 
    diff = cv2.absdiff(gray, gray_next)

    # Apply thresholding to highlight the regions with significant differences
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    #Display the resulting frame 
    cv2.imshow('Motion Detection', thresh)

    # Update the previous frame
    gray = gray_next

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Draw rectangles around the detected eyes
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Face and Eye Detection', frame)

     # Check if both a face and eyes are detected
    if len(faces) > 0 and len(eyes) > 0:
        login_successful = True
        break

    # Increment login attempts
    login_attempts += 1

    # Exit the loop if max login attempts reached
    if login_attempts >= max_login_attempts:
        break

    # Display login attempts information
    print(f"Login attempts: {login_attempts}/{max_login_attempts}")

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows 
cap.release()
cv2.destroyAllWindows()

# Check login result
if login_successful:
    print("Login successful!")
else:
    print("Login failed.")
