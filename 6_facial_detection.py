import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
                                       "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                      "haarcascade_smile.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                    "haarcascade_eye.xml")


def detect_features(frame) :
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    # parameters are : image , scale , min no. of neighbours 
    # you can also specify minSize and maxSize for the feature 
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    
    for(x,y,w,h) in faces :
        frame = cv2.rectangle(frame , (x,y) , (x+w,y+h) , 
                            color =(0,255,0) , thickness=5)
        face = frame[y:y+h,x:x+w]
        gray_face = gray[y:y+h,x:x+w]
        smiles = smile_cascade.detectMultiScale(gray_face,2.5,9)
        for(xp,yp,wp,hp) in smiles :
            face = cv2.rectangle(face, (xp,yp) ,(xp+wp,yp+hp) , 
                                  color = (255,0,0) , thickness = 5)
        eyes = eye_cascade.detectMultiScale(gray_face , 2.5 , 7)
        for(xp,yp,wp,hp ) in eyes :
            face = cv2.rectangle(face , (xp,yp) , (xp+wp , yp+hp) ,
                                  color =(0,0,255) , thickness = 7)

    return frame


stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No stream :(")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))
output = cv2.VideoWriter("assets/6_facial_detection.mp4",cv2.VideoWriter_fourcc(*'MP4V'),
                         fps = fps , frameSize=(width,height))

while(True) :
    ret , frame = stream.read()
    if not ret :
        print("No more stream :(")
        break

    frame = cv2.resize(frame , (width,height))
    frame = detect_features(frame)
    output.write(frame)
    cv2.imshow("WebCam!" , frame)

    if cv2.waitKey(1) == ord('q') : 
        break

stream.release()
cv2.destroyAllWindows()