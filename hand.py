import cv2
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Function to preprocess the image
def preprocess_image(img):
    img = cv2.resize(img, (224, 224))  # Resize image to fit model input
    img = image.img_to_array(img)  # Convert image to numpy array
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = preprocess_input(img)  # Preprocess image for MobileNetV2
    return img

# Function to predict gesture from image
def predict_gesture(img):
    processed_img = preprocess_image(img)
    predictions = model.predict(processed_img)
    decoded_predictions = decode_predictions(predictions, top=1)[0]
    return decoded_predictions[0][1]  # Return the predicted gesture label

# Main function to capture video from webcam
def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Display the captured frame
        cv2.imshow('Hand Gesture Recognition', frame)

        # Use a region of interest (ROI) to isolate the hand area
        # This would require additional code for hand detection and ROI extraction
        
        # Example: Assume hand ROI is extracted and stored in hand_roi variable
        # hand_roi = frame[y:y+h, x:x+w]

        # Perform gesture recognition on the hand ROI
        gesture_label = predict_gesture(hand_roi)
        print(f"Predicted Gesture: {gesture_label}")

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
