"""Fixtures y hooks compartidos por todos los tests.

conftest.py es un archivo especial de pytest: lo que se define acá queda
disponible en todos los tests automáticamente, sin necesidad de importarlo.
"""
import os
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.config import USUARIO_VALIDO, PASSWORD_VALIDO


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

@pytest.fixture
def sesion_iniciada(driver):
    """Devuelve un driver ya logueado en el inventario de SauceDemo.

    Evita repetir el login en cada test de catálogo, carrito y checkout.
    """
    login = LoginPage(driver)
    login.abrir()
    login.iniciar_sesion(USUARIO_VALIDO, PASSWORD_VALIDO)
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura un screenshot automáticamente cuando un test falla.

    Este hook corre en cada fase del test. Si la fase de ejecución ('call')
    termina en fallo y el test usó el fixture 'driver', se guarda una imagen
    con fecha/hora y nombre del test en la carpeta reports/, y se adjunta al
    reporte HTML si pytest-html está disponible.
    """
    outcome = yield
    reporte = outcome.get_result()

    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            os.makedirs("reports", exist_ok=True)
            marca_tiempo = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"reports/FALLO_{item.name}_{marca_tiempo}.png"
            driver.save_screenshot(nombre_archivo)
            print(f"\nScreenshot de fallo guardado en: {nombre_archivo}")

            # Adjuntar la captura al reporte HTML (si el plugin está presente).
            try:
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html is not None:
                    extra = getattr(reporte, "extras", [])
                    extra.append(pytest_html.extras.image(nombre_archivo))
                    reporte.extras = extra
            except Exception:
                # Si la versión de pytest-html difiere, el archivo igual queda guardado.
                pass