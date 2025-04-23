import cv2
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image

def detect_emotion():
    # Load emotion detection model
    model = model_from_json(open("model/facial_expression_model_structure.json", "r").read())
    model.load_weights('model/facial_expression_model_weights.h5')
    
    # Load face detection cascade classifier
    face_cascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
    
    # Define emotion labels
    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    
    # Start webcam
    cap = cv2.VideoCapture(0)
    
    print("Press 'q' to quit")
    
    while True:
        # Capture frame from webcam
        ret, img = cap.read()
        
        if not ret or img is None:
            print("Error: Unable to capture frame.")
            break
            
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            # Draw rectangle around face
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Extract and preprocess face
            detected_face = img[int(y):int(y+h), int(x):int(x+w)]
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)
            detected_face = cv2.resize(detected_face, (48, 48))
            
            # Prepare image for prediction
            img_pixels = image.img_to_array(detected_face)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels /= 255
            
            # Predict emotion
            predictions = model.predict(img_pixels)
            max_index = np.argmax(predictions[0])
            emotion = emotions[max_index]
            
            # Display emotion text
            cv2.putText(img, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        # Show the result
        cv2.imshow('Emotion Detection', img)
        
        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_emotion()