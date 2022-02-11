from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import index
import diferenca

aux = index.lista
lista = list(aux.keys())


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
    for x in lista:
        url = aux[x]
        site = url["site"]
        try:
            site = url["site"]
            _screenshot(site)
            diff = diferenca.diff("img/"+site+".png", "img/erro.png")
            if diff > 0.001:
                print(diff)
        except Exception as e:
            print("Error: ")
            print(e)
            pass

except Exception as e:
    print("Error: ")
    print(e)
