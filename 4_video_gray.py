import cv2

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No stream :(")
    exit()

width = int(stream.get(3))
height = int(stream.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("assets/4_stream_gray.avi",fourcc,
                         30.0, frameSize=(width,height))

while stream.isOpened() :
    ret , frame = stream.read()
    if not ret :
        print("No more stream :(")
        break
    
    frame = cv2.flip(frame,1) #1 to flip horizontally , 0 to flip vertically
    frame = cv2.resize(frame , (width,height))
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    output.write(cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR))
    cv2.imshow("WebCam!" , gray)

    # we have done waitKey(0) which means any key of our keyboard
    # org maps q to integer ie its corresponding ascii value
    if cv2.waitKey(1) == ord('q') : 
        break

stream.release()
#output.release()
cv2.destroyAllWindows()