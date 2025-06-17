import requests
from bs4 import BeautifulSoup

def buscar_vagas_gupy(query='estágio'):
    url = f"https://portal.gupy.io/job-search/positions?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    cards = soup.find_all('a', class_='sc-hQhXFD')  # classe dos cards
    vagas = []

    for card in cards:
        titulo = card.find('h2').text.lower() if card.find('h2') else ''
        link = card['href']
        vagas.append({
            'titulo': titulo,
            'link': link
        })

    return vagas
