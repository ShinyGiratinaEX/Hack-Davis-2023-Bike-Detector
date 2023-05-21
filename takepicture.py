import cv2
import time

def main():

    cam = cv2.VideoCapture(0)

    img_counter = 0

    ret, frame = cam.read()
    img_name = "bike{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)

    cam.release()

    cv2.destroyAllWindows()