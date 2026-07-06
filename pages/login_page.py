"""Page Object de la página de login de SauceDemo."""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import LOGIN_URL


class LoginPage(BasePage):
    """Representa la página de inicio de sesión y sus acciones.

    Los localizadores se definen como atributos de clase: si el sitio
    cambia un selector, se corrige en un solo lugar.
    """

    CAMPO_USUARIO = (By.ID, "user-name")
    CAMPO_PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")
    MENSAJE_ERROR = (By.CSS_SELECTOR, '[data-test="error"]')

    def abrir(self):
        """Navega a la página de login."""
        self.driver.get(LOGIN_URL)

    def iniciar_sesion(self, usuario, password):
        """Completa las credenciales y hace clic en Login."""
        self.escribir(self.CAMPO_USUARIO, usuario)
        self.escribir(self.CAMPO_PASSWORD, password)
        self.clickear(self.BOTON_LOGIN)

    def obtener_mensaje_error(self):
        """Devuelve el texto del mensaje de error mostrado tras un login fallido."""
        return self.obtener_texto(self.MENSAJE_ERROR)