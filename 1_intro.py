import cv2

img = cv2.imread("assets/cat.webp",cv2.IMREAD_COLOR)
print(img.size)
print(img[260,450])

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(rgb_img[260,450])
# for i in range (img.shape[0]) :
#     for j in range (img.shape[1]) :
#         img[i,j] = max(254,img[i,j]*2)
cv2.imshow("CAT" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("assets/grey_cat.webp " , gray_img)