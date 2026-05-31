""" 
Navegación y Verificación del Catálogo: (Clases 6 a 8)

Caso de Prueba de Navegación:
Verificar que el título de la página de inventario sea correcto.
Comprobar que existan productos visibles en la página.
Validar que elementos importantes de la interfaz estén presentes.
Listar nombre y precio del primer producto.

Criterios mínimos:
Valida título.
Valida presencia de productos.
Lista nombre/precio del primero.
"""

from utils.driver import setup_driver
from utils.login import login_saucedemo, validar_titulo_inventario
from utils.catalogo import (
    validar_presencia_productos,
    validar_elementos_catalogo,
    obtener_nombre_precio_primer_producto
)
from utils.config import USUARIO_VALIDO, PASSWORD_VALIDO


def test_catalogo_inventario():
    """Verifica título, productos visibles y elementos principales del catálogo."""

    # Inicializar el driver
    driver = setup_driver()

    try:
        # Iniciar sesión con credenciales válidas
        login_saucedemo(
            driver,
            USUARIO_VALIDO,
            PASSWORD_VALIDO
        )

        # Validar que el título visible sea Products
        titulo = validar_titulo_inventario(driver)

        # Validar que existan productos visibles
        productos = validar_presencia_productos(driver)

        # Validar elementos importantes de la interfaz
        validar_elementos_catalogo(driver)

        # Obtener nombre y precio del primer producto
        nombre_producto, precio_producto = obtener_nombre_precio_primer_producto(driver)

        print(f"Título de catálogo OK: {titulo}")
        print(f"Se encontraron {len(productos)} productos.")
        print("Elementos principales del catálogo visibles.")
        print(f"Primer producto: {nombre_producto}")
        print(f"Precio: {precio_producto}")

    finally:
        print("Cerrando el navegador.")
        driver.quit()