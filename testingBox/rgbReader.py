import cv2


# img = cv2.imread('./ui/bg.png')
# cv2.imshow('RGB Reader',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# aa=img[0,0] #bgr
# print(aa)

#===============================
img=cv2.imread('./demo.png')
r,c,no_use = img.shape

print(r,c)