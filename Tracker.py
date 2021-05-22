print('Vanakkam!')
import requests
from bs4 import BeautifulSoup
import EmailSender
#import smtplib

#import winsound

#from playsound import playsound

URL = 'https://www.amazon.in/gp/product/B07HLBTQZF/ref=s9_acss_bw_cg_revamp1_2b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=TBATZ9YEJVGZPW8X1XR6&pf_rd_t=101&pf_rd_p=4b788029-5c6f-44fc-87f1-ae4dcaa2a358&pf_rd_i=13773797031'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

#frequency = 2500 #Hertz
#duration = 1000  #ms

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    #print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id='priceblock_ourprice').get_text() 
    price_converted = float(price[2:7].replace(",","")) 

    print(title.strip())

    print(price.strip())

    print(price_converted)

    if(price_converted <= target):
       
        EmailSender.email_anuppu()
        
check_price()



    


