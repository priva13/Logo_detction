# Thumbstack Logo Detection Using Python

## Modules used
- opencv
- tkinter
- numpy

## How it works

### Getting cascade.xml file
- Collectting various Positive Images of Logo
- Collectting various Negative Images of Logo
- Train it using opencv and get cascade.xml file (It is very computational process that can be take much time)

### Using tkinter for GUI
- Tkinter is an inbuild module in python
- Using tkinter I added two button on gui
- Added specific Function on each `command`
- First button is for Detect logo from system's image file
- Second button is for Detect logo in camera frame

### Using opencv and cascade.xml file for detection
For First Button
- On clicking first button then open cv2 will get the filepath using `filedialog` method is tkinter
- Using `imread` method it will open the image
- Using `cvtColor` to convert image to grayscale
- Using `thumbstack_cascade.detectMultiScale(gray,1.11,5)` it will detect the logo
- Using `for` loop It will draw the `rectangle` around the logo on image
- And finally I will show the Image using `imshow` method

For Second Button

- Starting a camera `frame` using opencv
- In the camera frame `while` loop It will do the same process as in first button
- In this loop it will detect and the logo and show on the frame rounded with blue rectangle

