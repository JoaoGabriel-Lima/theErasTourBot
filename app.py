from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# local = "SP" # "SP" ou "RJ"
number_of_windows = int(input("Quantas filas? "))
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito --window-size=400,400")

print("Não feche o programa até que seu ingresso seja comprado!")
link = ""

driver_list = []
posx = 0
posy = 0


for i in range(number_of_windows):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.taylorswifttheerastour.com.br/")
    if link != "":
        driver.get(link)
    else:
        driver.find_element(By.XPATH, "/html/body/div/section[2]/div/div[3]/a[1]").click()
    driver.set_window_position(posx,posy)
    if posx+470 > 1450:
        posx = 0
        posy += 400
    else:
        posx += 470
    
    if posy+400 > 1280:
        posy = 0


    driver_list.append(driver)

    #! COOKIES (Não apague o comentário abaixo)
    if link != "":
        driver.find_element(By.XPATH, "/html/body/div/section[2]/div/div[3]/a[1]").click()
        print("--------------------")
        print("ID DO NAVEGADOR "+str(i+1)+": " + driver.get_cookie("Queue-it")["value"])
        print("--------------------")


    


