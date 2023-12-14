from ultralytics import YOLO
model=YOLO('yolov8l-cls.pt')
model.train(data='/Users/krishiv/Downloads/Nail Disease datasets',epochs=20)

