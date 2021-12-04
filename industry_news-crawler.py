from GoogleNews import GoogleNews
import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

'''
Language: lang as zh-TW
Period: period as number, N, representing news from last N days
'''
googlenews = GoogleNews(lang='zh-TW', period='1d')

googlenews.search('dram')

#return json objects representing different news
results= googlenews.results(sort=True)

#clear googlenews to do fresh search next time
googlenews.clear()

ii=0
total=("\n 今日產業要聞/ Memory, Foundry & Others: " + str(time.strftime("%Y-%m-%d"))+ "\n \n"+ "Memory:\n")

for result in results:
    if ii<3:
        total=total+("\nTitle: "+ str(result['title'])+ "\nURL: "+ str(result['link'])+"\n")
    ii+=1
    #print ("\nTitle: ", result['title'], "\nURL: ", result['link'])

googlenews.search('記憶體')
results= googlenews.results(sort=True)
googlenews.clear()
ii=0

for result in results:
    if ii<2:
        total=total+("\nTitle: "+ str(result['title'])+ "\nURL: "+ str(result['link'])+"\n")
    ii+=1

total=total+"\n\nFoundry & Semiconductor: "+"\n"

googlenews.search('晶圓代工')
results= googlenews.results(sort=True)
googlenews.clear()
ii=0

for result in results:
    if ii<2:
        total=total+("\nTitle: "+ str(result['title'])+ "\nURL: "+ str(result['link'])+"\n")
    ii+=1

googlenews.search('IC')
results= googlenews.results(sort=True)
googlenews.clear()
ii=0

for result in results:
    if ii<2:
        total=total+("\nTitle: "+ str(result['title'])+ "\nURL: "+ str(result['link'])+"\n")
    ii+=1

googlenews.search('車用 晶片 半導體')
results= googlenews.results(sort=True)
googlenews.clear()
ii=0

for result in results:
    if ii<2:
        total=total+("\nTitle: "+ str(result['title'])+ "\nURL: "+ str(result['link'])+"\n")
    ii+=1

total=total+"\n\n總體經濟概況: "+"\n"

googlenews.search('全球經濟')
results= googlenews.results(sort=True)
googlenews.clear()
ii=0

for result in results:
    if ii<5:
        total=total+("\nTitle: "+ str(result['title'])+ "\nURL: "+ str(result['link'])+"\n")
    ii+=1

print(total)

content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "今日產業要聞"  #郵件標題
content["from"] = "securesally@gmail.com"  #寄件者
content["to"] = "industry.news.st30@gmail.com" #收件者
content["bcc"] = "shiooma2001@yahoo.com.tw, jons@powerchip.com, simonckuo@psc.com.tw, jennyl@psc.com.tw, jerrychiu@psc.com.tw, maxcho@deutron.com.tw, johnny@eectc.com.tw, miriankuo@mxic.com.tw, kelvintu@chipbond.com.tw, sean.analyst@gmail.com, chchen@piecemakers.com.tw, lethe.sailors@gmail.com, mirianhjkuo@gmail.com, tchsiao@esmt.com.tw, Chris_hu@esmt.com.tw, Phil.hsu@zentel-japan.com.tw, gene.wu@zentel-japan.com.tw, samuel.wang@zentel-japan.com.tw"
content.attach(MIMEText(total))  #郵件內容

import smtplib
with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        #smtp.login("industry.news.st30@gmail.com", "vgivxlawddpajvfs")  # 登入寄件者gmail (industry.news.st30)
        smtp.login("shiooma2007@gmail.com", "avavofnwvpstydll")  # 登入寄件者gmail (shiooma2007)
        smtp.send_message(content)  # 寄送郵件
        print("Sent Complete!")
    except Exception as e:
        print("Error message: ", e)

