import lxml as lxml
from bs4 import BeautifulSoup
import requests



def extract_title(content): #conteúdo a ser examinado
    soup = BeautifulSoup(content, "xml")
    tag = soup.find("title", text=True) #Encontre a tag title desde que essa tag contenha algum texto

    if not tag: #Não encontrando retorne None, caso encontre retorne o texto dela
        return None
    return tag.string.strip()

def extract_links(content): #função que retorna todos os links presentes no conteudo de uma página
    soup = BeautifulSoup(content, "xml")
    links = set()#Não permitir elementos duplicados

    for tag in soup.find_all("a", href=True):#Retornar todas as tags 'a' que tenham o href preenchido
        if tag["href"].startswith("http"):#Se essa tag começar com http, eu a entegro aos meus links
            links.add(tag["href"])

    return links


def crawl(start_url):#recebe como parâmetro a url inicial, por onde começa a navegação
    seen_urls = set([start_url])#urls que eu já vi
    available_urls = set([start_url])#urls que existem mas não foram visitadas ainda

    while available_urls:
        url = available_urls.pop()#pego essa url do meu conjunto

        try:
            content = requests.get(url, timeout=3).text#Tento baixar o conteúdo dessa url com um tempo de 3 segundos
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