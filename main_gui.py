from tkinter import *
from face_lock_system import LockSystem

class GUIDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.F = LockSystem()

    # TODO
        
    def createWidgets(self):
        self.register_button = Button(self)
        self.register_button["text"] = "Register"
        self.register_button.grid(row=2, column=1)
        self.register_button["command"] = self.register
        
        self.unlock_button = Button(self)
        self.unlock_button["text"] = "Unlock"
        self.unlock_button.grid(row=2, column=2)
        self.unlock_button["command"] = self.unlock
        
        self.lock_button = Button(self)
        self.lock_button["text"] = "Lock"
        self.lock_button.grid(row=2, column=3)
        self.lock_button["command"] = self.lock
        
        self.checkout_button = Button(self)
        self.checkout_button["text"] = "Checkout"
        self.checkout_button.grid(row=2, column=4)
        self.checkout_button["command"] = self.checkout

        self.displayText = Label(self)
        self.displayText["text"] = "Copyright © 2019 MakeNTU"
        self.displayText.grid(row=3, column=0, columnspan=7)
        
if __name__ == '__main__':
    root = Tk(className="Face Lock")
    app = GUIDemo(master=root)
    app.mainloop()