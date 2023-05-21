import cv2
import time

def main(lane):

    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()
    img_name = "bike{}.png".format(lane)
    cv2.imwrite(img_name, frame)

    cam.release()

    cv2.destroyAllWindows()