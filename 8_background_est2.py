import cv2 

stream = cv2.VideoCapture("assets/cyclists.mp4")

if not stream.isOpened : 
    print("No stream")
    exit()

# Increasing history → Makes the model less reactive to sudden changes.
# Decreasing history → Makes it adapt quickly but may misclassify background as foreground.
# Increasing varThreshold → Makes detection stricter, 
                            # ignoring small movements.
# Decreasing varThreshold → Makes detection sensitive to small changes, 
                            # possibly increasing false positives.
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500,
                                                   varThreshold=200,
                                                   detectShadows= True)

while True :
    ret , frame = stream.read()
    if not ret :
        print("No more stream")
        break
    #apply bg_subtractor
    fg_mask = bg_subtractor.apply(frame)
 
    cv2.imshow("foregroung mask" , fg_mask)
    if cv2.waitKey(1) == ord('q'):
        break


stream.release()
cv2.destroyAllWindows()