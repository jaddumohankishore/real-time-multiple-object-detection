import tkinter as tk
from tkinter import filedialog, Text, Label, Button, Scrollbar
import cv2
import imutils
import time
import threading
from imutils.video import VideoStream
from ultralytics import YOLO

# ------------------ Globals ------------------
running = False
logged_objects = set()  # Track already logged objects
model = YOLO("yolov8n.pt")   # Lightweight YOLOv8 model
FIXED_WIDTH, FIXED_HEIGHT = 800, 600
CONF_THRESHOLD = 0.55  # Only detect objects with confidence >= 55%

# ------------------ Detection Helpers ------------------
def count_objects(results):
    counts = {}
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls)
            conf = float(box.conf)
            if conf < CONF_THRESHOLD:  # Ignore low-confidence detections
                continue
            label = model.names[cls_id]
            counts[label] = counts.get(label, 0) + 1
    return counts

def process_frame(frame):
    global logged_objects
    results = model(frame, verbose=False)
    annotated = results[0].plot()
    counts = count_objects(results)

    # Append only objects not yet logged
    new_objects_for_log = set(counts.keys()) - logged_objects
    for obj in new_objects_for_log:
        text.insert(tk.END, f"{obj}: {counts[obj]}\n")
    text.see(tk.END)

    logged_objects.update(new_objects_for_log)
    return annotated, counts

# ------------------ Video ------------------
def start_video(source, mode="webcam"):
    global running
    running = True
    text.insert(tk.END, f"{mode.upper()} DETECTION STARTED...\n")
    text.see(tk.END)

    vs = VideoStream(src=source).start() if mode == "webcam" else cv2.VideoCapture(source)
    time.sleep(1.0)

    while running:
        frame = vs.read() if mode == "webcam" else vs.read()[1]
        if frame is None:
            break

        frame = imutils.resize(frame, width=700)
        annotated, counts = process_frame(frame)
        annotated = cv2.resize(annotated, (FIXED_WIDTH, FIXED_HEIGHT))

        cv2.imshow("YOLOv8 Detector", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        if not running:
            break

    vs.stop() if mode == "webcam" else vs.release()
    cv2.destroyAllWindows()
    running = False

# ------------------ Stop Detection ------------------
def stop_video():
    global running
    running = False
    text.insert(tk.END, "\nDetection stopped.\n")
    text.see(tk.END)

def run_in_thread(func, *args):
    thread = threading.Thread(target=func, args=args, daemon=True)
    thread.start()

# ------------------ Image ------------------
def detect_image():
    global logged_objects
    filename = filedialog.askopenfilename(initialdir="images")
    if not filename:
        return

    text.insert(tk.END, f"Image loaded: {filename}\n")
    text.see(tk.END)

    img = cv2.imread(filename)
    results = model(img, verbose=False)
    annotated = results[0].plot()
    annotated = cv2.resize(annotated, (FIXED_WIDTH, FIXED_HEIGHT))
    counts = count_objects(results)

    new_objects_for_log = set(counts.keys()) - logged_objects
    for obj in new_objects_for_log:
        text.insert(tk.END, f"{obj}: {counts[obj]}\n")
    text.see(tk.END)

    logged_objects.update(new_objects_for_log)

    cv2.imshow("YOLOv8 Detector", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ------------------ GUI ------------------
main = tk.Tk()
main.title("YOLOv8 Object Detection for Visually Impaired")
main.geometry("1300x800")
main.config(bg="snow3")

Label(main, text="Object Detection Framework (YOLOv8)",
      bg="green", fg="white", font=("times", 20, "bold"),
      height=2, width=60).place(x=0, y=5)

font_btn = ("times", 14, "bold")
Button(main, text="Browse System Video",
       command=lambda: run_in_thread(start_video, filedialog.askopenfilename(initialdir="videos"), "video"),
       font=font_btn).place(x=50, y=100)
Button(main, text="Browse Image", command=detect_image, font=font_btn).place(x=300, y=100)
Button(main, text="Start Webcam", command=lambda: run_in_thread(start_video, 0, "webcam"), font=font_btn).place(x=500, y=100)
Button(main, text="Start External Cam", command=lambda: run_in_thread(start_video, 1, "webcam"), font=font_btn).place(x=700, y=100)
Button(main, text="Stop Detection", command=stop_video, font=font_btn, bg="red", fg="white").place(x=950, y=100)

# Text widget with scrollbar
text_frame = tk.Frame(main)
text_frame.place(x=10, y=180)
scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = Text(text_frame, height=25, width=150, font=("times", 12, "bold"), yscrollcommand=scrollbar.set)
text.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=text.yview)

main.mainloop()
