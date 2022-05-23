from html2image import Html2Image
import index
import diferenca
import requests


aux = index.lista
lista = list(aux.keys())
hti = Html2Image(custom_flags=['--virtual-time-budget=15000', '--hide-scrollbars'])
hti.size = (1500, 3200)
hti.output_path = 'img'
SevErro = "is a darknet gateway or Tor2Web"

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36'
    }
    for x in lista:
        url = aux[x]
        site = url["site"]
        try:
            response = requests.get(site, headers=headers)
            if SevErro not in response.text:
                hti.screenshot(url=site, save_as=str(x) + ".png")
                diff = diferenca.diff("img/"+x+".png", "img/"+x+"_base.png")
                if diff > 0.001:
                    print(diff)
        except Exception as e:
            print("Error: ")
            print(e)
            pass

except Exception as e:
    print("Error: ")
    print(e)
