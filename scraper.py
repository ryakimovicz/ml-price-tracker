import requests
from bs4 import BeautifulSoup
import smtplib
import os
import sys
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --- FIX PARA WINDOWS (Caracteres raros en consola) ---
# Fuerza a la terminal a usar UTF-8 para poder imprimir emojis y tildes
sys.stdout.reconfigure(encoding='utf-8')

# Cargar variables de entorno
load_dotenv()

# --- Configuración ---

URL = 'https://www.mercadolibre.com.ar/sony-playstation-5-slim-1tb-standard-bundle-astro-bot-y-gran-turismo-7/p/MLA53197633'
TARGET_PRICE = 1599999

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "es-AR,es;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com/"
}

# Datos del correo (vienen del archivo .env)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

# --- Lógica del Scraper ---

def send_email(product_title, product_price, product_url):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()  # Encriptar conexión
        server.ehlo()
        
        server.login(EMAIL_USER, EMAIL_PASS)
        
        # Crear mensaje con soporte UTF-8
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_TO
        msg['Subject'] = f"¡BAJO DE PRECIO! {product_title}"
        
        body = f"El producto bajo a ${product_price:,.2f}.\n\nCompralo aqui: {product_url}"
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        server.send_message(msg)
        print("📧 Email enviado exitosamente!")
        
        server.quit()
    except Exception as e:
        print(f"❌ Error enviando email: {e}")

def check_price():
    try:
        # Timeout para evitar que se cuelgue si internet anda mal
        page = requests.get(URL, headers=HEADERS, timeout=10)

        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            
            # Obtener Título
            title_tag = soup.find('h1', class_='ui-pdp-title')
            if title_tag:
                title = title_tag.get_text()
                print(f"Producto: {title.strip()}")
            else:
                # Debugging: Si falla, guarda el HTML para ver qué pasó (puede ser captcha)
                with open("debug_error.html", "w", encoding="utf-8") as f:
                    f.write(soup.prettify())
                print("Error: No se encontró el título. Revisa el archivo 'debug_error.html' generado.")
                return
            
            # Obtener Precio
            price_container = soup.find('div', class_='ui-pdp-price__second-line')
            
            if price_container:
                price_text = price_container.find('span', class_='andes-money-amount__fraction').get_text()
                price = float(price_text.replace('.', '').replace(',', '.'))
                
                print(f"Precio: ${price:,.2f}")
                
                # Comparar con Presupuesto
                if price < TARGET_PRICE:
                    print("¡ALERTA! El precio ha bajado del objetivo.")
                    send_email(title.strip(), price, URL)
                else:
                    print("El precio sigue alto. A esperar.")
            else:
                print("Error: No se encontró el contenedor del precio")
        else:
            print(f"Error: Status code {page.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

# --- Ejecución ---

if __name__ == "__main__":
    check_price()