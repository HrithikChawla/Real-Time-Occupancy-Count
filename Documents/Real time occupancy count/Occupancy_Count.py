import cv2

##test gitlab
# Initialize the cascade classifier for detecting faces
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
try:
    #face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    print('running the program. Please press "ESC" to terminate')
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # Initialize the camera (use bigger indices if you use multiple cameras)
    cap = cv2.VideoCapture(0)
    # Set the video resolution to half of the possible max resolution for better performance
    cap.set(3, 1920 / 2)
    cap.set(4, 1080 / 2)
    # Standard text that is displayed above recognized face
    exceptional_frames = 100

    while True:
        #print(exceptional_frames)
            #print("face detection program loading")

        count=0
            # Read frame from camera stream and convert it to greyscale
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect faces using cascade face detection
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        exceptional_frames=100
            # Loop through detected faces and set new face rectangle positions
        for (x, y, w, h) in faces:
            color = (0, 255, 0)
            startpoint = (x, y)
            endpoint = (x + w, y + h)
            exceptional_frames = 0
                # Draw face rectangle on image frame
            cv2.rectangle(img, startpoint, endpoint, color, 2)

            count=count+1
        #display the info on the screen
        cv2.putText(img,text="current occupancy is " + str(count), org=(50,50),fontFace=1,fontScale=3,thickness=3,color=(0,0,0))
            # Show image in cv2 window
        cv2.imshow("real-time Occupancy Count", img)
            # Break if input key equals "ESC"
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        exceptional_frames += 1
    cap.release()
    cv2.destroyAllWindows()
except Exception as error:
    print('Looks like there is something wrong. Please check your camera and rerun the program')
    print('The Error is: '+ str (error))


