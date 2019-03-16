import cv2 as cv
from time import time
from utils import genHash, findBean, getClip, atCenter


class Scanner:
    """
    initialize with camera number
    """
    def __init__(self, cam):
        self.cap = cv.VideoCapture(cam)
        self.index = cam
        self.frame = None
        self.bean = None
        self.area = (50000, 200000)
        self.sleepUntil = time()

    """
    functions for get status
    """
    def ready(self):
        return self.cap.isOpened()

    def found(self):
        return (time() - self.sleepUntil >= 0) & (self.bean is not None)

    def quit():
        key = cv.waitKey(1) & 0xFF

        if key == ord('q'):
            return True

        return False

    """
    functions for set status
    """
    def sleep(self, last):
        self.sleepUntil = time() + last

    """
    functions for get value
    """
    def getBean(self):
        bean, self.bean = self.bean, None
        filepath = './tem/' + genHash() + '.png'
        cv.imwrite(filepath, bean)
        return filepath
    def get_photo(self, file_name):
        frame = self.cap.read()[1]
        cv.imwrite(file_name, frame)
        self.cap.release()
        self.cap = cv.VideoCapture(0)
    """
    functions for process frame
    """
    def read(self):
        self.frame = self.cap.read()[1]

    def parse(self):
        if self.frame is None:
            return

        cnts = findBean(self.frame, self.area)

        for cnt in cnts:
            if atCenter(self.frame, cnt):
                self.bean = getClip(self.frame, cnt, 20)

        cv.imshow('frame'+str(self.index), self.frame)

    """
    functions for closure
    """
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cap.release()
        cv.destroyAllWindows()