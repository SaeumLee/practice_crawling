# 필요 패키지 설치 
import selenium
from selenium import *
selenium.__version__
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import bs4
from bs4 import BeautifulSoup

# 웹드라이버 설정
from selenium import webdriver as wd
driver = wd.Chrome()

# 타겟 사이트 접속 (스타벅스)
target_site = 'https://www.starbucks.co.kr/store/store_map.do'
driver.get(target_site)
time.sleep(1)

# 찾고자 하는 요소가 있는 엘리먼트를 찾아 클릭. 
driver.find_element(By.CSS_SELECTOR, '#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search' ).click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#mCSB_2_container > ul > li:nth-child(2) > a').click()
time.sleep(1)

# 스토어이름 가져오기
store_names = driver.find_elements(By.CSS_SELECTOR, "#mCSB_3_container > ul > li")

for store_name in store_names:
    store_name = store_name.get_attribute('data-name')
    print(store_name)

# 스토어 주소 가져오기
store_adresses = driver.find_elements(By.CSS_SELECTOR, "#mCSB_3_container > ul > li > .result_details")
body = driver.find_element(By.ID,'mCSB_3_dragger_vertical')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", body)
#salist= list()
for store_adress in store_adresses:
    store_adress = store_adress.text
    #salist.append(store_adress)
    print(store_adress)

#len(salist)
    
    # 상위 3개 밖에 출력이 되지않음..
    # get.arrtibute('innerHTML') 활용해보기



# 스토어 정보 매칭해서 출력 확인
store_types = driver.find_elements(By.CSS_SELECTOR, "#mCSB_3_container > ul > li > i")
for store_type in store_types:
    store_type = store_type.get_attribute('class')
    if store_type == 'pin_generalDT':
        print('DT')
    if store_type == 'pin_general':
        print('G')
    if store_type == 'pin_reserve':
        print('R')



def starbucks_info():
    # Get the list of store elements
    store_names = driver.find_elements(By.CSS_SELECTOR, "#mCSB_3_container > ul > li")

    # Iterate through the list and extract information for each store
    store_info = []
    for store in store_names:
        store_name = store.get_attribute('data-name')
        store_address = store.find_element(By.CSS_SELECTOR, '.result_details').get_attribute('innerHTML')
        
        # Determine the store type based on the class of the icon
        icon_class = store.find_element(By.CSS_SELECTOR, 'i').get_attribute('class')
        if icon_class == 'pin_generalDT':
            store_type = 'DT'
        elif icon_class == 'pin_general':
            store_type = 'G'
        elif icon_class == 'pin_reserve':
            store_type = 'R'
        else:
            store_type = 'WT'
        
        # Append the extracted information to the list
        store_info.append({
            '지점명': store_name,
            '주소': store_address,
            '타입': store_type
        })

    # Return the list of store information
    return store_info

# Call the function
starbucks_info()

# get_attribute('innerHTML') 사용으로 최종적 전부 출력 되는것 확인
