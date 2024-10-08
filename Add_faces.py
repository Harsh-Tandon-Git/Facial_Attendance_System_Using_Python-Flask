import sys
import cv2
import pickle
import numpy as np
import os
import time
from datetime import datetime

def add_face(name):
    
    video = cv2.VideoCapture(0)

    
    facedetect = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')

    
    faces_data = []

    
    i = 0

    
    while True:
        # Capture a frame from the video
        ret, frame = video.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = facedetect.detectMultiScale(gray, 1.3, 5)

        
        for (x, y, w, h) in faces:
            # Crop the face region from the frame
            crop_img = frame[y:y+h, x:x+w, :]

            
            resized_img = cv2.resize(crop_img, (50, 50))

            
            if len(faces_data) <= 5 and i % 5 == 0:
                faces_data.append(resized_img)

            i = i + 1

            # Display the count of captured faces on the frame
            cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)

       
        cv2.imshow("Frame", frame)

        # Wait for a key press or until 5 faces are captured
        k = cv2.waitKey(1)
        if k == ord('q') or len(faces_data) == 5:
            break

    
    video.release()
    cv2.destroyAllWindows()

    # Convert the list of face images to a NumPy array and reshape it
    faces_data = np.asarray(faces_data)
    faces_data = faces_data.reshape(5, -1)

    
    if 'names.pkl' not in os.listdir('Data/'):
        # If not present, create a list with the entered name repeated 5 times
        names = [name] * 5
        # Save the list to 'names.pkl'
        with open('Data/names.pkl', 'wb') as f:
            pickle.dump(names, f)
    else:
        # If 'names.pkl' is present, load the existing list
        with open('Data/names.pkl', 'rb') as f:
            names = pickle.load(f)
        # Append the entered name 5 times to the existing list
        names = names + [name] * 5
        # Save the updated list to 'names.pkl'
        with open('Data/names.pkl', 'wb') as f:
            pickle.dump(names, f)

   
    if 'faces_data.pkl' not in os.listdir('Data/'):
        # If not present, save the NumPy array 'faces_data' to 'faces_data.pkl'
        with open('Data/faces_data.pkl', 'wb') as f:
            pickle.dump(faces_data, f)
    else:
        # If 'faces_data.pkl' is present, load the existing array
        with open('Data/faces_data.pkl', 'rb') as f:
            faces = pickle.load(f)
        
        faces = np.append(faces, faces_data, axis=0)
       
        with open('Data/faces_data.pkl', 'wb') as f:
            pickle.dump(faces, f)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Add_faces.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    add_face(name)
