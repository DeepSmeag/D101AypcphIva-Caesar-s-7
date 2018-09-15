import cv2
import numpy as np


def ProcessImage(img_path):
    img = cv2.imread(img_path)
    imgToArr = np.asarray(img)
    # pixelsTxtFile = open("imgArr2changed.txt", 'w')
    pixelsList = imgToArr.tolist()
    for row in range(0, 50):
        for pixel in range(0, 230):
            if(pixelsList[row-1][pixel][0] < 30 and pixelsList[row-1][pixel][1] < 30
               and pixelsList[row-1][pixel][2] < 30):
                if(pixelsList[row][pixel][1] > 20 and pixelsList[row][pixel][2] > 20 and
                   pixelsList[row][pixel][0] < 100):
                    pixelsList[row][pixel] = [0, 0, 0]
            # print(str(pixelsList[row][pixel][1]) + " " + str(pixelsList[row][pixel][2]))
        # pixelsTxtFile.write(str(pixelsList[row])+', ')
        # pixelsTxtFile.write('\n')
    imgToArr = np.array(pixelsList)
    cv2.imwrite('ImgOCR\\ActualCaptchaEdit.png', imgToArr)
