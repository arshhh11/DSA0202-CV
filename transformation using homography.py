import cv2
import numpy as np
 
if _name_ == '_main_' :
    im_src = cv2.imread("C:/Users/arsh/OneDrive/Pictures\Saved Pictures/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg")
    pts_src = np.array([[141, 131], [480, 159], [493, 630],[64, 601]])
    im_dst = cv2.imread("C:/Users/Raja/OneDrive/Pictures\Saved Pictures/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg")
    pts_dst = np.array([[318, 256],[534, 372],[316, 670],[73, 473]])
    h, status = cv2.findHomography(pts_src, pts_dst)
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Image", im_dst)
    cv2.imshow("Warped Source Image", im_out)
 
    cv2.waitKey(0)
