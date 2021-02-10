from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookiesfile='data.json'
websitesToVisit=['https://rg.ru/', 'https://www.sports.ru/'  ]
#websitesToVisit=['http://vk.com'  ]
devicesToEmulate=['Laptop FullHD', 'iPhone Xs', 'iPhone X' ]


deviceProperties={'iPhone X':
                  {"deviceName": "iPhone X"},
                  'iPhone Xs':
                  {"deviceMetrics": { "width": 1125, "height": 2436, "pixelRatio": 3.0 },
                   "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"},
                  'Laptop FullHD':
                  {"deviceMetrics": {"width": 1920, "height": 1080},
                   "userAgent"    : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
}

#read cookies from json file
with open(cookiesfile) as json_file:
    cookiesdata = json.load(json_file)
cookies=cookiesdata['cookies']
print("cookies done, starting test")
#run the test
for device in devicesToEmulate:
    for website in websitesToVisit:
    #set device options
        mobile_emulation = deviceProperties[device]
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome( desired_capabilities = chrome_options.to_capabilities())
        #set cookies
        driver.get('http://vk.com')
        for cookie in cookies:
            driver.add_cookie(cookie)
        #actually go places
        driver.get(website)
        driver.implicitly_wait(10)
        #get links
        try:
            all_options = driver.find_elements_by_tag_name('a')
        except Exception:
            print("no links")
            all_options = []
        option = all_options[random.randrange(len(all_options))]  # choose random link
        link = option.get_attribute("href")
        print("link:", link)
        try:
            option.click()
        except Exception:
            print("cannot click")
        driver.close()
    print("device emulation done: ", device)
print("all done")




