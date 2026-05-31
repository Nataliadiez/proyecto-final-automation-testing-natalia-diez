from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.catalogo import validar_presencia_productos


def agregar_primer_producto_al_carrito(driver):
    """Agrega el primer producto visible del catálogo al carrito."""

    # Obtener todos los productos visibles del inventario
    productos = validar_presencia_productos(driver)

    # Seleccionar el primer producto de la lista
    primer_producto = productos[0]

    # Guardar el nombre del producto antes de agregarlo al carrito
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Hacer clic en el botón Add to cart del primer producto
    primer_producto.find_element(By.TAG_NAME, "button").click()

    return nombre_producto


def validar_contador_carrito(driver, cantidad_esperada):
    """Valida que el contador del carrito muestre la cantidad esperada."""

    # Esperar explícitamente a que aparezca el badge del carrito
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    # Validar que el contador tenga el valor esperado
    assert badge.text == cantidad_esperada, (
        f"El contador esperado era {cantidad_esperada}, pero se obtuvo {badge.text}."
    )

    return badge.text


def navegar_al_carrito(driver):
    """Navega a la página del carrito de compras."""

    # Hacer clic en el ícono del carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


def validar_producto_en_carrito(driver, nombre_producto_esperado):
    """Valida que el producto agregado aparezca correctamente en el carrito."""

    # Esperar explícitamente a que aparezca un producto en el carrito
    producto_en_carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text

    # Comparar el producto del carrito con el producto agregado
    assert producto_en_carrito == nombre_producto_esperado, (
        f"El producto esperado era '{nombre_producto_esperado}', pero se obtuvo '{producto_en_carrito}'."
    )

    return producto_en_carrito