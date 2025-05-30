# NeuroGest 🧠🖐️

**NeuroGest** is a computer vision-based hand-tracking application designed to control PowerPoint slide presentations using intuitive hand gestures. The system uses a webcam and detects specific hand movements to seamlessly navigate slides, enhancing touchless interaction during lectures, demos, or conferences.

---

## 🚀 Features

- 👆 **Gesture-Based Slide Control**  
  Navigate slides using hand gestures (e.g., next/previous slide with specific finger combinations).

- 🧠 **Real-Time Hand Tracking**  
  Uses machine learning and computer vision to detect hand landmarks in real time.

- ✅ **Precision Control**  
  Ensures only the index finger is used to control the pointer and ignores other fingers to prevent accidental slide transitions.

- 🔐 **Accidental Prevention**  
  Prevents unintentional gestures by adding robust detection and transition logic.


---

## 🛠️ Tech Stack

- **Programming Language**: Python  
- **Libraries Used**:
  - `cv2` (OpenCV) – for video capture and image processing
  - `mediapipe` – for hand gesture recognition
  - `numpy` – for numerical operations
---

## 🧑‍💻 How It Works

1. Run the program.
2. Raise your hand within the webcam frame.
3. Use the index finger to control the pointer.
4. Perform predefined gestures (e.g., swipe left/right) to move between slides.
5. The app filters out unwanted gestures and pinky/middle finger movement.

---

## 🖥️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/NeuroGest.git
cd NeuroGest
