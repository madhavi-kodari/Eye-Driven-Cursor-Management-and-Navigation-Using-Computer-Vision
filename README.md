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
(You can include screenshots or a demo video here)

## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by **[Your Name]**

