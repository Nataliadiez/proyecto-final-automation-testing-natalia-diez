"""Page Object de la página del carrito de SauceDemo."""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """Representa el carrito de compras y sus acciones."""

    ITEM_NOMBRE = (By.CLASS_NAME, "inventory_item_name")
    BOTON_CHECKOUT = (By.ID, "checkout")

    def obtener_nombre_producto(self):
        """Devuelve el nombre del primer producto listado en el carrito."""
        return self.obtener_texto(self.ITEM_NOMBRE)

    def ir_al_checkout(self):
        """Avanza al primer paso del checkout."""
        self.clickear(self.BOTON_CHECKOUT)