"""Caso de prueba de navegación y verificación del catálogo."""

from pages.inventory_page import InventoryPage


def test_catalogo(sesion_iniciada):
    """Verifica título, presencia de productos y elementos principales."""
    inventario = InventoryPage(sesion_iniciada)

    assert inventario.obtener_titulo() == "Products"
    assert len(inventario.obtener_productos()) > 0, "No hay productos visibles."
    assert inventario.elementos_principales_visibles(), "Falta un elemento clave."

    nombre, precio = inventario.obtener_nombre_precio_primer_producto()
    assert nombre != "", "El nombre del primer producto está vacío."
    assert precio.startswith("$"), "El precio no tiene el formato esperado."