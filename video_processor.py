import cv2

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Process each frame for anomaly detection
        # For example, apply some detection logic
    cap.release()
