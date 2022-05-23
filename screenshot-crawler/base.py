import index
import requests
from html2image import Html2Image

hti = Html2Image(custom_flags=['--virtual-time-budget=10000', '--hide-scrollbars'])
hti.size = (1500, 3200)
hti.output_path = 'img'

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
            response = requests.get(url["site"], headers=headers)
            if SevErro not in response.text:
                tamanho = (len(response.content))
                print(x)
                print(url["site"])
                print("--------")
                hti.screenshot(url=url["site"], save_as=x+"_base.png")

        except Exception as e:
            print("Error: ")
            print(e)
            pass

except Exception as e:
    print("Error: ")
    print(e)
