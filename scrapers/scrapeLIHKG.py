""" SCRAPE LIHKG"""
#!pip install selenium
from selenium import webdriver

driver = webdriver.Chrome('/Users/haley/Desktop/MA/MACompLing/WebScraping/chromedriver')
driver.implicitly_wait(10)
#driver.get('https://lihkg.com/thread/1356535/page/1')
driver.get('https://lihkg.com/thread/1712468/page/9')
#print(driver.page_source)


comments_element = driver.find_elements_by_xpath("//div[@class='_2cNsJna0_hV8tdMj3X6_gJ']")
cms = [cm.text for cm in comments_element]
wc = 0
for cm in comments_element:
    wc += len(cm.text)


print(cms, len(cms), wc)

driver.quit()


