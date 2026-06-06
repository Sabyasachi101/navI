from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # auto-downloads on first run (~6MB)

cap = cv2.VideoCapture(0)  # 0 = laptop webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated = results[0].plot()  # draws boxes + labels

    cv2.imshow("YOLOv8 - Object Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # press Q to quit
        break

cap.release()
cv2.destroyAllWindows()