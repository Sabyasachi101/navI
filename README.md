# navI — Smart Wearable Navigation for the Visually Impaired

> A low-cost, AI-powered wearable assistive system combining real-time object detection, OCR, fall detection, and GPS emergency alerting for visually impaired individuals.

---

## 👥 Team Members

| Name | Roll No | Responsibility |
|------|---------|----------------|
| Sabyasachi | 102303458 | Computer vision model development & AI integration |
| Ramansh | 102303447 | Hardware integration, camera setup & fall detection |
| Aditya Garg | 102303516 | IoT communication & GPS emergency alerts |
| Saksham Jaswal | 102303547 | OCR module, audio output & system integration |

**Mentor:** Dr. Komal Bharti  
**Co-Mentor:** Dr. Vaishali Kansal

---

## 📌 Project Overview

**navI** is a wearable smart glasses prototype that provides real-time situational awareness to visually impaired persons (VIPs). The system integrates:

- 🎯 **Real-time object detection** using FOMO / MobileNet on ESP32-S3 Sense
- 📖 **On-demand OCR** using Google Vision API or Tesseract to read signboards and labels
- 🚨 **Automated fall detection & SOS alerts** via MPU6050 IMU + NEO-6M GPS + Telegram Bot API
- 🔊 **Audio feedback** via MAX98357A I2S amplifier and speaker

Target budget: **₹6,000 – ₹7,000**

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Sensing Layer                        │
│   Camera Module  |  MPU6050 IMU  |  NEO-6M GPS Module   │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                  Intelligence Layer                      │
│     FOMO / MobileNet (TensorFlow Lite on ESP32-S3)      │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                  Connectivity Layer                      │
│     Google Vision API (OCR)  |  Telegram Bot / IFTTT    │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                  Interaction Layer                       │
│     MAX98357A I2S Amplifier + Speaker + Tactile Switch  │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Hardware Requirements

| Component | Purpose |
|-----------|---------|
| ESP32-S3 Sense | Main processor for image capture & AI inference |
| MPU6050 IMU Sensor | Fall detection via motion monitoring |
| NEO-6M GPS Module | Real-time geospatial coordinates for SOS alerts |
| MAX98357A I2S Amplifier | High-quality audio output |
| Micro SD Card | Local data storage |
| 8Ω Speaker | Auditory feedback to user |
| Rechargeable Battery | Portable power supply |

---

## 💻 Software Requirements

| Software | Purpose |
|----------|---------|
| Arduino IDE | Programming the ESP32-S3 microcontroller |
| TensorFlow Lite | Running optimized ML models on embedded hardware |
| Edge Impulse | Training and deploying AI models |
| FOMO / MobileNet | Lightweight models for real-time object detection |
| Google Vision API / Tesseract | OCR for text extraction from images |
| Telegram Bot API / IFTTT | Transmitting GPS-based SOS emergency alerts |

---

## 🚀 Getting Started (Development & Testing)

### Prerequisites
- Python 3.9+
- VS Code (recommended)
- Webcam (for local testing before ESP32-S3 hardware arrives)

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/navI.git
cd navI

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run Object Detection (Webcam / Local Testing)

```bash
python3 object_detection.py
```

> Press **Q** to quit the detection window.

### Run Object Detection (ESP32-CAM Stream)

Update the stream URL in `object_detection.py`:
```python
cap = cv2.VideoCapture("http://<ESP32-IP>/stream")
```

Then run:
```bash
python3 object_detection.py
```

---

## 📦 Project Modules

```
navI/
├── object_detection.py     # YOLOv8 real-time object detection
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Excludes .venv, model weights, etc.
```

---

## 🗺️ Project Execution Plan

| Iteration | Focus | Goal |
|-----------|-------|------|
| 1 | Hardware Prototyping | Stable power & sensor communication |
| 2 | Vision & AI Module | Object detection + OCR with low latency |
| 3 | Safety & IoT Integration | Automated SOS alerts on fall detection |
| 4 | Optimization & Deployment | Fully functional wearable prototype |

---

## 🎯 Project Outcomes

- ✅ Wearable smart glasses prototype (ESP32-S3 Sense)
- ✅ Real-time obstacle detection (vehicles, pedestrians, stairs)
- ✅ On-demand OCR for signboards and labels
- ✅ Automated fall detection + GPS SOS via Telegram
- ✅ High-fidelity audio feedback system
- ✅ Cost target: ₹6,000 – ₹7,000

---

## ⚠️ Limitations & Constraints

- ESP32-S3's limited CPU/RAM requires lightweight FOMO or MobileNet models
- OCR via cloud APIs introduces latency dependent on network stability
- Scope excludes indoor mapping, pathfinding, or turn-by-turn routing
- Night vision / infrared sensing is out of current scope

---

## 📄 License

This project is developed as part of a capstone submission. All rights reserved by the team.
