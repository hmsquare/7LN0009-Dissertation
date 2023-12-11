""" SCRAPE discuss"""
#!pip install selenium
from selenium import webdriver

driver = webdriver.Chrome('/Users/haley/Desktop/MA/MACompLing/WebScraping/chromedriver')
driver.implicitly_wait(10)
#driver.get('https://lihkg.com/thread/1712468/page/1')
driver.get('https://news.discuss.com.hk/viewthread.php?tid=29237535&extra=&page=1')
#print(driver.page_source)


comments_element = driver.find_elements_by_xpath("//div[@class='postmessage-content t_msgfont']")
cms = [cm.text for cm in comments_element]
wc = 0
for cm in comments_element:
    wc += len(cm.text)


print(cms, len(cms), wc)

driver.quit()

