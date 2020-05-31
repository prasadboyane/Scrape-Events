import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import glob
from selenium import webdriver


city = input('Enter your city name : ')
city=city.lower()

header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1 RuxitSynthetic/1.0 v1314310596 t3156991074188025320 smf=0'}


def append_to_file(fname,line):
    with open(fname,'a+') as f:
        f.write(line)

def remove_temp_files(fname):
    os.remove(fname)
    print(fname+" Removed!")

def cleanup_file(fname):

    try:
        if os.path.exists(fname) == False:
            return
    except Exception as e:
        print('Something went wrong ! ERROR: ', e)
    finally:
        pass


    if 'townscript_raw' in fname != -1:
        dframe = pd.read_csv(fname, sep='|', names=["Event Name", "Place", "Price"])
        data_frame_trimmed = dframe.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        flag=1
    
    if 'BookMyShow_raw' in fname != -1:
        dframe = pd.read_csv(fname, sep='|', names=["Date","Event Name", "Place", "Category", "Price"])
        data_frame_trimmed = dframe.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        flag=1
        
    if 'WhatsHot_raw' in  fname != -1:
        dframe = pd.read_csv(fname, sep='|', names=["Event Name","Place", "Date", "Time"])
        data_frame_trimmed = dframe.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        flag=1


    if 'Insider_raw' in  fname != -1:
        dframe = pd.read_csv(fname, sep='|', names=["Event Name", "Date", "Time", "Place","Price"])
        data_frame_trimmed = dframe.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        flag=1
        
        
    if flag==1:    
        data_frame_trimmed.to_csv(fname.split('.')[0]+'_1.csv', sep='|')
        remove_temp_files(fname)

#Dynamic scraping
print('-----------------------------------------------------')
print('######---- FREE EVENTS FROM BOOK MY SHOW ----######')
print('-----------------------------------------------------')
driver = webdriver.Chrome('C:/Users/prasad.boyane/Desktop/py_analysis/py_prac/web_scraping/Free_Events/chromedriver_win32/chromedriver.exe')
bms_url = 'https://in.bookmyshow.com/{}/events'.format(city)
driver.get(bms_url)
time.sleep(4.4)
bms_response=driver.execute_script('return document.documentElement.outerHTML')
driver.quit()

bms_html = bms_response
soup = BeautifulSoup(bms_html,'lxml')

all_events = soup.find_all('div',class_="ai eb v")
for tr in all_events:
    evts_meta = tr.find_all('div',class_="ax c er es et eu k v") 
    for evts in evts_meta:
        evts_dt=evts.find('div',class_='ar bk ev ew v')
        evts_title=evts.find('div',class_='al b ch fa fb')
        evts_place=evts.find('div',class_='b bd fa fb fc fd')
        evts_category=evts.find('div',class_='ap bd fd')
        evts_price=evts.find('div',class_='bd fc fd')
        
        if '₹0 onwards' in evts_price.text != -1 or 'Rs. 0' in evts_price.text != -1 :
            record = evts_dt.text+'|'+evts_title.text+'|'+evts_place.text+'|'+evts_category.text+'|'+evts_price.text + '\r\n'
            append_to_file('BookMyShow_raw.csv',record) 
cleanup_file('BookMyShow_raw.csv')   



print('-----------------------------------------------------')
print('######---- FREE EVENTS FROM INSIDER.IN ----######')
print('-----------------------------------------------------')
insider_url = 'https://insider.in/{}'.format(city)
time.sleep(3.2)
insider_response = requests.get(insider_url,headers=header)
insider_html = insider_response.text
soup = BeautifulSoup(insider_html, 'lxml')

#print('----------------- Featured Events-------------------') 
ft_events = soup.find_all('div',class_="featured-card-details")
for tr in ft_events:
    evt_name=tr.find('span',class_='featured-card-name-string')
    evt_dt=tr.find('span',class_='featured-card-date')
    evt_place=tr.find('span',class_='featured-card-venue')
    evt_price=tr.find('div',class_='featured-card-price')
    
    if 'Free' in evt_price.text != -1:
        record= evt_name.text.replace("|", "-")+'|'+evt_dt.text+'|'+evt_place.text+'|'+evt_price.text+'\r\n'
        append_to_file('Insider_raw.csv',record) 

#print('----------------- All categories -------------------')            
workshop_events = soup.find_all('div',class_="event-card-details")
for tr in workshop_events:
    evt_name=tr.find('div',class_='event-card-name')
    evt_dt=tr.find('span',class_='event-card-date')
    evt_place=tr.find('span',class_='event-card-venue')
    evt_price=tr.find('div',class_='event-card-container')
    
    if 'Free' in evt_price.text != -1:
        record= evt_name.text.replace("|", "-")+'|'+evt_dt.text+'|'+evt_place.text+'|'+evt_price.text+'\r\n'
        append_to_file('Insider_raw.csv',record) 
            
cleanup_file('Insider_raw.csv')




print('-----------------------------------------------------')
print('######---- FREE EVENTS FROM WHATS HOT ----######')
print('-----------------------------------------------------')
whot_url = 'https://www.whatshot.in/{}/events/all'.format(city)
whot_response = requests.get(whot_url,headers=header)
time.sleep(8.2)
whot_html = whot_response.text
soup = BeautifulSoup(whot_html, 'lxml')

all_events = soup.find_all('div',class_='restaurant-card clearfix')
for tr in all_events:
    evt_meta= tr.find_all('div',class_="card-text") 
    for i in evt_meta:
        link_part=i.find('a') 
        link='https://www.whatshot.in{}'.format(link_part.get('href'))
        #print(link)
        
        #Go to each events link and grab price
        evt_url=link
        evt_response = requests.get(evt_url,headers=header)
        time.sleep(4.2)
        evt_html = evt_response.text
        evt_soup = BeautifulSoup(evt_html, 'lxml')
        all_txt = evt_soup.find('script', type="text/javascript")
        if all_txt.text.find("Rs. 0") != -1 or all_txt.text.find("<p>Free") != -1:
            evt_name=i.find('div',class_='top-head')
            evt_place=i.find('div',class_='top-mid')
            evt_time=i.find('div',class_='top-last')
            record = evt_name.text+'|'+evt_place.text+'|'+evt_time.text+'\r\n'
            append_to_file('WhatsHot_raw.csv',record)
cleanup_file('WhatsHot_raw.csv')



#This site is dyamically loaded by JS and hence we cannt get all info directly by BS4.
#we need to mimic to open a website as a browser and load all dynamic JS content and then fetch data



print('-----------------------------------------------------')
print('######---- FREE EVENTS FROM TOWNSCRIPT ----######')
print('-----------------------------------------------------')

driver = webdriver.Chrome('C:/Users/prasad.boyane/Desktop/py_analysis/py_prac/web_scraping/Free_Events/chromedriver_win32/chromedriver.exe')
ts_url = 'https://www.townscript.com/in/{}?page=1'.format(city)
driver.get(ts_url)
time.sleep(6.4)
ts_response=driver.execute_script('return document.documentElement.outerHTML')
driver.quit()

soup = BeautifulSoup(ts_response, 'lxml')
full_page = soup.find_all('div',class_='digest-view-container mb-6')
for i in full_page:
    all_evt=i.find_all('div',class_='flex flex-col ng-star-inserted')
    for j in all_evt:
        each_strip=j.find_all('div',class_='scroll hide-scroll flex overflow-x-scroll p-3 pt-0 pb-2 md:py-4 md:p-5 md:-ml-3')
        for k in each_strip:
            each_evt = k.find_all('div',class_='event-card click-shrink')
            for l in each_evt:
                evt_det=l.find('div',class_='content w-full fadeIn')
                evt_price=l.find('div',class_='footer')
                if evt_price.text == 'Free':
                    record= evt_det.text + " | " + evt_price.text + '\r\n'
                    #print(record)
                    append_to_file('townscript_raw.csv',record)
            #print('')
cleanup_file('townscript_raw.csv')



#Combine all CSVs to 1 excel different sheets

#get all csvs in curr dir of specific patter using glob
extension = 'csv'
result = glob.glob('*raw_1.{}'.format(extension))
all_files = result
#all_files = ['BookMyShow_raw_1.csv','Insider_raw_1.csv','townscript_raw_1.csv','WhatsHot_raw_1.csv']

writer = pd.ExcelWriter('Free_events_{}.xlsx'.format(city), engine='xlsxwriter')
for f in all_files:
    print(f)
    df = pd.read_csv(f, sep='|')
    #print(df)
    df.to_excel(writer, sheet_name=f.split('.')[0], index=False)
writer.save()

#Remove temp files *raw_1.csv
for f in all_files:
    os.remove(f)