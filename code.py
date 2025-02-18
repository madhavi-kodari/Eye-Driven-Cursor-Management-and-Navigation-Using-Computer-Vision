import cv2  # For video capture and processing
import mediapipe as mp  # For face and eye landmark detection
import pyautogui  # For controlling the mouse cursor
from pynput import keyboard  # For handling global keyboard inputs

# Initialize webcam and Mediapipe Face Mesh
cam = cv2.VideoCapture(0)  # Open the webcam (0 is usually the default webcam)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)  # Initialize Mediapipe FaceMesh for detecting facial landmarks
screen_w, screen_h = pyautogui.size()  # Get the screen dimensions for cursor mapping

# Variables
enable_cursor = True  # Toggle to enable or disable cursor movement
enable_detection = True  # Toggle to enable or disable webcam detection
cursor_speed = 1.5  # Multiplier to control the speed of cursor movement
running = True  # Flag to keep the program running until explicitly stopped
blink_counter = 0  # Counter to track consecutive blinks for detecting right-click
blink_threshold = 2  # Threshold for the number of blinks to trigger a right-click

# Function to handle global keyboard inputs
def on_press(key):
    global enable_cursor, enable_detection, running  # Access the global variables
    try:
        # Stop the program when 'q' is pressed
        if key.char == 'q':
            running = False
            print("Exiting...")
        # Toggle cursor movement on/off when 't' is pressed
        elif key.char == 't':
            enable_cursor = not enable_cursor
            status = "Enabled" if enable_cursor else "Disabled"
            print(f"Cursor movement {status}")
        # Toggle webcam detection on/off when 'w' is pressed
        elif key.char == 'w':
            enable_detection = not enable_detection
            status = "Enabled" if enable_detection else "Disabled"
            print(f"Webcam detection {status}")
    except AttributeError:
        pass  # Handle special keys that do not have a 'char' attribute

# Start listening for global keyboard events
listener = keyboard.Listener(on_press=on_press)  # Initialize keyboard listener
listener.start()  # Start listening for keyboard inputs

while running:  # Main loop to run until explicitly stopped
    if enable_detection:  # Check if webcam detection is enabled
        # Capture a frame from the webcam
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a mirror effect
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB for Mediapipe processing
        output = face_mesh.process(rgb_frame)  # Process the frame to detect face landmarks
        landmark_points = output.multi_face_landmarks  # Get the detected landmarks
        frame_h, frame_w, _ = frame.shape  # Get the dimensions of the webcam frame

        if landmark_points:  # If face landmarks are detected
            # Display a message on the frame
            cv2.putText(frame, "Face Detected", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            landmarks = landmark_points[0].landmark  # Extract the first set of face landmarks
            eyes_detected = False  # Initialize eye detection flag

            # Define eye regions using specific landmark indices for left and right eyes
            left_eye = [landmarks[i] for i in [145, 159, 160, 161]]
            right_eye = [landmarks[i] for i in [374, 386, 387, 388]]

            # Draw circles on the eye landmarks
            for eye in [left_eye, right_eye]:
                for point in eye:
                    x = int(point.x * frame_w)  # Scale x-coordinate to frame width
                    y = int(point.y * frame_h)  # Scale y-coordinate to frame height
                    cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)  # Draw a green circle at each landmark

            # Check if both eyes are detected
            if left_eye and right_eye:
                eyes_detected = True
                # Display a message for eye detection
                cv2.putText(frame, "Eyes Detected", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

                # Perform cursor movement if cursor control is enabled
                if enable_cursor:
                    # Map the gaze coordinates to screen dimensions
                    screen_x = screen_w * right_eye[0].x * cursor_speed
                    screen_y = screen_h * right_eye[0].y * cursor_speed
                    pyautogui.moveTo(screen_x, screen_y)  # Move the cursor to the calculated position

                # Blink detection for left and right mouse clicks
                # Calculate the vertical aspect ratio of the eyes
                left_eye_aspect = abs(left_eye[1].y - left_eye[3].y)
                right_eye_aspect = abs(right_eye[1].y - right_eye[3].y)
                if left_eye_aspect < 0.004 and right_eye_aspect < 0.004:  # If both eyes are closed
                    blink_counter += 1  # Increment blink counter
                    if blink_counter == blink_threshold:  # If blink threshold is met
                        pyautogui.rightClick()  # Perform a right-click
                        pyautogui.sleep(1)  # Add a delay to prevent repeated clicks
                        blink_counter = 0  # Reset blink counter
                    else:
                        pyautogui.click()  # Perform a left-click
                        pyautogui.sleep(1)  # Add a delay
                else:
                    blink_counter = 0  # Reset blink counter if eyes are open
            else:
                # Display a message if face is detected but eyes are not
                cv2.putText(frame, "Face detected but Eyes Not Detected", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            # Display a message if no face is detected
            cv2.putText(frame, "Face Not Detected", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display the video feed with overlays
        cv2.imshow('Eye Controlled Mouse', frame)

    # Delay to process frames and check for 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows
listener.stop()  # Stop the keyboard listener when the program ends
