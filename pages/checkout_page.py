"""Page Object del flujo de checkout (compra) de SauceDemo."""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Representa el proceso de compra y sus acciones."""

    CAMPO_NOMBRE = (By.ID, "first-name")
    CAMPO_APELLIDO = (By.ID, "last-name")
    CAMPO_CODIGO_POSTAL = (By.ID, "postal-code")
    BOTON_CONTINUAR = (By.ID, "continue")
    BOTON_FINALIZAR = (By.ID, "finish")
    MENSAJE_CONFIRMACION = (By.CLASS_NAME, "complete-header")

    def completar_datos(self, nombre, apellido, codigo_postal):
        """Completa el formulario de datos del comprador y continúa."""
        self.escribir(self.CAMPO_NOMBRE, nombre)
        self.escribir(self.CAMPO_APELLIDO, apellido)
        self.escribir(self.CAMPO_CODIGO_POSTAL, codigo_postal)
        self.clickear(self.BOTON_CONTINUAR)

    def finalizar_compra(self):
        """Confirma la compra en el paso de resumen."""
        self.clickear(self.BOTON_FINALIZAR)

    def obtener_mensaje_confirmacion(self):
        """Devuelve el mensaje final (esperado: 'Thank you for your order!')."""
        return self.obtener_texto(self.MENSAJE_CONFIRMACION)