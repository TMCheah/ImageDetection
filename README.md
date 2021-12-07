# ImageDetection
Image Detection using cv2.goodFeaturesToTrack 
Base on my understanding by cracking the code how everything works, basically it captures the template's corners, and match with the corners captures in the test image through sliding window. When the corners matches certain threshold, it is then consider as found. In other words, the system do not know what is the object, it only knows the corner :)

### Template image used is a baby Yoda (template.jpg)
![Template](https://github.com/TMCheah/ImageDetection/blob/main/template.jpg)

### Output
![Output](https://github.com/TMCheah/ImageDetection/blob/main/object%20detection.png)
