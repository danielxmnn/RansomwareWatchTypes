from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import index
import requests


aux = index.lista
lista = list(aux.keys())
SevErro = "Error accessing resource: "
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36'
    }
    for x in lista:
        url = aux[x]
        try:
            site = url["site"]
            response = requests.get(site, headers=headers)
            if SevErro not in response.text:
                tamanho = (len(response.content))
                print(x)
                print(site)
                print("--------")
                driver = webdriver.Firefox()
                driver.get(site)
                sleep(10)
                el = driver.find_element_by_tag_name('body')
                el.screenshot(str(x) + ".png")
                #driver.get_screenshot_as_file("" + str(url["site"]) + ".png")
                driver.quit()
        except Exception as e:
            print("Error: ")
            print(e)
            pass

except Exception as e:
    print("Error: ")
    print(e)
