from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

service = ChromeService(executable_path="C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demos.jquerymobile.com/1.4.5/checkboxradio-radio/")
driver.maximize_window()
driver.implicitly_wait(10)

wb = load_workbook(filename = "radiobutton.xlsx")

sheetRange = wb['Sheet1']
pilihan = sheetRange['A2'].value

if pilihan == 'one':
    driver.find_element(By.XPATH, "(//label[@class='ui-btn ui-corner-all ui-btn-inherit ui-btn-icon-left ui-radio-off'][normalize-space()='One'])[1]").click()
elif pilihan == 'two':
    driver.find_element(By.XPATH, "(//label[@for='radio-choice-0b'])[1]").click()
else:
    print('Data tidak muncul')
   