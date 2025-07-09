import requests
from bs4 import BeautifulSoup

# URL da página de login
LOGIN_URL = 'https://cookieprovider.sicredi.com.br/siteminderagent/forms/login.fcc?TYPE=33554433&REALMOID=06-000835a4-e4c3-1697-b564-4251ac13e084&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-YJ%2fdswk1EMKrtcbb1mZQURgRPql3b1WPRZlDA6ZXd77tkrKeEbRESEyIscAeacQV&TARGET=-SM-https%3a%2f%2fcookieprovider%2esicredi%2ecom%2ebr%2f'

def get_access_token(username, password):
    with requests.Session() as session:
        # Faz uma requisição GET para obter a página de login e os cookies de sessão
        response = session.get(LOGIN_URL)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extrai os campos ocultos necessários para o login (se houver)
        # Estes campos podem variar, então é importante inspecionar a página
        payload = {
            'USER': username,
            'PASSWORD': password,
            # Adicione outros campos ocultos se necessário, como 'SMENC', 'SMLOCALE', etc.
            # Exemplo: 'SMENC': soup.find('input', {'name': 'SMENC'})['value']
        }

        # Envia a requisição POST com as credenciais
        # A URL para o POST pode ser a mesma do GET ou uma diferente, dependendo do formulário
        # Para este caso, vamos assumir que é a mesma URL, mas pode ser necessário ajustar
        post_response = session.post(LOGIN_URL, data=payload)

        # Após o login, o access token pode estar em:
        # 1. Cookies da sessão (verifique session.cookies)
        # 2. Redirecionamento para uma URL com o token (verifique post_response.url)
        # 3. Corpo da resposta HTML/JSON (analise post_response.content)

        # Exemplo: Se o token estiver em um cookie chamado 'access_token'
        access_token = session.cookies.get('access_token')
        if access_token:
            return access_token

        # Exemplo: Se o token estiver no corpo da resposta (JSON ou HTML)
        # Pode ser necessário analisar o HTML/JSON para encontrar o token
        # print(post_response.text) # Descomente para inspecionar a resposta

        return None

# Exemplo de uso (substitua com suas credenciais reais)
# username = 'seu_usuario'
# password = 'sua_senha'
# token = get_access_token(username, password)
# if token:
#     print(f'Access Token: {token}')
# else:
#     print('Não foi possível obter o access token.')


