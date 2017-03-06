import selenium.webdriver.chrome.service as service
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
import os
import time
from selenium.common import exceptions
from config import *
from BeautifulSoup import BeautifulSoup


serv = service.Service(config.chromeDriver)
serv.start()
driver = webdriver.Remote(
        command_executor='http://%s:4444/wd/hub' % config.server,
        desired_capabilities=DesiredCapabilities.CHROME)

driver.set_page_load_timeout(5)
print 'Loading URL : %s' % config.URL

while True :
    try :
        driver.get(config.URL)
        break
    except exceptions.TimeoutException:
        continue
driver.find_element_by_css_selector('.ui-button-icon-primary.ui-icon.ui-icon-closethick').click()
driver.find_element_by_css_selector('input[name="trainInput"]').send_keys('12723')
time.sleep(2)
driver.find_element_by_css_selector('#showAllInstancesBtn .ui-button-text').click()
time.sleep(2)
driver.find_elements_by_css_selector('#trainInstances .oneInstanceSpanBtn.ui-button.ui-widget'
                                     '.ui-state-default.ui-corner-all.ui-button-text-only')[0].click()

data = []
soup = BeautifulSoup(driver.page_source)
table = soup.findAll('table', attrs={'class':'fullRunningTbl'})[1]
#print table
table_body = table.find('tbody')
#print table_body
rows = table_body.findAll('tr')
for row in rows:
    cols = row.findAll('td')
    cols = [str(ele.text.strip()) for ele in cols]
    cols = [e.rstrip('.') for e in cols]
    if len(cols) > 2 :
        data.append(cols)

for line in data :
    print line

driver.close()