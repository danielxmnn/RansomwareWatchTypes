from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import index
import diferenca

aux = index.lista
lista = list(aux.keys())
SevErro = "Error accessing resource: "
SevErro2 = "Onion.ws is a "


def _screenshot(a):
    driver = webdriver.Firefox()
    driver.get(a)
    sleep(15)
    el = driver.find_element(By.NAME, 'body')
    el.screenshot("img/" + str(x) + ".png")
    driver.close()
    driver.quit()
    return


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
            if SevErro in response.text:
                try:
                    reserva1 = site.replace("onion.ly", "onion.ws")
                    response = requests.get(reserva1, headers=headers)
                    if SevErro2 not in response.text:
                        _screenshot(reserva1)
                    else:
                        print("!ERROR!")
                        print(x)
                        print("!ERROR!")
                except Exception as e:
                    print("Error: ")
                    print(e)
                    pass
            if SevErro not in response.text:
                _screenshot(site)
            else:
                print("!ERROR!")
                print(x)
                print("!ERROR!")
        except Exception as e:
            print("Error: ")
            print(e)
            pass

except Exception as e:
    print("Error: ")
    print(e)
