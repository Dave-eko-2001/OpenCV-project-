

import cv2



capture = cv2.VideoCapture(1)

face_haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



while True:

    _, image = capture.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BRG2GRAY)

    faces = face_haar_cascade.detectMultiScale(gray, 1.1, 4)



    for (x,y, w, h) in faces:

        cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 5)



        cv2.imshow("Video", image)

        k=cv2.waitkey(30) & 0xFF

        if k == 27:

            break



    cv2.release()
