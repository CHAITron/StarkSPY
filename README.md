# StarkSPY

StarkSPY is a **Linux** bounding box marking tool and integrates into surveillance application.
You can create actions, when object attempts your marked bounding area. (e.g. print texts, counters, change status, etc.)

It is written in Python and uses OpenCV for its graphical interface.

The created box positions are according to OpenCV showup window. 
It will be saved in plain text file.Then it will be used again in the main program.

## Usages
'cd StarkSPY/'
'python3 --rectangle' (rectangle marking)
'python3 --circle' (circle marking)

### Instruction manual
#### Mouse control
Action | Description | 
--- | --- |
Left Click | Begin upper left point of box
Left Click Again | Draw bottom right point of box
#### Keyboard Shortcuts
Shortcut | Description | 
--- | --- |
<kbd>  s</kbd> | save old boxes and begin new box |
<kbd>  r</kbd> | reset all boxes (clear) |
<kbd>  q</kbd> | save all then exit program |
