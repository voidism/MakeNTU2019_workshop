from face_api import AzureAPI
from camera import Scanner
from utils import genHash

class LockSystem():
    def __init__(self):
        self.myAPI = AzureAPI()
        self.UserId = None
        self.locked = True
        self.cam = Scanner(0)
        self.img_file = genHash() + ".png"

    def Register(self, img_file):
        if self.locked == False:
            print("It is still unlocked!")
            return "It is still unlocked!"
        if self.UserId == None:
            self.cam.get_photo(self.img_file)
            faceid = self.myAPI.GetFaceId(self.img_file)
            self.UserId = faceid
            self._unlock()
            return "Unlocked!"
        else:
            print("This box is occupied!")
            return "This box is occupied!"

    def Unlock(self, img_file):
        if self.locked == False:
            print("It is still unlocked!")
            return "It is still unlocked!"
        if self.UserId == None:
            print("Have not register yet!")
            return "Have not register yet!"
        self.cam.get_photo(self.img_file)
        cur_id = self.myAPI.GetFaceId(self.img_file)
        if self.myAPI.VerifyFaceId(self.UserId, cur_id):
            self._unlock()
            return "Unlocked!"
        else:
            print("Verify fail. Please do again!")
            return "Verify fail. Please do again!"

    def Checkout(self, img_file):
        if self.UserId == None:
            print("Have not register yet!")
            return "Have not register yet!"
        elif not self.locked:
            print("Lock before checkout!")
            return "Lock before checkout!"
        self.cam.get_photo(self.img_file)
        cur_id = self.myAPI.GetFaceId(self.img_file)
        if self.myAPI.VerifyFaceId(self.UserId, cur_id):
            self.UserId = None
            print("Checkout Successfully!")
            return "Checkout Successfully!"
        else:
            print("Verify fail. Please do again!")
            return "Verify fail. Please do again!"

    def Lock(self):
        if self.locked == True:
            return "Already Locked!"
        self._lock()
        return "Locked!"

    def _unlock(self):
        self.locked = False

    def _lock(self):
        self.locked = True