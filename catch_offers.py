import requests
from bs4 import BeautifulSoup

class CatchOffers:
    #Função para buscar o site pela URL
    def reqUrl(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        return soup

    #Função que retorna duas listas, uma contendo a URL dos jogos que estão na promoção diária, e a outra contendo a imagem do banner dos jogos que estão na promoção diária.
    def getDailyGamesOffers(self):
        gamesURL = []
        gamesIMG = []
        url = 'https://store.steampowered.com/specials?l=brazilian'
        soup = self.reqUrl(url)

        for list_games in soup.find_all('div', class_='dailydeal_cap'):
            list_g = list_games.find_all('a')
            x = str(list_g).split('"')
            gamesURL.append(x[1])
            gamesIMG.append(x[3])

        return gamesURL, gamesIMG

    #Função que retorna duas listas, uma contendo o preço original dos jogos, e a outra contendo o preço com o desconto aplicado.
    def getDailyGamesOffersPrices(self):
        gameOriginalPrice = []
        gameFinalPrice = []
        url = 'https://store.steampowered.com/specials?l=brazilian'
        soup = self.reqUrl(url)

        for list_prices in soup.find_all('div', class_='dailydeal_ctn'):
            list_p = list_prices.find_all('div', class_='discount_prices')
            x = str(list_p).split('>')
            y = x[2].split('</div')
            z = x[4].split('</div')
            gameOriginalPrice.append(y[0])
            gameFinalPrice.append(z[0])
            
        return gameOriginalPrice, gameFinalPrice

    def getSpotlightOffers(self):
        gamesURL = []
        gamesIMG = []
        url = 'https://store.steampowered.com/specials?l=brazilian'
        soup = self.reqUrl(url)

        for list_games in soup.find_all('div', class_='spotlight_img'):
            list_g = list_games.find_all('a')
            x = str(list_g).split('"')
            gamesURL.append(x[1])
            gamesIMG.append(x[7])

        return gamesURL, gamesIMG

    def getSpotlightOffersContentH2(self):
        gamesH2 = []
        url = 'https://store.steampowered.com/specials?l=brazilian'
        soup = self.reqUrl(url)

        for list_content in soup.find_all('div', class_='spotlight_content'):
            list_c = list_content.find_all('h2')
            x = str(list_c).split('>')
            y = x[1].split('</h2')
            gamesH2.append(y[0])

        return gamesH2