import os

from face_api import AzureAPI
from camera import Scanner
from utils import genHash
from servo import Servo

class LockSystem:
    def __init__(self):
        self.myAPI = AzureAPI()
        self.UserId = None
        self.locked = True
        self.cam = Scanner(0)
        self.servo = Servo()

    def GetHashName(self):
        return genHash() + ".png"

    def Register(self):
        if self.locked == False:
            return "It is still unlocked!"
        if self.UserId == None:
            temp_name = self.GetHashName()
            self.cam.get_photo(temp_name)
            faceid = self.myAPI.GetFaceId(temp_name)
            os.remove(temp_name)
            if faceid == "":
                return "Face Not Detected!"
            if faceid == "api_error":
                return "API connect Fail!"
            self.UserId = faceid
            self._unlock()
            return "Unlocked!"
        else:
            return "This box is occupied!"

    def Unlock(self):
        if self.locked == False:
            return "It is still unlocked!"
        if self.UserId == None:
            return "Have not register yet!"
        temp_name = self.GetHashName()
        self.cam.get_photo(temp_name)
        cur_id = self.myAPI.GetFaceId(temp_name)
        os.remove(temp_name)
        if cur_id == "":
            return "Face Not Detected!"
        if cur_id == "api_error":
            return "API connect Fail!"
        if self.myAPI.VerifyFaceId(self.UserId, cur_id):
            self._unlock()
            return "Unlocked!"
        else:
            return "Verify fail. Please do again!"

    def Checkout(self):
        if self.UserId == None:
            return "Have not register yet!"
        elif not self.locked:
            return "Lock before checkout!"
        temp_name = self.GetHashName()
        self.cam.get_photo(temp_name)
        cur_id = self.myAPI.GetFaceId(temp_name)
        os.remove(temp_name)
        if cur_id == "":
            return "Face Not Detected!"
        if cur_id == "api_error":
            return "API connect Fail!"
        if self.myAPI.VerifyFaceId(self.UserId, cur_id):
            self.UserId = None
            return "Checkout Successfully!"
        else:
            return "Verify fail. Please do again!"

    def Lock(self):
        if self.locked == True:
            return "Already Locked!"
        self._lock()
        return "Locked!"

    def _unlock(self):
        self.locked = False
        self.servo.turn(0)

    def _lock(self):
        self.locked = True
        self.servo.turn(90)
