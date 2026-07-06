"""Clase base para todos los Page Objects.

Concentra el comportamiento común (esperas, clicks, escritura) para no
repetirlo en cada página. Cada página concreta hereda de esta clase.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Comportamiento compartido por todas las páginas del sitio."""

    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def esperar_visible(self, localizador):
        """Espera a que un elemento esté visible y lo devuelve."""
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(localizador)
        )

    def esperar_todos_visibles(self, localizador):
        """Espera a que todos los elementos que coinciden estén visibles."""
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_all_elements_located(localizador)
        )

    def escribir(self, localizador, texto):
        """Escribe texto en un campo, luego de esperarlo."""
        campo = self.esperar_visible(localizador)
        campo.clear()
        campo.send_keys(texto)

    def clickear(self, localizador):
        """Hace clic en un elemento, luego de esperar que sea clickeable."""
        elemento = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(localizador)
        )
        elemento.click()

    def obtener_texto(self, localizador):
        """Devuelve el texto visible de un elemento."""
        return self.esperar_visible(localizador).text

    def url_actual(self):
        """Devuelve la URL actual del navegador."""
        return self.driver.current_url