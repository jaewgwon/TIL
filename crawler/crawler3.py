import requests
from bs4 import BeautifulSoup
import codecs
import re
import json

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
url = 'https://book.naver.com/category/index.nhn?cate_code=100&tab=recommend&list_type=list&sort_type=salecount&page='
result_data = []

def list_crwl(inputNum):
	target_url = url + inputNum
	html = requests.get(target_url, headers = headers).content
	soup = BeautifulSoup(html, 'html.parser')
	#book_list = soup.find('ol', attrs={'class' : 'basic'})
	title_list = soup.find_all("dt", {"id": re.compile('book_title_*')})
	result_list = []
	for title in title_list:
		result_list.append(title.find("a", {"class" : "N=a:bta.title"}).attrs['href'])
	return result_list

def context_crwl(inner_url):
	data_format = {
	'book_title' : '',
	'book_image' : '',
	'book_writer' : '',
	'book_date' : '',
	'book_publisher' : '',
	'book_content' : ''
	}
	inner_html = requests.get(inner_url, headers = headers).content
	inner_soup = BeautifulSoup(inner_html, 'html.parser')
	if inner_soup.find('a', {'class' : re.compile('N=a:bil.title,*')}) != None:
		book_title = inner_soup.find('a', {'class' : re.compile('N=a:bil.title,*')}).text
		if book_title != None:
			data_format['book_title'] = book_title
	else:
		data_format['book_title'] = ''

	if inner_soup.find('a', {'class' : re.compile('N=a:bil.image,*')}) != None:
		book_img = inner_soup.find('a', {'class' : re.compile('N=a:bil.image,*')}).find('img').attrs['src']
		if book_img != None:
			data_format['book_image'] = book_img
	else:
		data_format['book_image'] = ''

	if inner_soup.find('a', {'class' : re.compile('N=a:bil.author,*')}):
		book_writer = inner_soup.find('a', {'class' : re.compile('N=a:bil.author,*')}).text
		if book_writer != None:
			data_format['book_writer']  = book_writer
	else:
		data_format['book_writer']  = ''

	#temp_text for extract published date
	if inner_soup.find('div', {'class' : 'book_info_inner'}) != None:
		temp_text = inner_soup.find('div', {'class' : 'book_info_inner'}).text
		if len(extract_date(temp_text)) == 1:
			data_format['book_date'] = extract_date(temp_text)[0]
	else:
		data_format['book_date'] = ''
	if inner_soup.find('a', {'class' : re.compile('N=a:bil.publisher*')}) != None:
		book_publisher = inner_soup.find('a', {'class' : re.compile('N=a:bil.publisher*')}).text
		if book_publisher != None:
			data_format['book_publisher'] = book_publisher
	else:
		data_format['book_publisher'] = ''
	if inner_soup.find('div', {'id' : re.compile('bookIntroContent')}) != None:
		book_content = inner_soup.find('div', {'id' : re.compile('bookIntroContent')}).text
		if book_content != None:
			data_format['book_content']  = book_content
	else:
		data_format['book_content']  = ''

	result_data.append(data_format)

	#print(inner_soup.find('a', {'class' : 'N=a:bil.title'}).text)


#input: string, output: ??? list?
#텍스트에서 XXXX.XX.XX 형태의 날짜를 추출하는 def
def extract_date(text):
	data = re.compile('[0-9]{4}[.][0-9]{2}[.][0-9]{2}')
	return data.findall(text)

def main():
	url_list = []

	#크롤링할 페이지 설정
	for i in range(1, 3):
		url_list = url_list + list_crwl('%d' % i)

	url_cnt = len(url_list)
	print('총 %d 권의 책이 크롤링될 예정입니다.' % url_cnt)

	p_cnt = 0
	for url in url_list:
		p_cnt = p_cnt + 1
		context_crwl(url)
		p_pcnt =  p_cnt/url_cnt*100
		print("Progress : %f%", p_pcnt)

	print('크롤링 완료.')

	result_json = json.dumps(result_data, ensure_ascii=False)

	print(result_json)

	file = open("crawled_data.json", "w")
	file.write(result_json)
	file.close()

	#print(result_data)


main()