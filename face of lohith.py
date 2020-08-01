import face_recognition
import cv2
import numpy as np  
import pyttsx3  
import speech_recognition as sr 
import random
import glob
import math

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Initiating Biometric Face Recognition Mode")  
speak("Scanning for faces")  
# Get a referee to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
lohith_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Camera Roll/LOLU pandey.jpg")
lohith_face_encoding = face_recognition.face_encodings(lohith_image)[0]

# Load a second sample picture and learn how to recognize it.
billgates_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/bill gates.png")
billgates_face_encoding = face_recognition.face_encodings(billgates_image)[0]

shan_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Shankarappa.jpg")
shan_face_encoding = face_recognition.face_encodings(shan_image)[0]

resh_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Reshma.jpg")
resh_face_encoding = face_recognition.face_encodings(resh_image)[0]

kump_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Kumaraswamy.jpg")
kump_face_encoding = face_recognition.face_encodings(kump_image)[0]

modi_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/NarendraModi.jpg")
modi_face_encoding = face_recognition.face_encodings(modi_image)[0]

stark_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Tony Stark.jpg")
stark_face_encoding = face_recognition.face_encodings(stark_image)[0]

gandhi_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Gandhi.jpg")
gandhi_face_encoding = face_recognition.face_encodings(gandhi_image)[0]

obama_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Barack Obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    lohith_face_encoding,
    billgates_face_encoding,
    shan_face_encoding,
    resh_face_encoding,
    kump_face_encoding,
    modi_face_encoding,
    stark_face_encoding,
    gandhi_face_encoding,
    obama_face_encoding,
]
known_face_names = [
    "Lohith.S",
    "Bill Gates",
    "Shankar",
    "Reshma",
    "Kumaraswamy",
    "Narendra Modi",
    "Tony Stark",
    "Gandhi",
    "Barack Obama"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True



while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #text = "Jarvis 2.0"
    #for (top, right, bottom, left):
        #bottom *= 4
        #left *= 4
    #cv2.putText(frame,text,(210,40), font,1.2, (139,0,0), 2)
    #cv2.line(frame,(120,10),(200,50),(139,0,0),2)
    #cv2.putText(frame,'Hola',(20,100), font,1.2, (139,0,0), 2)
    #cv2.line(frame,(200,50),(400,50),(139,0,0),2)
    #cv2.line(frame,(500,10),(400,50),(139,0,0),2)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown face"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)             
        process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 255, 0), 1)

    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()