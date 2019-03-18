import cv2
import time
import threading

# 接收攝影機串流影像，採用多執行緒的方式，降低緩衝區堆疊圖幀的問題。
class Scanner:
    def __init__(self, URL=0):
        self.Frame = []
        self.status = False
        self.isstop = False
		
	# 攝影機連接。
        self.capture = cv2.VideoCapture(URL)
        self.start()

    def start(self):
	# 把程式放進子執行緒，daemon=True 表示該執行緒會隨著主執行緒關閉而關閉。
        print('ipcam started!')
        threading.Thread(target=self.queryframe, daemon=True, args=()).start()

    def stop(self):
	# 記得要設計停止無限迴圈的開關。
        self.isstop = True
        print('ipcam stopped!')

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()
        self.capture.release()
   
    def getframe(self):
	# 當有需要影像時，再回傳最新的影像。
        return self.Frame

    def get_photo(self, filename):
        cv2.imwrite(filename, self.Frame)
        
    def queryframe(self):
        while (not self.isstop):
            self.status, self.Frame = self.capture.read()
        
        self.capture.release()
