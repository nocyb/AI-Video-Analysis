# 🎥 YOLO Video Object Detection

A simple Python script that applies **real‑time object detection** on a video file using [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) and **OpenCV**.  
The script automatically saves the processed video with bounding boxes and object confidences.

<p align="center">
  <img src="https://i.imgur.com/mLurTMJ.jpeg" width="700" alt="Preview of AI Video Analysis" />
</p>

---

## ✨ Features

- Detects common objects in any `.mp4` or `.mov` video using YOLOv8  
- Automatically saves output as `<filename>_output.mp4` or `.mov`  
- Lets the user pick the export format  
- Real‑time display window with bounding boxes  
- Works with any pretrained YOLOv8 model (`yolov8n.pt`, `yolov8s.pt`, etc.)

---

## 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/nocyb/AI-Video-Analysis.git
   cd AI-Video-Analysis
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv8 model** (optional - will auto-download on first run)
   ```bash
   # The script uses yolov8n.pt by default
   # It will be downloaded automatically when you first run the script
   ```

---

## 🚀 Usage

1. **Place your video file** in the project directory (supports `.mp4`, `.mov`, `.avi`, etc.)

2. **Run the script**
   ```bash
   python vid_analytics.py
   ```

3. **Follow the prompts**:
   - Enter your video filename (e.g., `my_video.mp4`)
   - Choose output format (`mp4` or `mov`, defaults to `mp4`)

4. **Watch the real-time detection** in the preview window
   - Press `q` to quit early or let it process the entire video

5. **Find your processed video** saved as `<filename>_output.<format>`

---

## 📋 Requirements

- Python 3.8+
- OpenCV (`opencv-python`)
- Ultralytics YOLO (`ultralytics`)
- YOLOv8 model file (`yolov8n.pt` - downloads automatically)

---

## 🎯 Example

```bash
$ python vid_analytics.py
Enter video name (e.g., video.mov or video.mp4): my_video.mp4
Output format (mp4/mov) [default mp4]: mp4
🔍 Starting detection on my_video.mp4 ... (press 'q' to quit)
✅ Video saved as: my_video_output.mp4
```

---

## 🔧 Configuration

- **Model**: Change `model_path` in `vid_analytics.py` to use different YOLO models:
  - `yolov8n.pt` (nano - fastest)
  - `yolov8s.pt` (small)
  - `yolov8m.pt` (medium)
  - `yolov8l.pt` (large)
  - `yolov8x.pt` (extra large - most accurate)

---

## 📄 License

This project is licensed under the MIT License. Feel free to modify, distribute, and use this code for your own projects!

---

## 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for the object detection model
- [OpenCV](https://opencv.org/) for video processing capabilities
