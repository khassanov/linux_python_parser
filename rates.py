import requests
import os
import sys

from bs4 import  BeautifulSoup

def get_html():
    url = 'https://allbanks.kz/%D0%BE%D0%B1%D0%BC%D0%B5%D0%BD%D0%BD%D0%B8%D0%BA%D0%B8/%D0%B0%D1%81%D1%82%D0%B0%D0%BD%D0%B0'
    req = requests.get(url)
    return req.text

def get_dollar_rate(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find("td", attrs={"class" : "currency"}, text='USD').find_parent("tr").find_all("td")[-1].text
    result2 = soup.find("td", attrs={"class" : "currency"}, text='USD').find_parent("tr").find_all("td")[1].text
    return 'Покупка: '+result + ' Продажа: ' + result2



def get_euro_rate(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find("td", attrs={"class" : "currency"}, text='EUR').find_parent("tr").find_all("td")[-1].text
    result2 = soup.find("td", attrs={"class" : "currency"}, text='EUR').find_parent("tr").find_all("td")[1].text
    return 'Покупка: '+result + ' Продажа: ' + result2



def get_rub_rate(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find("td", attrs={"class" : "currency"}, text='RUR').find_parent("tr").find_all("td")[-1].text
    result2 = soup.find("td", attrs={"class" : "currency"}, text='RUR').find_parent("tr").find_all("td")[1].text
    return 'Покупка: '+result + ' Продажа: ' + result2



def send_notify(message):
    if(message == dollars):
        title = 'Доллар США'
        os.system('notify-send "{}": "{}"'.format(title, message))
    elif(message == euros):
        title = 'Euro'
        os.system('notify-send "{}": "{}"'.format(title, message))
    else:
        title = 'Российский рубль'
        os.system('notify-send "{}": "{}"'.format(title, message))

dollars = get_dollar_rate(get_html())
euros = get_euro_rate(get_html())
rubs = get_rub_rate(get_html())

def main():
    
    send_notify(dollars)
    send_notify(euros)
    send_notify(rubs)

if __name__ == '__main__':
    main()
sys.setrecursionlimit(10000)