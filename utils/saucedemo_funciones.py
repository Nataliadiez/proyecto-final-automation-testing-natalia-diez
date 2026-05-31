from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Datos base del sitio
URL_LOGIN = "https://www.saucedemo.com/"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"


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


def abrir_pagina_login(driver):
    """Abre la página de login de SauceDemo."""

    driver.get(URL_LOGIN)


def esperar_formulario_login(driver):
    """Espera explícitamente a que el formulario de login esté visible."""

    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    return username_input


def completar_login(driver, usuario, password):
    """Completa los campos de usuario y contraseña."""

    # Esperar a que el campo usuario esté visible antes de escribir
    username_input = esperar_formulario_login(driver)

    # Ingresar credenciales válidas
    username_input.send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)


def hacer_click_login(driver):
    """Hace clic en el botón de login."""

    driver.find_element(By.ID, "login-button").click()


def login_saucedemo(driver, usuario, password):
    """Ejecuta el flujo completo de login en SauceDemo."""

    abrir_pagina_login(driver)
    completar_login(driver, usuario, password)
    hacer_click_login(driver)


def validar_redireccion_inventario(driver):
    """Valida que el login haya redirigido a la página de inventario."""

    # Esperar explícitamente a que la URL contenga /inventory.html
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    # Validar URL actual
    assert "/inventory.html" in driver.current_url, "No se redirigió a la página de inventario."


def validar_titulo_navegador(driver):
    """Valida que el título de la pestaña del navegador sea Swag Labs."""

    assert driver.title == "Swag Labs", f"El título esperado era 'Swag Labs', pero se obtuvo '{driver.title}'."


def validar_titulo_inventario(driver):
    """Valida que el título visible de la página de inventario sea Products."""

    # Esperar explícitamente a que el título de inventario esté visible
    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header_secondary_container .title"))
    ).text

    # Validar texto visible
    assert titulo == "Products", f"El título esperado era 'Products', pero se obtuvo '{titulo}'."

    return titulo


def validar_login_exitoso(driver):
    """Valida que el login haya sido exitoso usando URL, título del navegador y título visible."""

    validar_redireccion_inventario(driver)
    validar_titulo_navegador(driver)
    titulo = validar_titulo_inventario(driver)

    return titulo


def validar_presencia_productos(driver):
    """Valida que exista al menos un producto visible en el inventario."""

    productos = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    assert len(productos) > 0, "No se encontraron productos visibles en el inventario."

    return productos


def validar_elementos_catalogo(driver):
    """Valida que elementos importantes del catálogo estén presentes."""

    menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "react-burger-menu-btn"))
    )

    filtro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )

    carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
    )

    assert menu.is_displayed(), "El menú no está visible."
    assert filtro.is_displayed(), "El filtro no está visible."
    assert carrito.is_displayed(), "El carrito no está visible."


def obtener_nombre_precio_primer_producto(driver):
    """Obtiene el nombre y el precio del primer producto del catálogo."""

    productos = validar_presencia_productos(driver)

    primer_producto = productos[0]

    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre_producto != "", "El nombre del primer producto está vacío."
    assert precio_producto != "", "El precio del primer producto está vacío."

    return nombre_producto, precio_producto