import cv2 as cv
from time import time


class Scanner:
    """
    initialize with camera number
    """
    def __init__(self, cam=0):
        self.cap = cv.VideoCapture(cam)
        self.index = cam
        self.frame = None
        self.sleepUntil = time()

    """
    functions for get status
    """
    def ready(self):
        return self.cap.isOpened()

    """
    functions for set status
    """
    def sleep(self, last):
        self.sleepUntil = time() + last

    """
    functions for get value
    """
    def get_photo(self, file_name):
        frame = self.cap.read()[1]
        cv.imwrite(file_name, frame)
        self.cap.release()
        self.cap = cv.VideoCapture(0)

    """
    functions for closure
    """
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cap.release()
        cv.destroyAllWindows()