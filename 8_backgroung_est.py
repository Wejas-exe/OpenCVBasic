import cv2
import numpy as np
stream = cv2.VideoCapture("assets/cyclists.mp4")

if not stream.isOpened():
    print("No stream :(")
    exit()

# cv2.CAP_PROP_FRAME_COUNT gives the total number of frames in the video.
num_frames = stream.get(cv2.CAP_PROP_FRAME_COUNT)
# 20 random numbers between 0-1 i.e like percentages 
frame_ids = np.random.uniform(size=20)*num_frames

frames = []
for fid in frame_ids :
    stream.set(cv2.CAP_PROP_POS_FRAMES , fid)
    ret , frame = stream.read()
    if not ret :
        print("something is wrong")
        exit()
    frames.append(frame)

median = np.median(frames , axis = 0).astype(np.uint8)
median = cv2.cvtColor(median , cv2.COLOR_BGR2GRAY)


fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))
output = cv2.VideoWriter("assets/8_no_background.mp4",cv2.VideoWriter_fourcc(*'MP4V'),
                         fps = fps , frameSize=(width,height))

stream.set(cv2.CAP_PROP_POS_FRAMES,0)
while(True) :
    ret , frame = stream.read()
    if not ret :
        print("No more stream :(")
        break

    #take out any pixel that is similar to our video frame 
    frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    dif_frame = cv2.absdiff(median, frame)
    #if the diff is > 100 then the pixel is set to (white)255 (foreground)
    # otherwise 0 (background)
    threshold , diff = cv2.threshold(dif_frame , 100 , 255 
                                     ,cv2.THRESH_BINARY)
    
    output.write(diff)
    cv2.imshow("Video!" , diff)
    cv2.waitKey(20)
    if cv2.waitKey(1) == ord('q') : 
        break

stream.release()
cv2.destroyAllWindows()