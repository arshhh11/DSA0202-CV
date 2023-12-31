import cv2

# Load the image
img = cv2.imread('C:/Users/arsh/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg', 0)

# Apply Canny edge detection
edges = cv2.Canny(img, 100, 200)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
