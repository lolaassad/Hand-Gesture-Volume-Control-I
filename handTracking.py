import cv2
import mediapipe as mp


class handTracker():
    def __init__(self, mode=False, maxHands=False, detectionCon=0.5, modelComplexity=1, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.deteionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands(self.mode, self.maxHands, self.modelComplex, self.deteionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    # method to track hands in input image. locates hads and processes image via RGB conversion
    def handsFinder(self, image, draw=True):
        imageRGB = cv2.cvtCOlor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:  # off script, should be if draw
                    self.results.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image

    # creating a method to find x and y coordinates of each hand point
    def positionFinder(self, image, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            Hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(Hand.landmark):  # enumerate adds a counter element to a for loop
                h, w, c = image.shape
                cx = int(lm.x * w)  # using width and height respectively to get x and y coords
                cy = int(lm.x * h)
                lmList.append([id, cx, cy])
            if draw:
                cv2.circle(image, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lmList

    def main():
        cap = cv2.VideoCapture(0)
        tracker = handTracker()

        while True:
            success, image = cap.read()
            image = tracker.handsFinder(image)
            lmList = tracker.positionFinder(image)

            if len(lmList) != 0:
                print(lmList[4])

            cv2.imshow("Video", image)
            cv2.waitKey(1)
            
#source: 
