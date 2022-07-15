from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver import  Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options





def pars():
    while True:
        driver = webdriver.Chrome("/home/serhii/PycharmProjects/pythonProject36/chromedriver")
        driver.set_window_size(1920, 1080)
        driver.get(f"https://www.bezkolejki.eu/luwlodz")
        time.sleep(2)
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        time.sleep(0.5)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[6]/div/button').click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div/div[3]/div/div/div/button").click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        main_page = driver.page_source
        soup = BeautifulSoup(main_page, "html")
        soup = soup.find_all("div", class_="vc-weeks")
        for elem in soup:
            elem = elem.find_all_next("span")
            for elem in elem:
                try:
                    if elem["aria-disabled"] != "true":
                        print(elem["aria-label"])
                        time.sleep(10)
                    else:
                        continue
                except KeyError:
                    continue
        print("__________________________")




  
pars()



