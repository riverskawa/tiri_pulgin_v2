import numpy as np
import cv2
from matplotlib import pyplot as plt

img_path_1 = 'C:/Users/user/Documents/011_5mg_ml_1CC_004_output_gray_0/011_5mg_ml_1CC_004_output_gray_0/20220225105450585C_0.bmp'
img_path_2 = 'C:/Users/user/Documents/011_5mg_ml_1CC_004_output_gray_0/011_5mg_ml_1CC_004_output_gray_0/20220225105451360C_0.bmp'

sift = cv2.xfeatures2d.SIFT_create()

img1 = cv2.imread(img_path_1)
img2 = cv2.imread(img_path_2)

kp1, des1 = sift.detectAndCompute(img1,None)
print('pic one:'+str(len(kp1)))

kp2, des2 = sift.detectAndCompute(img2,None)
print('pic two:'+str(len(kp2)))

img3 = cv2.drawKeypoints(img1,kp1,img1,color=(255,0,255))
img4 = cv2.drawKeypoints(img2,kp2,img2,color=(255,0,255))

hmerge = np.hstack((img3,img4))
cv2.imshow('point',hmerge)
cv2.waitKey(0)

bf = cv2.BFMatcher()

matchs = bf.knnMatch(des1,des2,k=2)

good = []
for m,n in matchs:
    if m.distance <0.75*n.distance:
        good.append([m])

img5 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
cv2.imshow('BFmatchs',img5)
cv2.waitKey(0)
cv2.destroyAllWindows()