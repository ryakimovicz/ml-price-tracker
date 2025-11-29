import requests
from bs4 import BeautifulSoup

URL = 'https://www.mercadolibre.com.ar/sony-playstation-5-slim-1tb-standard-bundle-astro-bot-y-gran-turismo-7/p/MLA53197633'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def check_price():
    try:
        page = requests.get(URL, headers=HEADERS)

        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            
            title = soup.find('h1', class_='ui-pdp-title').get_text()
            
            print(f"Producto: {title.strip()}")
            price_container = soup.find('div', class_='ui-pdp-price__second-line')
            
            if price_container:
                price_text = price_container.find('span', class_='andes-money-amount__fraction').get_text()
                
                price = float(price_text.replace('.', '').replace(',', '.'))
                
                print(f"Precio: ${price:,.2f}")
            else:
                print("Error: No se encontró el contenedor del precio")
        else:
            print(f"Error: Status code {page.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_price()