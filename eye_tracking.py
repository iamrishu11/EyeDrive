import cv2  # Import the OpenCV library for computer vision tasks

def detect_eyes(frame, face_cascade, eye_cascade):
    """
    Detects faces and eyes in the given frame and highlights them.
    
    Parameters:
        frame (numpy.ndarray): The image frame from the video feed.
        face_cascade (cv2.CascadeClassifier): Pre-trained Haar cascade for face detection.
        eye_cascade (cv2.CascadeClassifier): Pre-trained Haar cascade for eye detection.
    
    Returns:
        numpy.ndarray: The frame with detected faces and eyes highlighted.
    """
    # Convert the frame to grayscale for better detection performance
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

    # Loop through each detected face
    for (x, y, w, h) in faces:
        # Define the region of interest (ROI) for both grayscale and color images
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        
        # Detect eyes within the ROI (the detected face)
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Loop through each detected eye
        for (ex, ey, ew, eh) in eyes:
            # Draw a rectangle around the detected eye
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            
            # Calculate the center of the detected eye
            eye_center = (x + ex + ew // 2, y + ey + eh // 2)
            
            # Draw a circle at the center of the detected eye
            cv2.circle(frame, eye_center, 2, (0, 0, 255), 3)
            
            # Print the coordinates of the eye center to the console
            print(f"Looking at: {eye_center}")

    return frame  # Return the frame with detected eyes highlighted

def main():
    """
    Main function to capture video from the webcam, detect faces and eyes,
    and display the results in a full-screen window.
    """
    # Load Haar cascades for face and eye detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # Open the default webcam (camera index 0)
    cap = cv2.VideoCapture(0)

    """
    # Create a window named "Eye Tracking"
    cv2.namedWindow('Eye Tracking', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Eye Tracking', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    """

    # Continuously capture frames from the webcam
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        # Break the loop if no frame is captured
        if not ret:
            break

        # Detect and highlight faces and eyes in the current frame
        frame = detect_eyes(frame, face_cascade, eye_cascade)

        # Display the processed frame in the full-screen window
        cv2.imshow('Eye Tracking', frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam resource and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Ensure that the main function is executed only if this script is run directly
if __name__ == '__main__':
    main()
