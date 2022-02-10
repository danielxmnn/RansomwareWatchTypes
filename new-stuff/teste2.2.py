import requests
import index

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
            if SevErro in response.text:
                reserva1 = site.replace("onion.ly", "onion.ws")
                response = requests.get(reserva1, headers=headers)
            if SevErro not in response.text:
                tamanho = (len(response.content))
                print(x)
                print(site)
                print(tamanho)
                print("--------")
            else:
                print("---ERROR---")
                print(x)
                print(site)
                print("---ERROR---")
        except Exception as e:
            print("Error: ")
            print(e)
            pass

except Exception as e:
    print("Error: ")
    print(e)
