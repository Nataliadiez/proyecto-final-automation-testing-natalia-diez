"""Caso de prueba del flujo completo de compra (checkout)."""

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_completo(sesion_iniciada):
    """Verifica el flujo end-to-end: agregar producto, comprar y confirmar."""
    inventario = InventoryPage(sesion_iniciada)
    inventario.agregar_primer_producto()
    inventario.ir_al_carrito()

    CartPage(sesion_iniciada).ir_al_checkout()

    checkout = CheckoutPage(sesion_iniciada)
    checkout.completar_datos("Natalia", "Diez", "1704")
    checkout.finalizar_compra()

    mensaje = checkout.obtener_mensaje_confirmacion()
    assert mensaje == "Thank you for your order!", f"Mensaje inesperado: {mensaje}"