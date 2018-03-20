import lxml as lxml
from bs4 import BeautifulSoup
import requests



def extract_title(content): #conteúdo a ser examinado
    soup = BeautifulSoup(content, "xml")
    tag = soup.find("title", text=True) 

    if not tag: 
        return None
    return tag.string.strip()

def extract_links(content): # retorna todos os links presentes no conteudo de uma página
    soup = BeautifulSoup(content, "xml")
    links = set()#Não permitir elementos duplicados

    for tag in soup.find_all("a", href=True):
        if tag["href"].startswith("http"):
            links.add(tag["href"])

    return links


def crawl(start_url):#recebe como parâmetro a url inicial, por onde começa a navegação
    seen_urls = set([start_url])#urls que eu já vi
    available_urls = set([start_url])#urls que existem mas não foram visitadas ainda

    while available_urls:
        url = available_urls.pop()

        try:
            content = requests.get(url, timeout=3).text
        except Exception:
            continue

        title = extract_title(content)

        if title:
            print('Titulo- {}'.format(title))
            print('Url- {}'.format(url))
            print()
        for link in extract_links(content):
            if link not in seen_urls:
                seen_urls.add(link)
                available_urls.add(link)
try:
    crawl('https://www.epocacosmeticos.com.br/l-oreal-professionnel-nutrifier-mascara-nutritiva/p')
except KeyboardInterrupt:
    print()
    print("Bye!")
