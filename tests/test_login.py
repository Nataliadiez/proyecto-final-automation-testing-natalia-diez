"""Casos de prueba de login."""

from pages.login_page import LoginPage
from utils.config import USUARIO_VALIDO, PASSWORD_VALIDO, INVENTORY_URL


def test_login_exitoso(driver):
    """Verifica que un usuario válido es redirigido al inventario."""
    login = LoginPage(driver)
    login.abrir()
    login.iniciar_sesion(USUARIO_VALIDO, PASSWORD_VALIDO)

    assert INVENTORY_URL in login.url_actual(), "No se redirigió al inventario."