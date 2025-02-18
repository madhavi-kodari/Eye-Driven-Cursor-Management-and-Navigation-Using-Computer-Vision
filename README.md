# Eye-Driven-Cursor-Management-and-Navigation-Using-Computer-Vision
Mini-Project
## Overview
This project implements an eye-controlled cursor system using computer vision and machine learning techniques. It enables users to control the mouse cursor using eye movements detected via a webcam. This technology is particularly useful for accessibility applications, allowing individuals with motor impairments to interact with a computer hands-free.

## Features
- Real-time face and eye tracking using Mediapipe Face Mesh.
- Eye gaze-based cursor movement.
- Blink-based mouse clicks (left and right clicks).
- Global keyboard shortcuts to enable/disable cursor movement and webcam detection.

## Technologies Used
- **Python** - Main programming language.
- **OpenCV** - Used for video capture and image processing.
- **Mediapipe** - Used for face and eye landmark detection.
- **PyAutoGUI** - Used for cursor movement and mouse control.
- **Pynput** - Used for global keyboard event handling.

## Installation
### Prerequisites
Ensure you have Python installed on your system (Python 3.7 or higher recommended).

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/eye-driven-cursor.git
   cd eye-driven-cursor
   ```
2. Install the required dependencies:
   ```sh
   pip install opencv-python mediapipe pyautogui pynput
   ```
3. Run the program:
   ```sh
   python eye_cursor_control.py
   ```

## Usage
- The system will automatically detect your face and eyes via the webcam.
- Move your eyes to control the cursor.
- Blink to trigger left and right mouse clicks.
- Keyboard Shortcuts:
  - Press **'q'** to quit the program.
  - Press **'t'** to toggle cursor movement on/off.
  - Press **'w'** to toggle webcam detection on/off.

## Demo
![Screenshot 2024-12-31 114853](https://github.com/user-attachments/assets/32fbaacc-1896-4917-843e-e2466ac78261)
This image represent the face detection and eyes detection.
![Screenshot 2024-12-31 114928](https://github.com/user-attachments/assets/a925a7c0-42f7-4cbc-a961-4bfe8aa2f212)
Here we can see how the gesture points are marked on eyes clearly.
![Screenshot 2024-12-31 123322](https://github.com/user-attachments/assets/dc7b023e-bafd-413a-818a-fd115ebc492b)
it eye gesture to perform click.
![Screenshot 2024-12-31 120251](https://github.com/user-attachments/assets/3fec4d44-b88a-41c0-985a-949237be1dcb)
here we can see that the cursor pointing on the github repository.
![Screenshot 2024-12-31 120731](https://github.com/user-attachments/assets/e31bb637-a5f2-406b-8f9d-5be88e63d466)
based on the cursor pointing it performed click and open to the new page.
![Screenshot 2024-12-31 125841](https://github.com/user-attachments/assets/64bb743c-e741-4cdf-b4eb-7849625af772)
this image show the how the keyboard shortcuts performed.
## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by **K.Madhavi**

