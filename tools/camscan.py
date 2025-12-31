from ultralytics import YOLO
import cv2
def new_win():
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cv2.namedWindow("Hoshang Vision 👁️", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("no frame")
            break

        results = model(frame, conf=0.5, verbose=False)
        frame = results[0].plot()

        cv2.imshow("Hoshang Vision 👁️", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
