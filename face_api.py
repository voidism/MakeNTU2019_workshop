import http.client, urllib.request, urllib.parse, urllib.error, base64, json, ssl

ssl._create_default_https_context = ssl._create_unverified_context

class AzureAPI:
    def __init__(self, key='###your azure api key###', website='###you server location###'):
        self.DetectHeaders = {
            # Request headers
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': key,
        }

        self.VerifyHeaders = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': key,
        }

        self.params = urllib.parse.urlencode({
            # Request parameters
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
        })
        self.void = urllib.parse.urlencode({
        })
        self.website = website
        self.body = None
        self.response = None
        self.conn = http.client.HTTPSConnection(self.website)

    def Reconnect(self):
        self.conn = http.client.HTTPSConnection(self.website)

    def GetFaceId(self, filename):
        try:
            self.body = open(filename, mode="rb")
            # TODO
            self.response = self.conn.getresponse()
            data = self.response.read()
            result = json.loads(data.decode('ascii'))
            print(result)
            if len(result) == 0:
                return ""
            else:
                return result[0]['faceId']
        except Exception as e:
            print(e)
            print("Try: Reconnect to API.")
            self.Reconnect()
            return ""

    def VerifyFaceId(self, id1, id2):
        try:
            self.body = '{"faceId1":"%s", "faceId2":"%s"}'%(id1, id2)
            self.conn.request("POST", "/face/v1.0/verify?%s" % self.void, self.body, self.VerifyHeaders)
            self.response = self.conn.getresponse()
            data = self.response.read()
            result = json.loads(data.decode('ascii'))
            print(result)
            return result['isIdentical']
        except Exception as e:
            print(e)
            print("Try: Reconnect to API.")
            self.Reconnect()
            return False

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
