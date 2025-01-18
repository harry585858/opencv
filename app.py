import cv2
import numpy as np

point_list = []
color = (255, 0, 0)

def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        point_list.append((x, y))
    
    for point in point_list:
        cv2.circle(img, point, 10, color, 5)
    
    if len(point_list) == 4:
        do_result(point_list)
    cv2.imshow('img', img)

def do_result(point_list):
    height, width, rgb = img.shape 
    
    #시계방향으로 점 4개 입력
    before = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
    after = np.float32(point_list)
    
    #  transform matrix
    matrix = cv2.getPerspectiveTransform(after, before)
    
    #  perspective warp
    result = cv2.warpPerspective(img, matrix, (width, height))
    
    # 출력
    cv2.imshow('result', result) 

img = cv2.imread('cat.jpg')
cv2.namedWindow('img')
mode = int(input('1:transform, 2:binary : '))
if mode == 1:
    cv2.setMouseCallback('img', mouse_handler)
elif mode == 2:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, int(input('criteria : ')), 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
