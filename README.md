# Objetivo
Este codigo python tem como objetivo construir um crawler para visitar o site  epocacosmeticos.com.br e salvar um arquivo .csv com o nomedo produto, 
o título e a url.

Linguagem de programação utilizada : Python 3.6.4

# Explicações
Funçao que vai extrair o conteúde de uma página html
e que mande o BeautifulSoup pesquisar a primeira tag title que tenha um texto contido 

<pre>def extract_title(content):
    soup = BeautifulSoup(content, "xml")
    tag = soup.find("title", text=True) 

    if not tag:
        return None
    return tag.string.strip()</ pre>
    
    
    A segunda função a ser criada vai extrair os links do conteúdo da pagina e procurar a tag 'a' em que 
    href seje verdadeiro, e se iniciando com http serão incluidas aos links
    
    def extract_links(content):
    soup = BeautifulSoup(content, "xml")
    links = set()

    for tag in soup.find_all("a", href=True):
        if tag["href"].startswith("http"):
            links.add(tag["href"])

    return links
    
    # Módulos 
    BeautifulSoup: Faz pesquisas em páginas html 
    
    Requests: Baixa o código de uma página pela função "get"
