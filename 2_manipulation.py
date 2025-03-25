import cv2
import numpy as np

img = cv2.imread("assets/cat.webp",cv2.IMREAD_COLOR)
print(img[0,0])

#RESIZE
img = cv2.resize(img , (400,800))
img = cv2.resize(img , (0,0) , fx=2 , fy=1)

#CROP 
#height , width = img.shape[0] , img.shape[1]
height , width = img.shape[:2]
img = img[int(height/3) : , 50:-50]

#ROTATE
img = cv2.rotate(img , cv2.ROTATE_180)
rotation_matrix = cv2.getRotationMatrix2D(center=(width/2,height/2) ,
                                           angle = 135 , scale =1.0)
rotated_img = cv2.warpAffine(img , rotation_matrix , (width,height))

#TRANSLATE
tx = width/5
ty = -height/5
translation_matrix = np.array([
    [1,0,tx],
    [0,1,ty]
])
translated_img = cv2.warpAffine(img , translation_matrix,(width,height))
cv2.imwrite("assets/cat_translated.webp",translated_img)
cv2.imshow("cat",translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()