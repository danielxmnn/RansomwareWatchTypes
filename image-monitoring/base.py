import index
import requests
import webbrowser
import pyautogui
import time

aux = index.lista
lista = list(aux.keys())
SevErro = "is a darknet gateway or Tor2Web"

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36'
    }
    for x in lista:
        url = aux[x]
        try:
            try:
                response = requests.get(url["site"], headers=headers)
            except Exception as e:
                aux1 = url["site"]
                aux2 = aux1.replace(".ws", ".ly")
                response = requests.get(aux2, headers=headers)
            if SevErro not in response.text:
                tamanho = (len(response.content))
                print(x)
                print(url["site"])
                print("--------")
                webbrowser.open(url["site"], new=2)
                time.sleep(8)
                pyautogui.press('F11')
                time.sleep(8)
                pyautogui.screenshot(r'.\/img\/' + x + '_base.png')
                time.sleep(3)
                pyautogui.hotkey('ctrl', 'w')
                pyautogui.hotkey('ctrl', 'w')

        except Exception as e:
            print("Error1: ")
            print(e)
            pass

except Exception as e:
    print("Error2: ")
    print(e)
