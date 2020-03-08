from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://youtube.com')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')

search_key=input('Enter what u search : ')

searchbox.send_keys(search_key)

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')

searchbutton.click()
