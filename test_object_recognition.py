#pip install -qr https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt 

import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

results = model(imgs)

results.save()