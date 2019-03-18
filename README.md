# MakeNTU 2019 workshop - FaceLock

MakeNTU 2019 工作坊小project - 用 Microsoft Azure, OpenCV, Raspberry Pi 3 製作一個人臉置物櫃鎖

![cover](cover.jpg)

## Requirements

- a Raspberry Pi 3 model B+
- a servo motor
- a web-cam
- python3
- python-opencv installed

## Microsoft Azure apply

### 辦帳號

如果有學校信箱，可直接申請教育試用版，免綁信用卡

https://azure.microsoft.com/zh-tw/free/students/

![](https://i.imgur.com/Er8OD5o.png)

需要驗證學校的電子郵件

![](https://i.imgur.com/kGLr2mb.png)

按同意，申請完成

![](https://i.imgur.com/wwShjgL.png)

### 開通API

來到 Azure 首頁

![](https://i.imgur.com/7KcCmI6.png)

點選"建立資源"

![](https://i.imgur.com/Unql15X.png)

點選"AI + 機器學習服務"，選"Face"

![](https://i.imgur.com/5QkDnQj.png)

填入名稱、位置(server位置，要記得，等等會用到)、Pricing Tier 選 f0、Resource group 按"新建"創一個


![](https://i.imgur.com/Qtz0mAl.png)

稍等一會就會顯示部署成功，可以按"釘選到儀表板"

![](https://i.imgur.com/x4vTlsy.png)

從儀表板進入資源(右上角)

![](https://i.imgur.com/nySOAwm.png)

進入keys取得金鑰

![](https://i.imgur.com/SOKknf5.png)

複製下金鑰(任一支)，等等用

![](https://i.imgur.com/NSVdlyj.png)



## RPI 基本操作

給大家的RPI都已經灌好OS，如果需要自己灌，下載此映像檔並解壓縮，用[ApplePI-Baker](<https://www.pibakery.org/download.html>)之類的程式燒錄進SD卡即可

<https://drive.google.com/file/d/1wUdb_WaU1hjPG_VCjFBW8ShqgJWwMoqK/view?usp=sharing>

此映像檔已經裝好python3.6、miniconda、python-opencv

並設有一組wifi名稱密碼，會自動連上，可以直接將手機的無限基地台名稱及密碼設定如下，RPI即可自己連上：

![](https://i.imgur.com/F8yWHDb.png)



當RPI跟電腦都各自連上手機分享的網路，透過手機的基地台設定可以察看所有連上裝置的內網ip



![](https://i.imgur.com/3Bs3Qxr.jpg)

找到RPI的內網IP位置，且電腦也已經連接上手機分享的網路，就可以使用Terminal打`ssh pi@192.168.xx.xx`，password:`raspberry` 連上RPI了

但因為ssh只能用bash，沒辦法看到RPI畫面，如果想用VNC連RPI看畫面，需要裝一下tightvncserver：

```bash
sudo apt-get install tightvncserver
tightvncserver
```

第一次使用會叫你設定一個8位數的VNC密碼

然後用mac開啟Finder>>前往>>連接伺服器

打入  `vnc://{RPI的內網IP}:5901` 如：`vnc://192.168.0.104:5901`。之後按連線輸入密碼，即可連上。

如果下次開機，也想使用VNC，記得要再打一次`tightvncserver`

如果是windows請下載VNC的client端軟體，如<https://www.realvnc.com/en/connect/download/viewer/>

## 下載本專案程式碼

隨便找個地方，像是`~` (`/home/pi/`)

打`git clone https://github.com/voidism/MakeNTU2019_workshop`

## 前置作業

- 在程式碼 `face_api.py` 的第6行 填入 `###your azure api key###` 和 `###you server location###`。如：West US 就填 [westus.api.cognitive.microsoft.com](westus.api.cognitive.microsoft.com)。
- 將 servo motor 與 GPIO pin腳連接:
  - 紅 <=> pin 2
  - 棕 <=> pin 6
  - 橘 <=> pin 11
  - ![gpio](https://www.bigmessowires.com/wp-content/uploads/2018/05/Raspberry-GPIO.jpg)
  - ![](https://i.imgur.com/nebKdoa.jpg)
- 將 web-cam 用 USB 與 RPi 相接

## Run Code

1. 跑 `python3 -i servo.py`:

```
>>> s = Servo()
>>> s.turn(90)
```

確認伺服馬達是否運作正常。

2. 跑 `python3 -i camera.py`:

```
>>> s = Scanner(0)
>>> s.get_photo("test.png")
```

確認 web-cam 是否有拍下照片 `"test.png"`。

3. 跑 `python3 -i face_api.py`:

```
>>> s = AzureAPI()
>>> s.GetFaceId("test.png")
```

確認 API 是否有回傳資料。


4. 如果一切順利，就可以跑 `main_gui.py`了。

## 使用說明
`main_gui.py` 正常執行下會出現GUI小視窗：

![](https://i.imgur.com/up4xYHQ.png)

1. 先將臉部對準 web-cam，按 register 註冊，登錄成功後 Lock 會打開，在 Checkout 之前無法再次註冊
2. 按 Lock 將鎖鎖上後，下次可再將臉部對準 web-cam 按 Unlock 開鎖，若是其他人則無法開鎖
3. 在上鎖的情況下可按將臉部對準 web-cam 按 Checkout，確認是本人後即可登出，並可由下一位使用者再次註冊
4. 所有錯誤操作皆會顯示提示字眼於下方，如：人臉沒有對準鏡頭，會顯示 `Face Not Detected!`。