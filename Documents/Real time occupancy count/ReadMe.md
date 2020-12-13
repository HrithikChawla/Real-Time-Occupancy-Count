**Occupancy Count**

first edition

**Overview**

Given a set up webcam, the program can open the camera and display the real-time Human face Occupancy Count on the screen.

**Prerequisites**

Python3

**How to run**

python Occupancy_Count.py

--------------------------------------------
**Open Source Model**

Python Library: *Opencv* with *haar cascade* algorithm
> OpenCV:  https://pypi.org/project/opencv-python/

> haar cascade https://github.com/opencv/opencv/tree/master/data/haarcascades

Need to download *haarcascade_frontalface_default.xml* from
>  https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

--------------------------------------
**Design**

The project is written in python file.


*  Initialize the camera that is already set properly.

*  Detect human faces with the help of “Haar Cascade” algorithm.


* Count the number of human faces appear in the real-time webcam.


*   Display the number on the screen.

*  Enable user to close the camera by pressing “ESC”
----------------------------------------
**Important file**

"Occupancy_count": is the main code




------------------------------------------
**Report**


The first edition is doing OK when the light is sufficient and people are at a normal distance from the camera.



-----------------------------------------
**Need Update**

The project is only the first edition. I will keep update.
