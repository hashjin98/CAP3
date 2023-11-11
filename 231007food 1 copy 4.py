from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import csv
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import traceback
import re

def info_get(Review_name):
    try:
        driver.execute_script("window.scrollTo(0, 3300)") 
        time.sleep(0.1)
        try: # 메뉴 더보기 클릭
            WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR ,'div.place_section.I_y6k > div.lfH3O')))
            더보기 = driver.find_element(By.CSS_SELECTOR ,'div.place_section.I_y6k > div.lfH3O')
            더보기.click()
        except:
            pass
        time.sleep(0.5)
        
        
        try:
            aaa = driver.find_elements(By.CLASS_NAME, 'xHaT3')
            for i in aaa:
                i.send_keys(Keys.ENTER)
        except:
            pass
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        
        address = soup.select_one('.LDgIH').text if soup.select_one('.LDgIH') else "" #주소
        # print(address)
        # tel = soup.select_one('.xlx7Q').text if soup.select_one('.xlx7Q') else ""# 전화번호    
        male = soup.select_one('g.c3-chart-arc.c3-target.c3-target-male > text:nth-child(3)').get_text() if soup.select_one('g.c3-chart-arc.c3-target.c3-target-male > text:nth-child(3)') else "" #남성
        female = soup.select_one('g.c3-chart-arc.c3-target.c3-target-female > text:nth-child(2)').get_text() if soup.select_one('g.c3-chart-arc.c3-target.c3-target-female > text:nth-child(2)') else "" #여성 
        div = soup.find('div', class_='nZapA')if soup.select_one('.nZapA') else "" #역에서 xm
        around = ""
        if div:
            station = div.strong.text  # <strong> 태그의 텍스트 추출
            around = "".join([text for text in div.stripped_strings if text not in div.span.stripped_strings and text != station])  # <strong>과 <span> 태그를 제외한 텍스트 추출

            
        op_hour = soup.select_one('.A_cdD').text  if soup.select_one('.A_cdD') else "" #영업시간

        
        tel = soup.find('path', {'d' : "M2.92 1.15L.15 3.93a.5.5 0 00-.14.45 16.09 16.09 0 0012.6 12.61.5.5 0 00.46-.14l2.78-2.78a.5.5 0 000-.71l-4.18-4.18-.07-.06a.5.5 0 00-.64.06l-1.9 1.9-.28-.18a9.53 9.53 0 01-2.65-2.63L5.96 8 7.88 6.1a.5.5 0 000-.71L4.41 1.93l-.78-.78a.5.5 0 00-.7 0zm5.62 10.79l.37.21.09.04a.5.5 0 00.49-.13l1.82-1.82 3.48 3.47-2.24 2.24-.07-.01A15.1 15.1 0 011.14 4.84l-.1-.4 2.24-2.23 3.54 3.53-1.84 1.84a.5.5 0 00-.08.6 10.54 10.54 0 003.64 3.76z"}).find_parent('div').find(class_='xlx7Q').text\
            if soup.find('path', {'d' : "M2.92 1.15L.15 3.93a.5.5 0 00-.14.45 16.09 16.09 0 0012.6 12.61.5.5 0 00.46-.14l2.78-2.78a.5.5 0 000-.71l-4.18-4.18-.07-.06a.5.5 0 00-.64.06l-1.9 1.9-.28-.18a9.53 9.53 0 01-2.65-2.63L5.96 8 7.88 6.1a.5.5 0 000-.71L4.41 1.93l-.78-.78a.5.5 0 00-.7 0zm5.62 10.79l.37.21.09.04a.5.5 0 00.49-.13l1.82-1.82 3.48 3.47-2.24 2.24-.07-.01A15.1 15.1 0 011.14 4.84l-.1-.4 2.24-2.23 3.54 3.53-1.84 1.84a.5.5 0 00-.08.6 10.54 10.54 0 003.64 3.76z"}) else ""
        car = soup.find('path', {'d' : "M10.05 15.48h4.45V7.86a3.26 3.26 0 01-2.22.86c-.81 0-1.57-.3-2.15-.81a3.24 3.24 0 01-2.15.81 3.24 3.24 0 01-2.13-.79 3.24 3.24 0 01-2.13.8 3.26 3.26 0 01-2.22-.87v7.62h4.44V11.3a.5.5 0 01.5-.5h3.11a.5.5 0 01.5.5v4.17zm-1 0V11.8h-2.1v3.67h2.1zm6.45-9.79a.5.5 0 010 .04v10.25a.5.5 0 01-.5.5H1a.5.5 0 01-.5-.5V5.73 5.7a3.11 3.11 0 010-.1.5.5 0 01.05-.22L2.3 1.78a.5.5 0 01.45-.28h10.5a.5.5 0 01.45.28l1.75 3.59a.5.5 0 01.05.22v.1zM3.06 2.5L1.5 5.7a2.19 2.19 0 002.22 2.02 2.24 2.24 0 001.74-.82.5.5 0 01.78 0 2.24 2.24 0 001.74.82c.7 0 1.33-.31 1.75-.85a.5.5 0 01.79 0 2.24 2.24 0 001.76.85c1.2 0 2.16-.9 2.22-2.02l-1.56-3.2H3.06z"}).find_parent('div').find(class_ ='vV_z_').text\
            if soup.find('path', {'d' : "M10.05 15.48h4.45V7.86a3.26 3.26 0 01-2.22.86c-.81 0-1.57-.3-2.15-.81a3.24 3.24 0 01-2.15.81 3.24 3.24 0 01-2.13-.79 3.24 3.24 0 01-2.13.8 3.26 3.26 0 01-2.22-.87v7.62h4.44V11.3a.5.5 0 01.5-.5h3.11a.5.5 0 01.5.5v4.17zm-1 0V11.8h-2.1v3.67h2.1zm6.45-9.79a.5.5 0 010 .04v10.25a.5.5 0 01-.5.5H1a.5.5 0 01-.5-.5V5.73 5.7a3.11 3.11 0 010-.1.5.5 0 01.05-.22L2.3 1.78a.5.5 0 01.45-.28h10.5a.5.5 0 01.45.28l1.75 3.59a.5.5 0 01.05.22v.1zM3.06 2.5L1.5 5.7a2.19 2.19 0 002.22 2.02 2.24 2.24 0 001.74-.82.5.5 0 01.78 0 2.24 2.24 0 001.74.82c.7 0 1.33-.31 1.75-.85a.5.5 0 01.79 0 2.24 2.24 0 001.76.85c1.2 0 2.16-.9 2.22-2.02l-1.56-3.2H3.06z"}) else ""
        소개 = soup.find('path', {'d' : "M11 15V3H2v12h9zm1-6h3v6a1 1 0 01-1 1H2a1 1 0 01-1-1V3a1 1 0 011-1h9a1 1 0 011 1v6zm0 1v5h2v-5h-2zM4 5.5h5v1H4v-1zM4 8h5v1H4V8zm0 2.5h3v1H4v-1z"}).find_parent('div').find(class_ ='zPfVt').text\
            if soup.find('path', {'d' : "M11 15V3H2v12h9zm1-6h3v6a1 1 0 01-1 1H2a1 1 0 01-1-1V3a1 1 0 011-1h9a1 1 0 011 1v6zm0 1v5h2v-5h-2zM4 5.5h5v1H4v-1zM4 8h5v1H4V8zm0 2.5h3v1H4v-1z"}) else ""
        소개 = re.sub(r'\s+', ' ', 소개).strip()
        # print(소개)
        
        분위기 =[]
        인기토픽 = []
        찾는목적 = []
        etc = []
        # 데이터랩 분석
        해시태그 = soup.find_all(class_='nc5wr')
        for i in 해시태그:
            태그 = i.find_all(class_= 'sJgQj') 
            카테고리 = i.select_one('.pNnVF').text # 분위기
            for j in 태그:
                A = j.text
                A = A.replace(',', '')
                # print(A)
                if 카테고리 == '분위기':
                    분위기.append(A)
                elif 카테고리 == '인기토픽':
                    인기토픽.append(A)  
                elif 카테고리 == '찾는목적':
                    찾는목적.append(A)
                else:
                    etc.append(A)
                    
        # 메뉴 정보 크롤링
        ReviewTeb = driver.find_elements(By.CLASS_NAME, 'tpj9w._tab-menu')  
        for i in ReviewTeb:
            if i.text == '메뉴':
                try:
                    i.click()
                    time.sleep(0.8)
                    break
                except Exception as ex:
                    err_msg = traceback.format_exc()
                    print(err_msg)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        AAA = soup.findAll(class_ = 'E2jtL')
        for i in AAA:
            Food_Name = i.find(class_ = 'lPzHi').text
            Food_Price = i.find(class_ = 'GXS1X').text
            Food_URL = ""                        
            #음식 url
            food_div = i.find('div', class_='K0PDV') if i.find('div', class_='K0PDV') else ""
            if food_div != "":
                Food_URL = food_div['style']
                Food_URL = Food_URL.split(';')
                for prop in Food_URL:
                    if 'background-image' in prop:
                        Food_URL = prop.split('url("')[1].split('")')[0] 
                # print(Food_URL)
            
            # print(f'{Review_name}, {X}, {Y}')
            try:
                wr2.writerow([Review_name, Food_Name, Food_Price, address,"","", tel, 분위기, 인기토픽, 찾는목적, male, female, around, "", car, 소개, Food_URL])
            except Exception as ex:
                wr2.writerow([Review_name ,"저장중 error"])
                err_msg = traceback.format_exc()
                print(err_msg)
    except Exception as ex:
        err_msg = traceback.format_exc()
        print(err_msg)
        wr2.writerow(['ERROR',Review_name])
        
            
def review_get(Review_name): # 리뷰 크롤링
    # 리뷰 탭으로 이동
    ReviewTeb = driver.find_elements(By.CLASS_NAME, 'tpj9w._tab-menu')  
    for i in ReviewTeb:
        if i.text == '리뷰':
            i.click()
            time.sleep(0.8)
            break
    # 리뷰 더보기 버튼 누르기

    review_count = driver.find_element(By.CLASS_NAME, 'place_section_count')
    review_count = int(review_count.text)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(0.3)
    review_count = max(49, int(review_count/ 10 -1))
    try:
        if review_count > 0:  # 리뷰가 10개 이상이면
            for _ in range(review_count):
                driver.find_element(By.CLASS_NAME, 'lfH3O').click()
                time.sleep(0.5)
        # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    except NoSuchElementException:
        print("-모든 리뷰 더보기 완료-")

    time.sleep(1)
    RV_plus = driver.find_elements(By.CSS_SELECTOR, 'div.ZZ4OK > a')
    try:
        for i in RV_plus:
            i.send_keys(Keys.ENTER)
            # time.sleep(0.1)
    except Exception as ex:
        err_msg = traceback.format_exc()
        # print(err_msg)
    time.sleep(0.5)
    
    try:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        AAA = soup.findAll(class_='YeINN')
        for i, v in enumerate(AAA):
            Review_ID = v.find(class_='VYGLG').text if v.find(class_='VYGLG') else ""
            Review_Text = v.find(class_='zPfVt').text if v.find(class_='zPfVt') else ""
            Review_Text = re.sub(r'\s+', ' ', Review_Text).strip()
            Review_Date = v.find('time').text if v.find('time') else ""
            Review_count = v.find_all('span', class_='tzZTd')[1].text.strip() if v.find(class_='tzZTd') else ""
            Review_count = re.findall(r'\d+', Review_count)[0]
            # print(Review_count)
            # print([(i+1),Review_name, Review_ID, Review_Text,
            #             Review_Date, Review_count])

            wr.writerow([(i+1),Review_name, Review_ID, Review_Text,
                        Review_Date, Review_count])
    except Exception as ex:
        # Review_ID = ""
        # Review_Text = ""
        # Review_Date = ""
        # Review_count = ""
        print("리뷰 긁어 오던중 오류")
        err_msg = traceback.format_exc()
        # print(len(i))
        print(err_msg)
    print(F"{Review_name} 끝------------------------------------------")



df = pd.read_excel('한식1.xlsx')
all_data = pd.DataFrame()

# ------------------- CSV 파일 다루기
# data = open("230920_한식_종로_RV2_.csv", 'a', newline='', encoding='utf-8')
# wr = csv.writer(data)
data2 = open("231014_한식1_info.csv", 'a', newline='', encoding='utf-8')
wr2 = csv.writer(data2)

# 기본 세팅
driver = webdriver.Chrome()
url = 'https://map.naver.com/p?c=15.00,0,0,0,dh'
driver.get(url)
time.sleep(1)
driver.find_element(
    By.CSS_SELECTOR, 'div.input_box>input.input_search').send_keys(f"종각역\n")
time.sleep(1)


# 크롤링 시작
# for index, row in df.head(5).iterrows:
for index, row in df.iterrows():
    driver.switch_to.default_content()
    try:
        search_box = driver.find_element(
            By.CSS_SELECTOR, 'div.input_box>input.input_search')
        search_box.send_keys(Keys.CONTROL + "A")
        print(row['이름'])
        search_box.send_keys(f"{row['이름']}\n")
        time.sleep(0.5)

        driver.switch_to.frame('searchIframe')  # 검색창 iframe
        try:
            driver.find_element(By.CLASS_NAME, 'P7gyV').click()  # 검색어 1번
        except:
            pass
        
        driver.implicitly_wait(2)
        time.sleep(0.3)

         
        driver.switch_to.default_content() # 원래 ifrmae
        try:
            driver.switch_to.frame('entryIframe')  # 상세 내용 Iframe
        except:
            pass
        info_get(row['이름'])
        # review_get(row['이름'])
        
        
    except Exception as ex:
        err_msg = traceback.format_exc()
        # print(err_msg)

# data.close()
data2.close()
print(" 끝!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
