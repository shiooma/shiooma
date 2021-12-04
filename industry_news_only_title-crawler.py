import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# 下載 google 首頁內容 with search keywords

url='https://www.google.com/search'
param1= {'q':'dram 三星 美光 海力士 -股價 -股市 -原物料 -104人力 -相關報導 -新聞 -購物 -劍橋英語 -Trendforce -CFM -Youtube -行业 -论坛 -專輯 -藍標 -Mouser -拍賣 -露天 -电脑 -Engineer -现货 -免费 -东方银星 -电子工程', 'tbs':'qdr:w'}
param2= {'q':'nand flash 華邦 旺宏 -股價 -股市 -原物料 -104人力 -相關報導 -新聞 -購物 -劍橋英語 -Trendforce -CFM -Youtube -行业 -论坛 -專輯 -藍標 -Multi-level -Mouser -Engineer -拍賣 -露天 -电脑 -question -Windows -现货 -免费 -东方银星 -电子工程','tbs':'qdr:w'}
param2a= {'q':'記憶體 鈺創 晶豪 ISSI 愛普 -股價 -股市 -原物料 -104人力 -相關報導 -新聞 -購物 -劍橋英語 -Trendforce -CFM -Youtube -行业 -论坛 -專輯 -藍標 -拍賣 -露天 -question -Windows -电脑 -现货 -免费', 'tbs':'qdr:w'}
param3= {'q':'晶圓代工 封測 -股價 -股市 -原物料 -104人力 -相關報導 -新聞 -購物 -劍橋英語 -Trendforce -CFM -Youtube -行业 -论坛 -專輯 -藍標', 'tbs':'qdr:d'}
param4= {'q':'IC 12吋廠 產能 -股價 -股市 -原物料 -104人力 -相關報導 -新聞 -購物 -劍橋英語 -Trendforce -CFM -Youtube -行业 -论坛 -專輯 -藍標 -日商公司 -好康', 'tbs':'qdr:d'}
param5= {'q':'車用 半導體 -股價 -股市 -原物料 -104人力 -相關報導 -新聞 -購物 -劍橋英語 -Trendforce -CFM -Youtube -行业 -论坛 -專輯 -藍標', 'tbs':'qdr:d'}
param6= {'q':'全球經濟 芯片 晶片 半導體 -股價 -股市 -原物料 -104人力 -相關報導 -新聞 -購物 -劍橋英語 -Trendforce -CFM -Youtube -行业 -论坛 -專輯 -藍標', 'tbs':'qdr:d'}

r=requests.get(url,params=param1)

# 確認是否下載成功
if r.status_code == requests.codes.ok: 
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  # 以 原始碼 的 表頭 抓出各類頭條新聞
  headlines = soup.find_all('h3')
 
  i=0
  total=("\n 今日產業要聞/ Memory, Foundry & Others: " + str(time.strftime("%Y-%m-%d"))+ "\n \n"+ "Memory:\n")

  for h in headlines:
      
    # 新聞標題
      if i<3: 
        #print("標題：" + h.text)
        total=total+ str(str(h.text)+"\n")
        i=i+1

    # 新聞網址
    #print("網址：" + link.get('href'))

# param2 (Flash)
  r=requests.get(url,params=param2)
  # 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  # 以 CSS 的 class 抓出各類頭條新聞
  headlines = soup.find_all('h3')
  j=0

  for h in headlines:
      
    # 新聞標題
      if j<2: 
        #print("標題：" + h.text)
        total=total+ str(str(h.text)+"\n")
        j=j+1
    # 新聞網址
    #print("網址：" + link.get('href'))
# print (total)

#param2a (記憶體)
  r=requests.get(url,params=param2a)
  # 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  # 以 CSS 的 class 抓出各類頭條新聞
  headlines = soup.find_all('h3')
  jj=0

  for h in headlines:
      
    # 新聞標題
      if jj<2: 
        #print("標題：" + h.text)
        total=total+ str(str(h.text)+"\n")
        jj=jj+1
    # 新聞網址
    #print("網址：" + link.get('href'))
# print (total)

# param3 (Foundry)
  r=requests.get(url,params=param3)
  # 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')
  total=total+str("\nFoundry / OSAT: \n")

  # 以 CSS 的 class 抓出各類頭條新聞
  headlines = soup.find_all('h3')
  k=0

  for h in headlines:
      
    # 新聞標題
      if k<3: 
        #print("標題：" + h.text)
        total=total+ str(str(h.text)+"\n")
        k=k+1
    # 新聞網址
    #print("網址：" + link.get('href'))

# param4 (Others-IC)
  r=requests.get(url,params=param4)
  # 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')
  total= total+str("\nOthers: \n")

  # 以 CSS 的 class 抓出各類頭條新聞
  headlines = soup.find_all('h3')
  l=0

  for h in headlines:
      
    # 新聞標題
      if l<1: 
        #print("標題：" + h.text)
        total=total+ str(str(h.text)+"\n")
        l=l+1
    # 新聞網址
    #print("網址：" + link.get('href'))

# param5 (Others-China Semiconductor)
  r=requests.get(url,params=param5)
  # 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  # 以 CSS 的 class 抓出各類頭條新聞
  headlines = soup.find_all('h3')
  m=0

  for h in headlines:
      
    # 新聞標題
      if m<1: 
        #print("標題：" + h.text)
        total=total+ str(str(h.text)+"\n")
        m=m+1
    # 新聞網址
    #print("網址：" + link.get('href'))

# param6 (Others-China Semiconductor)
  r=requests.get(url,params=param6)
  # 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  # 以 CSS 的 class 抓出各類頭條新聞
  headlines = soup.find_all('h3')
  n=0

  for h in headlines:
      
    # 新聞標題
      if n<3: 
        #print("標題：" + h.text)
        total=total+ str(str(h.text)+"\n")
        n=n+1
    # 新聞網址
    #print("網址：" + link.get('href'))

print (total)

content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "今日產業要聞"  #郵件標題
content["from"] = "securesally@gmail.com"  #寄件者
content["to"] = "industry.news.st30@gmail.com" #收件者
# content["bcc"] = "shiooma2001@yahoo.com.tw, shiooma2007@gmail.com, jons@powerchip.com, jons@psc.com.tw, simonckuo@psc.com.tw, jennyl@psc.com.tw, jerrychiu@psc.com.tw, maxcho@deutron.com.tw, johnny@eectc.com.tw, miriankuo@mxic.com.tw, kelvintu@chipbond.com.tw, sean.analyst@gmail.com, chchen@piecemakers.com.tw, lethe.sailors@gmail.com, mirianhjkuo@gmail.com"
content.attach(MIMEText(total))  #郵件內容

import smtplib
with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("industry.news.st30@gmail.com", "vgivxlawddpajvfs")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("Sent Complete!")
    except Exception as e:
        print("Error message: ", e)