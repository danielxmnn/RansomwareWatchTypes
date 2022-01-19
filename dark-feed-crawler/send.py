import requests  # dependency


def main(a, b, c):
    url = "https://discord.com/api/webhooks/YOUR_WEBHOOK_KEY"

    # for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {"content": "\n!\n Grupo: " + a + "\n Data: " + b + "\n Vitima: " + c + ""}

    # leave this out if you dont want an embed
    # for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object

    result = requests.post(url, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
