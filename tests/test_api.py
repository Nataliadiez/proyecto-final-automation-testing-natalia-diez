"""Casos de prueba de API pública (JSONPlaceholder) usando requests.

Cubre los métodos GET, POST y DELETE, validando códigos de estado y la
estructura del JSON devuelto. Incluye un flujo encadenado (opcional).
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def test_get_post_existente():
    """GET: obtener un post devuelve 200 y la estructura esperada."""
    respuesta = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)

    assert respuesta.status_code == 200
    cuerpo = respuesta.json()
    assert cuerpo["id"] == 1
    for clave in ("userId", "id", "title", "body"):
        assert clave in cuerpo, f"Falta la clave '{clave}' en la respuesta."


def test_post_crear_recurso():
    """POST: crear un post devuelve 201 y el recurso creado con su id."""
    nuevo = {"title": "Automation", "body": "Proyecto final", "userId": 1}
    respuesta = requests.post(f"{BASE_URL}/posts", json=nuevo, timeout=TIMEOUT)

    assert respuesta.status_code == 201
    cuerpo = respuesta.json()
    assert cuerpo["title"] == nuevo["title"]
    assert "id" in cuerpo, "La respuesta no incluye el id del recurso creado."


def test_delete_recurso():
    """DELETE: eliminar un post devuelve 200."""
    respuesta = requests.delete(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert respuesta.status_code == 200


def test_flujo_crear_y_usar_id():
    """Encadenamiento: crear un recurso y reutilizar el id que devuelve."""
    nuevo = {"title": "Encadenado", "body": "flujo dependiente", "userId": 2}
    creacion = requests.post(f"{BASE_URL}/posts", json=nuevo, timeout=TIMEOUT)
    assert creacion.status_code == 201

    id_creado = creacion.json()["id"]
    assert isinstance(id_creado, int), "El id devuelto no es un entero."