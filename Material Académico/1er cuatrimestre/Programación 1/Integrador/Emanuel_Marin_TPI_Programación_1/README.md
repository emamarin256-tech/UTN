# Sistema de Control de Inventario

Proyecto académico desarrollado en **Python** para gestionar el inventario de herramientas de una ferretería. Permite registrar herramientas, consultar existencias, identificar productos agotados y actualizar el stock mediante ventas o ingresos de mercadería.

El sistema utiliza un menú interactivo y funciones independientes para organizar las operaciones, incorporando validaciones de datos y manejo de errores para garantizar un funcionamiento adecuado.

## Funcionalidades

El programa cuenta con las siguientes opciones:

1. **Cargar herramientas:** permite registrar varias herramientas junto con sus existencias iniciales.
2. **Mostrar inventario:** muestra todas las herramientas registradas y sus cantidades disponibles.
3. **Consultar stock:** busca una herramienta por su nombre e informa las unidades disponibles.
4. **Mostrar herramientas agotadas:** identifica y muestra las herramientas cuyo stock es igual a cero.
5. **Agregar una herramienta:** incorpora un nuevo producto al inventario con su stock inicial.
6. **Actualizar existencias:** permite registrar ventas o ingresos de mercadería y actualizar las cantidades correspondientes.
7. **Salir:** finaliza la ejecución del programa.

## Tecnologías utilizadas

- **Lenguaje:** Python 3.13.2.
- **Entorno de desarrollo:** Visual Studio Code 1.143.1.

No requiere la instalación de bibliotecas externas.

## Características de implementación

- **Estructuras de datos:** utiliza una lista de diccionarios para almacenar las herramientas y sus cantidades.
- **Modularización:** organiza las operaciones mediante funciones independientes, evitando concentrar toda la lógica en un único bloque de código.
- **Validaciones:** controla nombres vacíos o duplicados, cantidades negativas y movimientos inválidos.
- **Manejo de errores:** utiliza `try`, `except` y `raise` para detectar y gestionar entradas incorrectas.
- **Control de existencias:** impide realizar ventas que superen el stock disponible.
- **Búsquedas:** permite localizar herramientas sin distinguir entre mayúsculas y minúsculas.

## Requisitos y ejecución

Para ejecutar el programa se necesita tener Python instalado.

1. Clonar o descargar este repositorio.
2. Abrir la carpeta **"docs"** del proyecto en Visual Studio Code o en una terminal.
3. Ejecutar el archivo principal con el siguiente comando:

```bash
python Emanuel_Marin_TPI_Programación_1_Sistema_de_Control_de_Inventario.py
```

Reemplazar `Emanuel_Marin_TPI_Programación_1_Sistema_de_Control_de_Inventario.py` por el nombre del archivo Python que contiene el programa.

Una vez iniciado, se mostrará el menú principal desde el cual se podrán seleccionar las distintas operaciones.

## Almacenamiento de datos

El inventario se almacena temporalmente en memoria mediante una lista de diccionarios.

Los registros permanecen disponibles durante la ejecución del programa. Al finalizar, los datos se pierden, ya que el proyecto no contempla almacenamiento permanente en archivos ni bases de datos.

## Material complementario

🎥 **Video demostrativo del proyecto:** [[Emanuel Ignacio Marin TPI Programación 1](https://youtu.be/CPYLAnOnZrk?si=G06WLDx3dyZNiSXw)]

📚 **Documentación del proyecto (PDF):** [[Emanuel_Marin_TPI_Programación_1_Informe_de_diseño_y_fundamentación.pdf](https://github.com/emamarin256-tech/Emanuel_Ignacio_Marin_TPI_Programacion_1/blob/main/docs/Emanuel_Marin_TPI_Programaci%C3%B3n_1_Informe_de_dise%C3%B1o_y_fundamentaci%C3%B3n.pdf)]

## Autor

Emanuel Marin

**Trabajo Práctico Integrador — Programación 1**
