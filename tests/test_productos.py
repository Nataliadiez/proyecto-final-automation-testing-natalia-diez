""" 
Interacción con Productos: (Clase 8)

Caso de Prueba de Carrito:
Añadir un producto al carrito haciendo clic en el botón correspondiente.
Verificar que el contador del carrito se incremente correctamente.
Navegar al carrito de compras.
Comprobar que el producto añadido aparezca correctamente en el carrito.

Criterios mínimos:
Agrega primer producto.
Verifica ítem en carrito.
"""

from utils.driver import setup_driver
from utils.login import login_saucedemo
from utils.carrito import (
    agregar_primer_producto_al_carrito,
    validar_contador_carrito,
    navegar_al_carrito,
    validar_producto_en_carrito
)
from utils.config import USUARIO_VALIDO, PASSWORD_VALIDO


def test_agregar_producto_al_carrito():
    """Verifica que se pueda agregar un producto al carrito correctamente."""

    # Inicializar el driver
    driver = setup_driver()

    try:
        # Iniciar sesión con credenciales válidas
        login_saucedemo(
            driver,
            USUARIO_VALIDO,
            PASSWORD_VALIDO
        )

        # Agregar el primer producto del catálogo al carrito
        nombre_producto = agregar_primer_producto_al_carrito(driver)

        # Verificar que el contador del carrito muestre 1
        badge = validar_contador_carrito(driver, "1")

        # Navegar al carrito de compras
        navegar_al_carrito(driver)

        # Verificar que el producto agregado aparezca en el carrito
        producto_en_carrito = validar_producto_en_carrito(driver, nombre_producto)

        print(f"Producto agregado al carrito: {nombre_producto}")
        print(f"Contador del carrito OK: {badge}")
        print(f"Producto visible en carrito: {producto_en_carrito}")

    finally:
        # Cerrar el navegador al finalizar la prueba
        print("Cerrando el navegador.")
        driver.quit()