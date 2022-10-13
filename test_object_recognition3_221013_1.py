import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
imgs = ['a.jpeg']  # batch of images

results = model(imgs)

results.save()