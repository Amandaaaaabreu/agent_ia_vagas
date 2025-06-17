# src/fontes/remotar.py

import requests
from bs4 import BeautifulSoup

def buscar_vagas_remotar():
    print("🔎 Buscando vagas no Remotar...")
    url = "https://remotar.com.br/search/jobs?q=qa"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
    except Exception as e:
        print(f"⚠️ Erro na requisição: {e}")
        return []

    if response.status_code != 200:
        print(f"⚠️ Erro {response.status_code} ao acessar o site da Remotar.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    vagas = []

    for vaga in soup.select('.job-list .job-card'):
        titulo = vaga.select_one('.job-title')
        empresa = vaga.select_one('.job-company')
        link_tag = vaga.find('a', href=True)

        if titulo and empresa and link_tag:
            vagas.append({
                'titulo': titulo.text.strip(),
                'empresa': empresa.text.strip(),
                'link': "https://remotar.com.br" + link_tag['href']
            })

    return vagas
