import urllib.request

url = 'https://www.pudim.com.br'
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request(url, headers=headers)

try:
    site = urllib.request.urlopen(req)
except urllib.error.URLError:
    print(f'O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')

# site.read() captura todo o código do site!!!
