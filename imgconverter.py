from PIL import Image
import numpy as np
import cv2
from statistics import mean


def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
    return newAr


def grayscale(img):
    i = Image.fromarray(img)
    iar = np.array(i)
    iar = threshold(iar)

    return iar


def pil2cv2(img):
    cv2Img = np.array(img)
    cv2Img = cv2Img[:, :, ::-1].copy()
    # convert the image back into uint8
    finImg = cv2.convertScaleAbs(cv2Img)

    return finImg
