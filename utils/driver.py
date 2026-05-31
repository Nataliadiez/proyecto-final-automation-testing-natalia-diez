from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Configuración del driver de Chrome
def setup_driver():
    """Configura y devuelve una instancia del WebDriver de Chrome."""

    chrome_options = Options()

    # Opcional: abre el navegador maximizado para visualizar mejor la prueba
    chrome_options.add_argument("--start-maximized")

    # Inicializar el driver de Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # Espera implícita para búsquedas generales de elementos
    driver.implicitly_wait(5)

    return driver