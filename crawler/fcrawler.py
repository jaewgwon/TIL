from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

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
driver.find_elements_by_name("fap_jobfair_divide_seq")[1].click()
driver.find_element_by_id("choiceJobfairModalBtnSave").click()
WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to_alert().accept()
url_list = []
for i in range(1, 8):
    url = 'https://job.sesoc.global/fap/user/user_job_advertisement_list_form?clickedPage=' + str(i)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    urls = soup.select('div.jobname > a')
    for item in urls:
        url_list.append(item.attrs['href'])

data_list = []

for target in url_list:
    row = []
    url2 = 'https://job.sesoc.global' + target
    driver.get(url2)
    #title
    row.append(driver.find_element_by_xpath("//*[@ng-model='::jobAdCategory.fap_job_ad_title']").get_attribute('value'))
    #name
    row.append(driver.find_element_by_id('comp_en_nm').get_attribute('value'))
    #wage
    row.append(driver.find_element_by_class_name('basic-total').text)
    #wage_detail
    row.append(driver.find_element_by_xpath("//*[@ng-model='::jobAdPay.JobPayList[0].fap_job_pay_dtl']").get_attribute('value'))
    #jan_time
    row.append(driver.find_element_by_xpath("//*[@ng-model='::jobAdPay.JobPayList[0].JobPayBaseList[2].JobServiceWorkList[0].fap_job_service_work_tm']").get_attribute('value'))
    #jan_money
    row.append(driver.find_element_by_xpath("//*[@ng-model='::jobAdPay.JobPayList[0].JobPayBaseList[2].fap_job_pay_base_info']").get_attribute('value'))
    #jan_detail
    row.append(driver.find_element_by_xpath("//*[@ng-model='::jobAdPay.JobPayList[1].fap_job_pay_dtl']").get_attribute('value'))
    #transp_fee
    row.append(driver.find_element_by_xpath("//*[@ng-model='::jobAdPay.JobPayList[2].fap_job_pay_info']").get_attribute('value'))
    #inc_fee
    row.append(driver.find_element_by_xpath("//*[@ng-model='::jobAdPay.JobPayList[3].fap_job_pay_dtl']").get_attribute('value'))
    #jinjai
    row.append(driver.find_element_by_xpath("//*[@ng-model='::jobIdealPerson.fap_job_pref[0].fap_job_pref_dtl']").get_attribute('value'))

    data_list.append(row)
    
result = pd.DataFrame(data_list)
result.to_csv('crawled_data.csv', encoding='UTF-8')


    


    