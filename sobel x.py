import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/arsh/Downloads/wallpaperflare.com_wallpaper.jpg")

# Apply Sobel filter along the X-axis
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Convert the output to absolute values
sobelx = np.abs(sobelx)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Edge Detection (X-axis)', sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
