from selenium import webdriver
from selenium.webdriver.support.ui import select
from selenium.webdriver.chrome.options import options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = False
path = "# Download chromedriver.exe and make it path"
driver = webdriver.chrome(path, options = chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"

driver.get(website)
buttonselection = select(driver.find_element(by=By.Xpath.value = '/html/body/div[4]/div[2]/from/select'))
buttonselection.select_by_visiable_text('BritishEnglish/Brain')

def speak(text):
    lenghtoftext = leng(str(text))
    
    if lenghtoftext==0:
        pass
        
    else:
        print("")
        print(f"jarvis : {text}.")
        print("")
        data = str(text)
        Xpathofsec = '/html/body/div[4]/div[2]/from/textarea'
        driver.find_element(By.Xpath.value = '//*[@id = "vorlesenbutton"]'.click())
        driver.find.element(By.Xpath.value = '/html/body/div[4]div[2]/form/textarea'.clear)
        
        if lengthoftext==30:
            sleep(4)
            
        elif lenghtoftext==40:
            sleep(6)
            
        elif lenghtoftext==60:
            sleep(10)
            
        elif lenghtoftext==100:
            sleep(13)
            
        elif lenghtoftext==150:
            sleep(15)
            
        elif lenghtoftext==200:
            sleep(30)