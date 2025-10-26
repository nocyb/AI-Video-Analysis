import cv2
from ultralytics import YOLO
import os

input_video_path = input("Enter video name (e.g., video.mov or video.mp4): ").strip()

if not os.path.exists(input_video_path):
    print("❌ File not found.")
    exit()

output_format = input("Output format (mp4/mov) [default mp4]: ").strip().lower()
if output_format not in ["mp4", "mov"]:
    output_format = "mp4"

base_name, _ = os.path.splitext(input_video_path)
output_video_path = f"{base_name}_output.{output_format}"

model_path = "yolov8n.pt"
model = YOLO(model_path)

cap = cv2.VideoCapture(input_video_path)
if not cap.isOpened():
    print("❌ Unable to open the video.")
    exit()

fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*("mp4v" if output_format == "mp4" else "avc1"))
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

print(f"🔍 Starting detection on {input_video_path} ... (press 'q' to quit)")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("AI Object Detection", annotated_frame)
    out.write(annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"✅ Video saved as: {output_video_path}")