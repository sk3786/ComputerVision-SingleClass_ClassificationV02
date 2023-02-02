import cv2 as cv
import os

cam = cv.VideoCapture(0)


def video():


    # adjusting Size of Window
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)  # for height
    cam.set(cv.CAP_PROP_FRAME_WIDTH, 480)  # for width

    # adjusting the FPS rate
    cam.set(cv.CAP_PROP_FPS, 30)
    currentframe = 0

    # os.chdir('/home/shoaib/Codes/Deep_Learning & ML/Deep Learning/Projects/P1_Custom Real-time Object Detection/dataset')
    while True:

        ignore, frame = cam.read()


        cv.imshow('Window-01', frame)


        name = 'Frame(' + str(currentframe) + ').jpg'
        cv.imwrite(name, frame)
        currentframe += 1

        if cv.waitKey(1) & 0xff == ord('q'):
            break

cv.destroyAllWindows()

video()