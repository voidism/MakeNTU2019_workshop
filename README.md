# MakeNTU 2019 workshop - FaceLock

MakeNTU 2019 工作坊小project - 用 Microsoft Azure, OpenCV, Raspberry Pi 3 製作一個人臉置物鎖

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

填入名稱、位置(server位置)、Pricing Tier 選 f0、Resource group 按"新建"創一個


![](https://i.imgur.com/Qtz0mAl.png)

稍等一會就會顯示部署成功，可以按"釘選到儀表板"

![](https://i.imgur.com/x4vTlsy.png)

從儀表板進入資源(右上角)

![](https://i.imgur.com/nySOAwm.png)

進入keys取得金鑰

![](https://i.imgur.com/SOKknf5.png)

複製下金鑰(任一支)，等等用

![](https://i.imgur.com/NSVdlyj.png)


## 前製作業

- 在程式碼 `face_api.py` 的第6行 填入 `###your azure api key###` 和 `###you server location###`
- 將 servo motor 與 GPIO pin腳連接:
  - 紅 <=> pin 2
  - 棕 <=> pin 6
  - 橘 <=> pin 11
  - ![gpio](https://www.bigmessowires.com/wp-content/uploads/2018/05/Raspberry-GPIO.jpg)
  - ![](https://i.imgur.com/nebKdoa.jpg)
- 將 web-cam 用 USB 與 RPi 相接

## Run Code

跑 `main_gui.py`，看看有沒有漏裝東西

## 使用說明
正常執行下會出現GUI小視窗：

![](https://i.imgur.com/GUmOAkH.png)

1. 先將臉部對準 web-cam，按 register 註冊，登錄成功後 Lock 會打開，在 Checkout 之前無法再次註冊
2. 按 Lock 將鎖鎖上後，下次可再將臉部對準 web-cam 按 Unlock 開鎖，若是其他人則無法開鎖
3. 在上鎖的情況下可按將臉部對準 web-cam 按 Checkout，確認是本人後即可登出，並可由下一位使用者再次註冊
4. 所有錯誤操作皆會顯示提示字眼於下方，如：人臉沒有對準鏡頭，會顯示 `Face Not Detected!`。