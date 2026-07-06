# Proyecto Final — Automation Testing

Framework de automatización de pruebas desarrollado como Trabajo Final Integrador
del curso **Automation Testing** de Talento Tech (Gobierno de la Ciudad de Buenos Aires).

Combina **pruebas de UI** (Selenium WebDriver sobre SauceDemo) y **pruebas de API**
(requests sobre JSONPlaceholder), aplicando el patrón **Page Object Model** y
generando reportes HTML.

## Tecnologías

- **Python** como lenguaje principal
- **Pytest** como framework de testing
- **Selenium WebDriver** para las pruebas de interfaz
- **Requests** para las pruebas de API
- **pytest-html** para los reportes
- **Git / GitHub** para el control de versiones

## Estructura del proyecto

```
proyecto-final/
│
├── pages/                  # Page Objects (patrón POM)
│   ├── base_page.py        # Comportamiento común: esperas, clicks, escritura
│   ├── login_page.py       # Página de login
│   ├── inventory_page.py   # Catálogo de productos
│   ├── cart_page.py        # Carrito
│   └── checkout_page.py    # Flujo de compra
│
├── tests/                  # Casos de prueba
│   ├── test_login.py       # Login exitoso + negativos (parametrizados)
│   ├── test_inventory.py   # Navegación y catálogo
│   ├── test_cart.py        # Agregar producto al carrito
│   ├── test_checkout.py    # Flujo completo de compra
│   └── test_api.py         # API pública (GET / POST / DELETE)
│
├── utils/
│   └── config.py           # URLs y credenciales centralizadas
│
├── data/
│   └── usuarios.json        # Datos externos para parametrizar el login
│
├── reports/                # Reportes HTML y capturas de fallos
│
├── conftest.py             # Fixtures (driver, sesión) y captura en fallos
├── pytest.ini              # Configuración de pytest y reportes
├── requirements.txt
└── README.md
```

## Instalación

Se recomienda usar un entorno virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate

pip install -r requirements.txt
```

> **Nota:** desde Selenium 4.6, no hace falta descargar `chromedriver` manualmente.
> Selenium Manager detecta y gestiona el driver automáticamente. Solo se necesita
> tener **Google Chrome** instalado.

## Ejecución

Correr toda la suite (UI + API), con reporte HTML:

```bash
pytest
```

Correr un archivo puntual:

```bash
pytest tests/test_login.py
```

Correr sin abrir la ventana del navegador (modo headless):

```bash
pytest --headless
```

## Reportes

Al finalizar, se genera un reporte HTML en:

```
reports/report.html
```

El reporte muestra cada test, su estado (pasado/fallado) y su duración.
Cuando un test de UI **falla**, se guarda automáticamente una captura de pantalla
en `reports/` con el formato `FALLO_<nombre_del_test>_<fecha_hora>.png`, y se
adjunta al reporte HTML para facilitar el diagnóstico.

## Casos de prueba

### UI (Selenium) — 8 ejecuciones

| Caso | Tipo | Descripción |
|------|------|-------------|
| `test_login_exitoso` | Positivo | Login con credenciales válidas → redirige al inventario |
| `test_login_invalido` | Negativo (x4) | Credenciales inválidas, vacías y usuario bloqueado → muestra el error esperado |
| `test_catalogo` | Positivo | Verifica título, presencia de productos y elementos de la interfaz |
| `test_agregar_producto_al_carrito` | Positivo | Agrega un producto y valida el contador y su presencia en el carrito |
| `test_checkout_completo` | Positivo | Flujo end-to-end: agregar producto, comprar y confirmar |

Los casos negativos se leen desde `data/usuarios.json` (fuente externa) y se ejecutan
mediante **parametrización**: cada set de datos corre como un test independiente.

### API (requests) — 4 casos

| Caso | Método | Validación |
|------|--------|------------|
| `test_get_post_existente` | GET | Código 200 y estructura del JSON |
| `test_post_crear_recurso` | POST | Código 201 y recurso creado |
| `test_delete_recurso` | DELETE | Código 200 |
| `test_flujo_crear_y_usar_id` | POST | Encadenamiento: crear un recurso y reutilizar su id |

## Sitio y API bajo prueba

- **UI:** [SauceDemo](https://www.saucedemo.com) — aplicación demo para prácticas de automatización.
- **API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com) — API pública de prueba.

