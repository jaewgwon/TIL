from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

def main():
    
    driver = webdriver.Chrome('/home/jaewgwon/lib/chromedriver')
    driver.implicitly_wait(3)
    ################################
    #J-FAIR 기업정보 크롤러
    #자신의 ID와 PW를 입력하세요.
    ################################
    user_id = ''
    user_pw = ''

    driver.get('https://job.sesoc.global/fap/user/user_login')
    driver.find_element_by_id('user_id').send_keys(user_id)
    driver.find_element_by_id('user_pw').send_keys(user_pw)
    driver.find_element_by_name('go').click()
    driver.find_element_by_link_text('잡페어 선택').click()
    driver.find_elements_by_name("fap_jobfair_divide_seq")[0].click()
    driver.find_element_by_id("choiceJobfairModalBtnSave").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to_alert().accept()
    url_list = []
    print("정보 조회를 시작합니다.")
    print("종료하시려면 Ctrl + C를 눌러주세요.")
    while(True):
        driver.get('https://job.sesoc.global/fap/user/user_personal_apply_status_form')
        time.sleep(1)




if __name__ == "__main__":
    main()