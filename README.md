# StarkSPY
![Parking Application](/images/carpark.gif) <img src="/images/logo.png" width="220"/> 

StarkSPY is a **Linux** bounding box marking tool and video surveillance based on OpenCV library for checking availability of target object in real time.
There are two programs consist of marking tool(**GenBOX.py**), which allow you to create bounding area, and the main program(**SpyCAM.py**) with using object detection algorithm. 
Furthermore, You can program more actions, when object attempts your marked bounding area. (e.g. print texts, counters, change status, etc.)

It is written in Python3 and uses OpenCV for its graphical interface.

MobileNet-SSD is convolution neural networks model used to perform object detection. It is trained with PASCAL VOC (Visual Object Classes) dataset, so there are 21 classes to choose including: 
"background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor".

The created box positions are according to OpenCV showup window. 
It will be saved in plain text file.Then it will be used again in the main program.

## Usages
`cd StarkSPY/`
1. You need to draw bounding area first
* **rectangle marking:** `python3 GenBOX -s rectangle`
  * **circle marking:** `python3 GenBOX -s circle`
2. Use your marked areas in real-time capturing
    * `python3 SpyCAM`
  

### Instruction manual
<img src="/images/rectangle.gif" width="425"/><img src="/images/circle.gif" width="425"/>
#### Mouse control for rectangle marking
Action | Description | 
--- | --- |
First Left Click | Mark upper left point of box
Left Click Again | Adjust bottom right point of box

#### Mouse control for circle marking
Action | Description | 
--- | --- |
First Left Click | Mark center point of circle
Left Click Again | Adjust the circumference of circle

#### Keyboard Shortcuts
Shortcut | Description | 
--- | --- |
<kbd>s</kbd>| save drawed boxes and begin new box |
<kbd>r</kbd>| reset all boxes (clear all) |
<kbd>q</kbd>| save all then exit program |

## Full Tutorial

[![Tutorial Video](/images/tutorial.png)](https://youtu.be/EgN4qgl30dA)
[https://youtu.be/EgN4qgl30dA](https://youtu.be/EgN4qgl30dA)
