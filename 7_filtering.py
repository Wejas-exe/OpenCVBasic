import cv2 
import numpy as np 

img = cv2.imread("assets/cat.webp")

#filter2D
blur_filter = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])
blur_filter = blur_filter/5
blur_filter_img = cv2.filter2D(img , ddepth=-1,kernel=blur_filter)

#BLUR 
# ksize has to be odd , thats how the maths work out 
# ksize is bacically the size of array we have defined above inthe blur_filter 
# its 3x3 there
blur_img = cv2.blur(img , ksize=(11,11))

# GAUSSIAN BLUR 
gaus_img = cv2.GaussianBlur(img , ksize=(11,11), sigmaX=30 ,sigmaY=300)

#SHARPEN
sharpen_filter = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
shapren_img = cv2.filter2D(img , -1 ,kernel=sharpen_filter)

#EDGE DETECTION // LAPLACIAN FUNCTION
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
gray_img = cv2.GaussianBlur(gray_img , ksize=(3,3),sigmaX=1,sigmaY=1)
edges = cv2.Laplacian(gray_img , -1)

# ANOTHER WAY TO DETECT EDGE
kernel2 = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])
edges_2 = cv2.filter2D(src=gray_img, ddepth=-1, kernel=kernel2)


cv2.imshow("Cat!",edges)
cv2.imshow("Cat2!" , edges_2)
cv2.waitKey(0)
cv2.destroyAllWindows()