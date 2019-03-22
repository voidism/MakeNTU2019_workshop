import picamera
import time


class Scanner:
    def __init__(self, URL=0):
        self.Frame = []
        self.status = False
        self.isstop = False
		
	# 攝影機連接。
        self.capture = picamera.PiCamera()
        time.sleep(2)
        self.start()

    def start(self):
        print('ipcam started!')

    def stop(self):
        self.isstop = True
        print('ipcam stopped!')

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

    def get_photo(self, filename):
        self.capture.capture(filename)