import cv2 as cv
import sys

img = cv.imread("practicas\imagenes\imagen-1.jpg")


cv.imshow("Imagen",img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png", img) 