import requests


def verificar_site(url, timeout=5):
    try:
        resposta = requests.get(url, timeout=timeout)
        print(f'{url} está acessível (status {resposta.status_code})')
    except requests.exceptions.ConnectionError:
        print(f'{url} não está acessível (erro de conexão)')
    except requests.exceptions.Timeout:
        print(f'{url} não respondeu a tempo (timeout)')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar {url}: {e}')
    return False


verificar_site('www.pudim.com.br')
