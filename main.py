import cv2
import mediapipe as mp
import applescript
import osascript
import os


cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    cv2.circle(image, (cx, cy), 25, (127, 0, 255), cv2.FILLED)
                if id == 8:
                    cv2.circle(image, (cx, cy), 25, (127, 0, 255), cv2.FILLED)
                    flippedvolume = int(cy/100)
                    flippedvolume.__floor__
                    volume = 5
                    if flippedvolume == 1:
                        volume = 10
                    elif flippedvolume == 2:
                        volume = 9
                    elif flippedvolume == 3:
                        volume = 8
                    elif flippedvolume == 4:
                        volume = 7
                    elif flippedvolume == 5:
                        volume = 6
                    elif flippedvolume == 6:
                        volume = 5
                    elif flippedvolume == 7:
                        volume = 4
                    elif flippedvolume == 8:
                        volume = 3
                    elif flippedvolume == 9:
                        volume = 2
                    elif flippedvolume == 10:
                        volume = 1
                    #volume needs to round to nearest int between 1 and 10
                    command  = 'osascript -e "Set Volume {} "'.format(volume)
                    os.system(command)
                    print("Volume set to: ", volume)
                    #print("cx: " , cx)
                    #print("cy: " , cy)

                
                

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
    
    
    cv2.imshow("Output", cv2.flip(image, 1))
    cv2.waitKey(1)
    
    