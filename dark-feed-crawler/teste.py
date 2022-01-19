import requests
import hashlib


aux = 0
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36'
    }
    url = 'http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion.ly'
    response = requests.get(url, headers=headers)
    print(response.content)
    currentHash = hashlib.sha224(response).hexdigest()
    newHash = hashlib.sha224(response).hexdigest()
    if newHash == currentHash:
        aux += 1
except Exception as e:
    print("error")
