# MercadoLibre Price Tracker 📉🔔

Un script de automatización desarrollado en Python que monitorea el precio de productos en MercadoLibre Argentina en tiempo real. El sistema extrae la información del producto y envía una notificación automática por correo electrónico si el precio baja del objetivo establecido.

Este proyecto demuestra habilidades en **Web Scraping**, **Automatización de Tareas** y manejo de **Variables de Entorno** para seguridad.

## ✨ Características

* **Scraping Eficiente:** Extracción precisa de título y precio utilizando `BeautifulSoup4`.
* **Evasión de Bloqueos:** Implementación de Headers HTTP rotativos y User-Agents para evitar errores 429 (Too Many Requests).
* **Lógica de Negocio:** Comparación automática entre el precio actual y el presupuesto definido.
* **Sistema de Notificaciones:** Envío de alertas por email usando el protocolo SMTP de Gmail con soporte para caracteres especiales (UTF-8).
* **Seguridad:** Manejo de credenciales sensibles mediante variables de entorno (`.env`), evitando exponer contraseñas en el código fuente.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Peticiones HTTP:** Requests
* **Parsing HTML:** BeautifulSoup4
* **Gestión de Entorno:** Python-Dotenv
* **Correos:** Smtplib & Email.mime

## ⚙️ Instalación y Configuración

Sigue estos pasos para ejecutar el rastreador en tu entorno local:

### 1. Clonar el repositorio

```bash
git clone [https://github.com/ryakimovicz/ml-price-tracker.git](https://github.com/ryakimovicz/ml-price-tracker.git)
cd ml-price-tracker
```

### 2. Crear y activar el entorno virtual

**En Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configuración de Secretos (.env)

Este proyecto utiliza variables de entorno para proteger las credenciales de correo. Debes crear un archivo llamado `.env` en la raíz del proyecto (junto a `scraper.py`) y agregar el siguiente contenido:

```text
EMAIL_USER=tu_correo@gmail.com
EMAIL_PASS=tu_contraseña_de_aplicacion
EMAIL_TO=correo_destino@gmail.com
```

> **Nota:** Para `EMAIL_PASS`, no uses tu contraseña normal de Gmail. Debes generar una **Contraseña de Aplicación** desde la configuración de seguridad de tu cuenta de Google (Verificación en 2 pasos > Contraseñas de aplicaciones).

## 🚀 Uso

1.  Abre el archivo `scraper.py`.
2.  Modifica la variable `URL` con el enlace del producto de MercadoLibre que deseas rastrear.
3.  Establece tu precio máximo en la variable `TARGET_PRICE`.
4.  Ejecuta el script:

```bash
python scraper.py
```

Si el precio del producto es menor a tu objetivo, recibirás un correo electrónico con el enlace de compra.

## ⚠️ Disclaimer

Este proyecto fue creado con fines **educativos** para aprender sobre la extracción de datos web y la automatización con Python. Úsalo de manera responsable y respeta los términos de servicio de los sitios web que visites. No configures el script para realizar peticiones masivas en cortos periodos de tiempo.

---
**Autor:** Román Yakimovicz  
Desarrollado como parte de mi portfolio de programación.

💼 **LinkedIn:** [linkedin.com/in/ryakimovicz](https://www.linkedin.com/in/ryakimovicz/)  
🐙 **GitHub:** [@ryakimovicz](https://github.com/ryakimovicz)  
📧 **Email:** [ryakimovicz@gmail.com](mailto:ryakimovicz@gmail.com)