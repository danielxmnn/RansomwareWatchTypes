import requests  # dependency


def main(a, b, c):
    url = "https://discord.com/api/webhooks/**************************************************************************************"

    data = {"content": "\n!\n Grupo: " + a + "\n Data: " + b + "\n Vitima: " + c + ""}

    result = requests.post(url, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
