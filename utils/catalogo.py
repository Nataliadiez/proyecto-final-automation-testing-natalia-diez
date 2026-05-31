from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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