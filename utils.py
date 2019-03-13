import cv2 as cv
import numpy as np
import hashlib
import time


def createBlankImg(shape):
    height, width = shape
    blankImg = np.zeros((height, width, 3), np.uint8)
    return blankImg


def genHash():
    m = hashlib.md5()
    m.update(str(time.time()).encode('utf-8'))
    return m.hexdigest()[0:10]


def getRange(shape, range, margin):
    x, y, w, h = range
    height, width = shape

    xs = x - margin
    xe = x + w + margin
    ys = y - margin
    ye = y + h + margin

    if xs < 0:
        xs = 0
    if ys < 0:
        ys = 0
    if xe > width:
        xe = width
    if ye > height:
        ye = height

    return (ys, ye, xs, xe)


def getClip(img, cnt, margin):
    ys, ye, xs, xe = getRange(img.shape[:2], cv.boundingRect(cnt), margin)
    return img[ys:ye, xs:xe]


def drawRects(img, cnts, margin):
    height, width = img.shape[:2]
    for c in cnts:
        range = cv.boundingRect(c)
        ys, ye, xs, xe = getRange((height, width), range, margin)
        img = cv.rectangle(img, (xs, ys), (xe, ye), (0, 255, 0), 2)


def findContours(img, area):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(gray, 127, 255, 0)[1]
    cnts = cv.findContours(thresh,
                           cv.RETR_EXTERNAL,
                           cv.CHAIN_APPROX_SIMPLE)[1]
    cnts = [c for c in cnts if (area[0] <= cv.contourArea(c) <= area[1])]
    cnts = sorted(cnts, key=cv.contourArea, reverse=True)
    return cnts


def findBean(img, area):
    if img is None:
        return []

    blankImg = createBlankImg(img.shape[:2])
    cnts = findContours(img, (100, area[1]))
    drawRects(blankImg, cnts, 0)
    cnts = findContours(blankImg, area)
    drawRects(img, cnts, 30)
    return cnts


def atCenter(img, cnt):
    height, width = img.shape[:2]
    x, y, w, h = cv.boundingRect(cnt)
    cx = x+(w//2)

    if abs(cx - width//2) < 20:
        return True

    return False