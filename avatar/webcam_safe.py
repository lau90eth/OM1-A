import cv2

def safe_webcam_open():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam not found")
        return None
    return cap
