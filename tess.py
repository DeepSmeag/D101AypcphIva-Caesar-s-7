from PIL import Image
# import numpy as np
import pytesseract
import cv2
# from matplotlib import pyplot as plt


def ImgToTxt(img_path):
    imgsrc = img_path
    img = cv2.imread(imgsrc, 0)
    # plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
    # plt.show()
    # cv2.imshow('image', img)

    im_threshold = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow('img', im_threshold)
    imgdest = 'ImgOCR\\ActualCaptchaThresh.png'
    cv2.imwrite(imgdest, im_threshold)
    return(pytesseract.image_to_string(Image.open(imgdest)))
    # cv2.waitKey(0)
    # cv2.imwrite('CaptchaGray.png', img)
