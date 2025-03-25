import cv2

img = cv2.imread("assets/cat.webp",cv2.IMREAD_COLOR)

#BORDER // img , top , bottom , left , right , borderType, value
img = cv2.copyMakeBorder(img , 10,10,10,10,borderType= cv2.BORDER_CONSTANT ,
                          value= (0,40,100))

#LINE  // img , point1 , point2 , color , thickness 
img = cv2.line(img , (50,50) , (300,300) , color=(0,0,100) , thickness=5)

#ARROW // img , point1 , point2 , color , thickness
img = cv2.arrowedLine(img , (50,80) , ( 360,30) , color =(100,0,0) , thickness = 5)

#CIRCLE // img , center  , radius , color, thickness 
img = cv2.circle(img ,(100,100) ,50,color=(0,100,0))

#ELLIPSE //img , center , axes , angle , startAngle , endAngle , color , thickness
img = cv2.ellipse(img , center=(45,80) , axes=(100,200) ,angle=45 , startAngle=0 ,
                   endAngle=360 , color =(0,200,200), thickness=5)

#RECTANGLE //img , point1 , point2 , color , thickness
img = cv2.rectangle(img , (50,50) , (120,10) , (150,150,150) , 5)

#TEXT //img , text , origin, fontFace , fontScale , color , thickness
img = cv2.putText(img ,"ELLA <3" , org=(150,200) ,
                  fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=2,
                  color=(200,0,0),thickness=10)

cv2.imshow("Ella",img)
cv2.waitKey(0)
cv2.destroyAllWindows()