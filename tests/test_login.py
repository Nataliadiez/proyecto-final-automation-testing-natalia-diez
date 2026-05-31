"""
Automatización de Login:
Navegar a la página de login de saucedemo.com
Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
Validar login exitoso verificando que se haya redirigido a la página de inventario

Criterios mínimos:
Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”. 
"""

from utils.saucedemo_funciones import (
    setup_driver,
    login_saucedemo,
    validar_login_exitoso,
    USUARIO_VALIDO,
    PASSWORD_VALIDO
)


def test_login_exitoso():
    """Prueba el inicio de sesión exitoso en SauceDemo."""

    # Inicializar el driver
    driver = setup_driver()

    try:
        # Ejecutar login con credenciales válidas
        login_saucedemo(
            driver,
            USUARIO_VALIDO,
            PASSWORD_VALIDO
        )

        # Validar que el login fue exitoso
        titulo = validar_login_exitoso(driver)

        print("Login exitoso")
        print("Título de sección OK: ", titulo)

    finally:
        # Cerrar el navegador al finalizar la prueba
        print("Cerrando el navegador.")
        driver.quit()