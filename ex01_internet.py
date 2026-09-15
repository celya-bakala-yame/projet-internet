import urllib.request
from html.parser import HTMLParser
firefox = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'

req = urllib.request.Request('https://www.example.com/')
# Customize the default User-Agent header value:
req.add_header('User-Agent', firefox)
r = urllib.request.urlopen(req)

parser = HTMLParser()

class MyHTMLParser(HTMLParser):

        def __init__(self):
            super().__init__()
        def handle_starttag(self, tag, attrs):
            print("<< Trouvé balise ouvrante :", tag)
        def handle_endtag(self, tag):
            print(">> Trouvé balise fermante :", tag)
        def handle_data(self, data):
            if data.strip(): print("    Trouvé contenu  :", data)
            
            
class IMDBParser(HTMLParser):
    # Votre classe ici
    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

def scrap_imdb(html_data):
    """
    Extrait la liste de film contenue dans html_data.

    Args:
        html_data: source de la page html

    Returns:
        Liste de films
    """
    # Votre code ici...
    parser = IMDBParser()
    parser.feed(html_data)

    return parser.movies
    l = [line for line in html_data if 'titleColumn' in line]
    l = []
    return l
    
        
def main():
    """
    >>> with open("IMDb.html", mode='r', encoding='utf8') as f: html_data = f.read()
    >>> movies =  scrap_imdb(html_data)
    >>> for m in movies[:5]: print(m)
    Les évadés
    Le parrain
    The Dark Knight: Le chevalier noir
    Le parrain, 2ème partie
    12 hommes en colère
    >>> for m in movies[-5:]: print(m)
    Aladdin
    La couleur des sentiments
    La Belle et la Bête
    Du rififi chez les hommes
    Danse avec les loups
    """
    # Votre code ici...
    
    url = 'http://www.imdb.com/chart/top?ref_=nv_ch_250_4'
    try:
        html_data = ""
    except IOError:
        pass
    
    movies =  scrap_imdb(html_data)
    
    # print reversed list of movies
    
    return None

if __name__ == '__main__':
    main()