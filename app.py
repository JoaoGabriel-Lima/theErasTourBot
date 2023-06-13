# create a program that will ask the user how many windows they want to open and then open that many windows with webdrivers with diferent sessions

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

number_of_windows = int(input("Quantas filas? "))
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito --window-size=400,400")

print("Não feche o programa até que seu ingresso seja comprado!")

driver_list = []
posx = 0
posy = 0

for i in range(number_of_windows):
    driver = webdriver.Chrome(options=options)
    driver.get("https://taylor-swift-rj.sales.ticketsforfun.com.br/")
    driver.set_window_position(posx,posy)
    if posx+470 > 1450:
        posx = 0
        posy += 400
    else:
        posx += 470
    
    if posy+400 > 1280:
        posy = 0


    driver_list.append(driver)
    # driver.find_element(By.XPATH, "/html/body/div/section[2]/div/div[3]/a[1]").click()

    # get cookies after clicking on the button
    print("--------------------")
    print("ID DO NAVEGADOR "+str(i+1)+": " + driver.get_cookie("Queue-it")["value"])
    print("--------------------")


    


