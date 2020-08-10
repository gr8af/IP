import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.pianote.com/'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'}

def check_price():
    
    page  = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    details = soup.find("div", class_="bg-white",recursive=True)
    details_relevant = details.find_next("div",class_="bg-white").get_text()
    price = int(details_relevant[9:12])
    if(price < 197):
        send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('apoorv.623@gmail.com','dxoonmdcfnaprrnv')

    Subject = "Price drop on Pianote"
    body = "Go to Link https://www.pianote.com/"

    msg = f"Subject:{Subject}\n\n{body}"

    server.sendmail("apoorv.623@gmail.com","apoorv.236@gmail.com",msg)

    print("Email Sent")

    server.quit()

while(True):
    check_price()
    time.sleep(60)