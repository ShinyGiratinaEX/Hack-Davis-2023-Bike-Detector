import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

def main():
    img = cv2.imread('bikepics/bike5.png')
        
    box, label, count = cv.detect_common_objects(img, confidence = 0.3)
    bikebox = [box[i] for i in range(len(box)) if label[i] == "bicycle"]
    bikelabel = [label[i] for i in range(len(label)) if label[i] == "bicycle"]
    bikecount = [count[i] for i in range(len(count)) if count[i] == "bicycle"]
    output = draw_bbox(img, bikebox, bikelabel, bikecount)

    output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(12,12))
    plt.imshow(output)
    plt.axis('off')
    plt.show()

    print("Number of objects in this image are " +str(len(label)))
    print("Number of bicycles in this image are " +str(len([bicycle for bicycle in label if bicycle == "bicycle"])))
    return len([bicycle for bicycle in label if bicycle == "bicycle"])