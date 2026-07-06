"""Casos de prueba de login: uno positivo (happy path) y varios negativos.

Los casos negativos se leen desde un archivo JSON externo (data/usuarios.json)
y se ejecutan con parametrización: cada set de datos corre como un test aparte.
"""

import json
from pathlib import Path

import pytest

from pages.login_page import LoginPage
from utils.config import USUARIO_VALIDO, PASSWORD_VALIDO, INVENTORY_URL


def cargar_credenciales_invalidas():
    """Lee los sets de credenciales inválidas desde el archivo JSON externo."""
    ruta = Path(__file__).parent.parent / "data" / "usuarios.json"
    with open(ruta, encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos["credenciales_invalidas"]


def test_login_exitoso(driver):
    """Verifica que un usuario válido es redirigido al inventario."""
    login = LoginPage(driver)
    login.abrir()
    login.iniciar_sesion(USUARIO_VALIDO, PASSWORD_VALIDO)

    assert INVENTORY_URL in login.url_actual(), "No se redirigió al inventario."


@pytest.mark.parametrize(
    "caso",
    cargar_credenciales_invalidas(),
    ids=lambda caso: caso["descripcion"],
)
def test_login_invalido(driver, caso):
    """Verifica que credenciales inválidas muestran el mensaje de error esperado."""
    login = LoginPage(driver)
    login.abrir()
    login.iniciar_sesion(caso["usuario"], caso["password"])

    assert login.obtener_mensaje_error() == caso["error_esperado"]