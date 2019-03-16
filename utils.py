import hashlib
import time

def genHash():
    m = hashlib.md5()
    m.update(str(time.time()).encode('utf-8'))
    return m.hexdigest()[0:10]

