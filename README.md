# StarkSPY

![StarkSPY Logo](/images/logo.png)

StarkSPY is a **Linux** bounding box marking tool and integrates into surveillance application.
There are two programs consist of marking tool and the main program with using object detection algorithm. 
You can create more actions, when object attempts your marked bounding area. (e.g. print texts, counters, change status, etc.)

It is written in Python and uses OpenCV for its graphical interface.

The created box positions are according to OpenCV showup window. 
It will be saved in plain text file.Then it will be used again in the main program.

## Usages
`cd StarkSPY/\n`
* **rectangle marking:** `python3 --rectangle`
  * **circle marking:** `python3 --circle`

### Instruction manual
#### Mouse control for rectangle marking
Action | Description | 
--- | --- |
Left Click | Begin upper left point of box
Left Click Again | Draw bottom right point of box

#### Mouse control for circle marking
Action | Description | 
--- | --- |
Left Click | Begin center point of circle
Left Click Again | Draw point on the circumference of circle

#### Keyboard Shortcuts
Shortcut | Description | 
--- | --- |
<kbd>s</kbd>| save old boxes and begin new box |
<kbd>r</kbd>| reset all boxes (clear) |
<kbd>q</kbd>| save all then exit program |

#### Special Credits
  Thanks to Adrian Rosebrock, for writing many great articles some of my object detection codes are related to 
  https://www.pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/
