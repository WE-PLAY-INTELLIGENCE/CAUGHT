import cv2
import numpy as np

# Load your pre-trained model and video capture source

# # #Load the saved model
# model = models.load_model('model.h5')   ##Trained Respectively 
# video = cv2.VideoCapture(0)


# Define a list of colors for each class
class_colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]  # Define colors for different classes rgb values 
class_labels = ["Class 0", "Class 1", "Class 2"]  # Corresponding labels for the classes name according to trained model 

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Perform object detection with your model and obtain a list of detected objects
    detected_objects = detect_objects(frame, model)

    # Iterate through the detected objects and draw bounding boxes
    for obj in detected_objects:
        class_id, confidence, x, y, width, height = obj

        # Convert the coordinates and dimensions to integers
        x, y, width, height = int(x), int(y), int(width), int(height)

        # Use class ID to determine the color and label
        if class_id < len(class_colors):
            color = class_colors[class_id]
            label = class_labels[class_id]
        else:
            color = (0, 0, 0)  # Default color for unknown classes
            label = "Unknown"

        # Draw the bounding box
        cv2.rectangle(frame, (x, y), (x + width, y + height), color, 2)  # 2 is the thickness of the rectangle

        # Draw the label above the bounding box
        cv2.putText(frame, f"{label} ({confidence:.2f})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
