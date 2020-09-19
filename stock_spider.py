# get china stock symbols

from tqdm import tqdm
from time import sleep
from random import randint
from bs4 import BeautifulSoup
from requests import Request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Spider:

    def __init__(self, login_url='https://finance.yahoo.com/most-active'):
        print('init webdriver...')
        option = None
        option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=option)
        self.driver.get(login_url)
        print('webdriver initiated!')


# после открытия окна хрома нужно мануально проставить рынок China!

spider = Spider()
print('Выбрали China в автоматически открывшемся окне? Yes/No')
ans = input()
if ans.lower() != 'yes':
    raise 'Try Again'
else:
    print('You can run next cell!')


payload=pd.read_html(spider.driver.page_source)
table_0 = payload[0]
df = table_0

for i in tqdm(range(100)):
    spider.driver.find_elements_by_xpath('//*[@id="scr-res-table"]/div[2]/button[3]')[0].click()
    payload=pd.read_html(spider.driver.page_source)
    table_0 = payload[0]
    tmp_df = table_0
    df = df.append(tmp_df)
    time.sleep(randint(2,7) / 1.32)
    
df.to_excel('data/china_stocks.xlsx')
