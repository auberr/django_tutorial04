import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img = cv2.imread('a.jpeg')
results = model(img)
results.save()

result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6]=='person']

# opencv 로 이미지 읽기
tmp_img = cv2.imread('a.jpeg')
# opencv 로 이미지 사이즈 확인
print(tmp_img.shape)
# height, width, channel 에서 따로 분리
h,w,c = tmp_img.shape
# height, width 따로 출력
# 2. opencv 로 이미지를 읽고 이미지의 가로, 세로가 각 몇 pixel 인지 구하세요
#   a. (세로, 가로)
print(f"이미지의 세로는 {h} px 이고 이미지의 가로는 {w}px 입니다.")

# 3.이미지에서 사람을 찾아 하얀색으로 네모를 그려서 result1.png 로 저장하세요
cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), (255,255,255))
cv2.imwrite('result1.png', tmp_img)


'''테스트 코드'''
# for (x,y,z) in result:
#     cropped = tmp_img[int(result[x][y]):int(result[x][y]), int(result[x][y]):int(result[x][y])]
#     cv2.imwrite('people{z}.png', cropped)



# cropped = tmp_img[int(result[0][1]):int(result[0][3]), int(result[0][0]):int(result[0][2])]
# print(cropped.shape)
# cv2.imwrite('result4.png', cropped)
# cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), (255,255,255))
# cv2.imwrite('result5.png', tmp_img)





# 4. 이미지에서 사람들을 잘라 people1.png, people2.png… 로 저장하세요


