import cv2
import math
import argparse

shape = 'rectangle'
ap = argparse.ArgumentParser(description='....StarkSPY_2019....')
ap.add_argument("-s", "--shape", help="bounding shapes: rectangle, circle(default=rectangle)")
args = vars(ap.parse_args())
if not (args["shape"] is None):
    shape = str(args["shape"])

mouseX = mouseY = first_pressX = first_pressY = radius = 0
first = True
cap = cv2.VideoCapture(0)
width, height = int(cap.get(3)), int(cap.get(4))
count = 0
arraybox = []
name = ''


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return int(dist)


def draw_circle(event, x, y, flags, param):
    global mouseX, mouseY, first, first_pressX, first_pressY
    if first and (event == cv2.EVENT_LBUTTONDOWN):
        first_pressX, first_pressY = int(x), int(y)
        mouseX, mouseY = int(x), int(y)
        first = False
    elif (not first) and (event == cv2.EVENT_LBUTTONDOWN):
        mouseX, mouseY = int(x), int(y)


while cap.isOpened():
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    ret, image = cap.read()
    if ret:
        cv2.putText(image, '| Press \'r\' to reset |', (20, int(height - 15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (25, 25, 255), 2, cv2.LINE_AA)
        cv2.putText(image, '| Press \'s\' to save |', (220, int(height - 15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (25, 60, 255), 2, cv2.LINE_AA)
        cv2.putText(image, '| Press \'q\' to exit |', (420, int(height-15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (25, 90, 255), 2, cv2.LINE_AA)
        if shape == 'rectangle':
            cv2.rectangle(image, (first_pressX, first_pressY), (mouseX, mouseY), (255, 135, 0), 2, cv2.LINE_AA)
            if count > 0:
                for box in arraybox:
                    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (255, 135, 0), 2, cv2.LINE_AA)
        else:
            radius = calculateDistance(first_pressX, first_pressY, mouseX, mouseY)
            cv2.circle(image, (first_pressX, first_pressY), radius, (196, 213, 0), 2)
            if count > 0:
                for box in arraybox:
                    cv2.circle(image, (box[0], box[1]), box[2], (193, 213, 0), 2, cv2.LINE_AA)

        cv2.imshow('image', image)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            if count > 0:
                name = input("Choose Your Filename: ")
                with open("./{}.txt".format(name), "w") as txt_file:
                    for line in arraybox:
                        txt_file.write(" ".join(str(line)) + "\n")
            print('Exit Program....')
            break

        if k == ord('r'):
            print('All Boxes are cleared!')
            first_pressX = first_pressY = mouseX = mouseY = count = radius = 0
            first = True
            arraybox = []

        if k == ord('s'):
            if shape == 'rectangle':
                arraybox.append((first_pressX, first_pressY, mouseX, mouseY))
            else:
                arraybox.append((first_pressX, first_pressY, radius))
            count += 1
            first_pressX = first_pressY = mouseX = mouseY = radius = 0
            first = True
            print('All {} Boxes are saved!'.format(count))

cv2.destroyAllWindows()
