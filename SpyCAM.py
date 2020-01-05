# import the necessary packages
import argparse
import numpy as np
import cv2

# ____________________________________________   ARGUMENTS   ___________________________________________________

obj, threshold, before_detect, after_detect = 'bottle', 0.2, 'AVAILABLE', 'OCCUPIED'
ap = argparse.ArgumentParser(description='....StarkSPY_2019....')
ap.add_argument("-o", "--obj", help="choose your obj you want to detect from 21 classes (Default='car')")
ap.add_argument("-t", "--threshold", help="choose your threshold for obj detection (Default=0.2)")
ap.add_argument("-b", "--before", help="choose text to display when no obj is detected (Default='AVAILABLE')")
ap.add_argument("-a", "--after", help="choose text to display after found obj (Default='OCCUPIED')")
args = vars(ap.parse_args())
if not (args["obj"] is None):
    obj = str(args["obj"])
if not (args["threshold"] is None):
    threshold = float(args["threshold"])
if not (args["before"] is None):
    before_detect = str(args["before"])
if not (args["after"] is None):
    after_detect = str(args["after"])

# ____________________________________________   GLOBAL PARAMETERS   ___________________________________________________

prototxt = './MobileNetSSD/MobileNetSSD.prototxt.txt'
caffemodel = './MobileNetSSD/MobileNetSSD.caffemodel'
centerX = 0
centerY = 0
active_box = []

# There are 21 classes for you to choose
classes = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow",
           "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

# load deployed SSD network model
net = cv2.dnn.readNetFromCaffe(prototxt, caffemodel)
cap = cv2.VideoCapture(0)
index = 0


# ________________________________________      DEFINE FUNCTIONS        ________________________________________________

def get_boxes(filename):
    data = [line[2:-1].rstrip(' )\n').split(' ,   ') for line in open("./{}.txt".format(filename), "r")]
    center = []
    if len(data[0]) == 4:
        _type = 'rectangle'
        for boxes in range(len(data)):
            for element in range(4):
                data[boxes][element] = data[boxes][element].replace(" ", "")
                data[boxes][element] = int(data[boxes][element])
        for boxes in range(len(data)):
            calculate_center = int((int(data[boxes][0])+int(data[boxes][2]))/2), \
                               int((int(data[boxes][1])+int(data[boxes][3]))/2)
            center.append(calculate_center)
    if len(data[0]) == 3:
        _type = 'circle'
        for boxes in range(len(data)):
            for element in range(3):
                data[boxes][element] = data[boxes][element].replace(" ", "")
                data[boxes][element] = int(data[boxes][element])
        for boxes in range(len(data)):
            calculate_center = int(data[boxes][0]), int(data[boxes][1])
            center.append(calculate_center)
    return data, center, _type


def resize(img, width):
    (_height, _width) = img.shape[:2]
    ratio = width / float(_width)
    dim = (width, int(_height * ratio))
    resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized_img


def show_boxes(image, upper_left, bottom_right, color):
    cv2.rectangle(image, upper_left, bottom_right, color, 2, cv2.LINE_AA)


def show_circle(image, center, radius, color):
    cv2.circle(image, center, radius, color, 2, cv2.LINE_AA)


def put_text(image, text, position, color):
    cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2, cv2.LINE_AA)

def more_action():
	#program more actions to perform when object is detected
	print("Detected!")


# ____________________________________________      MAIN LOOP        ___________________________________________________

name = input("Choose Your Filename: ")
box_array, center_array, area_type = get_boxes(name)
while cap.isOpened():
    # grab the frame and limit to 400 pixels
    ret, frame = cap.read()
    if ret:
        #frame = resize(frame, 400)

        # grab the frame dimensions and convert it to a blob
        (h, w) = frame.shape[:2]
        frame_clone = frame
        blob = cv2.dnn.blobFromImage(cv2.resize(frame_clone, (300, 300)), 0.007843, (300, 300), 127.5)

        # set to network the input blob
        net.setInput(blob)
        detections = net.forward()

        # detection loop
        for i in np.arange(0, detections.shape[2]):
            # extract the confidence associated with the prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by ensuring the confidence is greater than the minimum threshold
            if confidence > threshold:
                # extract the index of the class label from the `detections`
                index = int(detections[0, 0, i, 1])
                if classes[index] == obj:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    y = startY - 15 if startY - 15 > 15 else startY + 15
                    centerX = int(startX + ((endX - startX) / 2))
                    centerY = int(startY + ((endY - startY) / 2))

        for box_center in center_array:
            if (centerX-30 < box_center[0] < centerX+30) and (centerY-30 < box_center[1] < centerY+30):
                active_box.append(center_array.index(box_center))
        if area_type == 'rectangle':
            for each_box in range(len(box_array)):
                if each_box in active_box:
                    show_boxes(frame, (box_array[each_box][0], box_array[each_box][1]),
                               (box_array[each_box][2], box_array[each_box][3]), (0, 90, 255))
                    put_text(frame, after_detect, (box_array[each_box][0], int(box_array[each_box][1])-5), (0, 90, 255))
                    #more_action()
                else:
                    show_boxes(frame, (box_array[each_box][0], box_array[each_box][1]),
                               (box_array[each_box][2], box_array[each_box][3]), (255, 135, 0))
                    put_text(frame, before_detect, (box_array[each_box][0], int(box_array[each_box][1]) - 5),
                             (255, 135, 0))
        elif area_type == 'circle':
            for each_box in range(len(box_array)):
                if each_box in active_box:
                    show_circle(frame, (box_array[each_box][0], box_array[each_box][1]),
                                box_array[each_box][2], (113, 81, 255))
                    put_text(frame, after_detect, (box_array[each_box][0], int(box_array[each_box][1])-5),
                             (113, 81, 255))
                    #more_action()
                else:
                    show_circle(frame, (box_array[each_box][0], box_array[each_box][1]),
                                box_array[each_box][2], (193, 213, 0))
                    put_text(frame, before_detect, (box_array[each_box][0], int(box_array[each_box][1]) - 5),
                             (193, 213, 0))

        cv2.imshow('frame', frame)
        active_box = []
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
