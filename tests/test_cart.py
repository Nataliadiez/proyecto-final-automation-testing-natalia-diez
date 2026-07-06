"""Caso de prueba de agregar un producto al carrito."""

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_agregar_producto_al_carrito(sesion_iniciada):
    """Verifica que el producto agregado aparece en el carrito con contador en 1."""
    inventario = InventoryPage(sesion_iniciada)

    nombre = inventario.agregar_primer_producto()
    assert inventario.obtener_contador_carrito() == "1", "El contador no muestra 1."

    inventario.ir_al_carrito()
    carrito = CartPage(sesion_iniciada)
    assert carrito.obtener_nombre_producto() == nombre, "El producto no coincide."