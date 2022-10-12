import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

results = model(imgs)

print(results.xyxy[0], results.xyxy[0][0][0].item())  # img1 predictions (tensor)
print(results.pandas().xyxy[0])  # img1 predictions (pandas)

tmp_img = cv2.imread('zidane.jpg')
cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), (255,255,255))
cv2.imwrite('result.png', tmp_img)
