"""Page Object de la página de inventario (catálogo) de SauceDemo."""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Representa el catálogo de productos y sus acciones.

    Las páginas devuelven datos; las validaciones (asserts) viven en los
    tests. Así los Page Objects son reutilizables.
    """

    TITULO = (By.CSS_SELECTOR, "div.header_secondary_container .title")
    PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    MENU = (By.ID, "react-burger-menu-btn")
    FILTRO = (By.CLASS_NAME, "product_sort_container")
    CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
    PRECIO_PRODUCTO = (By.CLASS_NAME, "inventory_item_price")
    BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")

    def obtener_titulo(self):
        """Devuelve el título visible de la sección (esperado: 'Products')."""
        return self.obtener_texto(self.TITULO)

    def obtener_productos(self):
        """Devuelve la lista de productos visibles en el catálogo."""
        return self.esperar_todos_visibles(self.PRODUCTOS)

    def elementos_principales_visibles(self):
        """Indica si el menú, el filtro y el carrito están visibles."""
        menu = self.esperar_visible(self.MENU)
        filtro = self.esperar_visible(self.FILTRO)
        carrito = self.esperar_visible(self.CARRITO)
        return menu.is_displayed() and filtro.is_displayed() and carrito.is_displayed()

    def obtener_nombre_precio_primer_producto(self):
        """Devuelve el nombre y el precio del primer producto del catálogo."""
        primero = self.obtener_productos()[0]
        nombre = primero.find_element(*self.NOMBRE_PRODUCTO).text
        precio = primero.find_element(*self.PRECIO_PRODUCTO).text
        return nombre, precio

    def agregar_primer_producto(self):
        """Agrega el primer producto al carrito y devuelve su nombre."""
        primero = self.obtener_productos()[0]
        nombre = primero.find_element(*self.NOMBRE_PRODUCTO).text
        primero.find_element(By.TAG_NAME, "button").click()
        return nombre

    def obtener_contador_carrito(self):
        """Devuelve el texto del contador (badge) del carrito."""
        return self.obtener_texto(self.BADGE_CARRITO)

    def ir_al_carrito(self):
        """Navega a la página del carrito."""
        self.clickear(self.CARRITO)