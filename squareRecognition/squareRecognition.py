# importing the module
import cv2
import numpy as np
# reading the video
source = cv2.VideoCapture(0)
  
# running the loop
while True:
  
    _, frame = source.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    blur = cv2.medianBlur(gray, 5)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

    thresh = cv2.threshold(frame, 160, 255, cv2.THRESH_BINARY_INV)[1]

    # extracting the frames
    ret, img = source.read()
      
    # converting to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    # displaying the video
    cv2.imshow("Live", gray)
    cv2.imshow("Live", thresh)
  
    # exiting the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
      
# closing the window
cv2.destroyAllWindows()
source.release()
