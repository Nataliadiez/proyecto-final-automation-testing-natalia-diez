"""Fixtures y hooks compartidos por todos los tests.

conftest.py es un archivo especial de pytest: lo que se define acá queda
disponible en todos los tests automáticamente, sin necesidad de importarlo.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Agrega la opción --headless para correr sin abrir la ventana del navegador."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Ejecuta Chrome en modo headless (sin interfaz gráfica).",
    )


@pytest.fixture
def driver(request):
    """Abre Chrome antes de cada test y lo cierra al terminar.

    Todo lo anterior al 'yield' es preparación (setup); lo posterior es
    limpieza (teardown). Así cada test corre aislado y no quedan
    navegadores abiertos, cumpliendo con que los tests sean
    independientes y repetibles.
    """
    opciones = Options()
    opciones.add_argument("--start-maximized")

    if request.config.getoption("--headless"):
        opciones.add_argument("--headless=new")
        opciones.add_argument("--window-size=1920,1080")

    navegador = webdriver.Chrome(options=opciones)
    yield navegador
    navegador.quit()