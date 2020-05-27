import requests
from bs4 import BeautifulSoup
import pandas as pd
import time



#city = input('Enter your city name : ')
city='pune'
header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1 RuxitSynthetic/1.0 v1314310596 t3156991074188025320 smf=0'}


#print('-----------------------------------------------------')
#print('######---- FREE EVENTS FROM BOOK MY SHOW ----######')
#print('-----------------------------------------------------')
#bms_url = 'https://in.bookmyshow.com/{}/events'.format(city)
#bms_response = requests.get(bms_url,headers=header)
#bms_html = bms_response.text
#soup = BeautifulSoup(bms_html,'lxml')
#
#all_events = soup.find_all('div',class_="a")
#for tr in all_events:
#    evts_meta = tr.find_all('div',class_="cx ep h") 
#    for i in evts_meta:
#        
#        # To find price
#        evts_price = i.find('div',class_="ak al er h i") 
#        #print(evts_price.text)
#        
#        if evts_price.text =='₹0 onwards' :       
#            # To find event title
#            evts_title = i.find('div',class_="ak al an ao er") 
#            print(evts_title.text)
#print('-----------------------------------------------------')
#
#
#
#print('-----------------------------------------------------')
#print('######---- FREE EVENTS FROM INSIDER.IN ----######')
#print('-----------------------------------------------------')
#insider_url = 'https://insider.in/{}'.format(city)
#time.sleep(3.2)
#insider_response = requests.get(insider_url,headers=header)
#insider_html = insider_response.text
#soup = BeautifulSoup(insider_html, 'lxml')
#
#print('----------------- Featured Events-------------------') 
#ft_events = soup.find_all('div',class_="carousel")
#for tr in ft_events:
#    evts_meta = tr.find_all('div',class_="featured-card-details") 
#    for j in evts_meta:
#        if j.text[-4:]== 'Free':
#            print(j.text)
#
#print('----------------- All categories -------------------')            
#workshop_events = soup.find_all('div',class_="event-card-details")
#for tr in workshop_events:
#    if tr.text[-4:] == 'Free':
#        print(tr.text)
#print('-----------------------------------------------------')
#
#
#
#
#print('-----------------------------------------------------')
#print('######---- FREE EVENTS FROM WHATS HOT ----######')
#print('-----------------------------------------------------')
#whot_url = 'https://www.whatshot.in/{}/events/all'.format(city)
#whot_response = requests.get(whot_url,headers=header)
#time.sleep(8.2)
#whot_html = whot_response.text
#soup = BeautifulSoup(whot_html, 'lxml')
#
#all_events = soup.find_all('div',class_='restaurant-card clearfix')
#for tr in all_events:
#    evt_meta= tr.find_all('div',class_="card-text") 
#    for i in evt_meta:
#        link_part=i.find('a') 
#        link='https://www.whatshot.in{}'.format(link_part.get('href'))
#        #print(link)
#        
#        #Go to each events link and grab price
#        evt_url=link
#        evt_response = requests.get(evt_url,headers=header)
#        time.sleep(4.2)
#        evt_html = evt_response.text
#        evt_soup = BeautifulSoup(evt_html, 'lxml')
#        all_txt = evt_soup.find('script', type="text/javascript")
#        if all_txt.text.find("Rs. 0") == -1 or all_txt.text.find("<p>Free") == -1:
#            pass
#        else:
#            print(i.text)
#print('-----------------------------------------------------')
            



# This site is dyamically loaded by JS and hence we cannt get all info directly by BS4.
# we need to mimic to open a website as a browser and load all dynamic JS content and then fetch data

#from selenium import webdriver
#print('-----------------------------------------------------')
#print('######---- FREE EVENTS FROM TOWNSCRIPT ----######')
#print('-----------------------------------------------------')
#
#driver = webdriver.Chrome('C:/Users/prasad.boyane/Desktop/py_analysis/py_prac/web_scraping/Free_Events/chromedriver_win32/chromedriver.exe')
#ts_url = 'https://www.townscript.com/in/{}?page=1'.format(city)
#driver.get(ts_url)
#time.sleep(6.4)
#ts_response=driver.execute_script('return document.documentElement.outerHTML')
#driver.quit()
#
#soup = BeautifulSoup(ts_response, 'lxml')
#full_page = soup.find_all('div',class_='digest-view-container mb-6')
#for i in full_page:
#    all_evt=i.find_all('div',class_='flex flex-col ng-star-inserted')
#    for j in all_evt:
#        each_strip=j.find_all('div',class_='scroll hide-scroll flex overflow-x-scroll p-3 pt-0 pb-2 md:py-4 md:p-5 md:-ml-3')
#        for k in each_strip:
#            each_evt = k.find_all('div',class_='event-card click-shrink')
#            for l in each_evt:
#                evt_det=l.find('div',class_='content w-full fadeIn')
#                evt_price=l.find('div',class_='footer')
#                if evt_price.text == 'Free':
#                    print(evt_det.text," | ",evt_price.text)
#        print()






