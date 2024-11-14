# Perfilador de Desempeño para Funciones Python

Desarrolla una herramienta que cree un perfil del desempeño de funciones en Python, midiendo métricas como el uso de memoria y el tiempo de ejecución. Esto debe proporcionar informes detallados sobre dónde ocurren los cuellos de botella en el desempeño.

## Enfoque del Proyecto

### 1. **Medir el Tiempo de Ejecución**
   Utilizar las librerías `time` o `timeit` para evaluar el desempeño de las funciones. El objetivo es medir el tiempo exacto que tarda una función en ejecutarse y detectar posibles optimizaciones.

### 2. **Monitorear el Uso de Memoria**
   Usar herramientas como `tracemalloc` o `memory_profiler` para monitorear el consumo de memoria durante la ejecución de las funciones. Esto ayudará a identificar áreas en las que el código puede estar utilizando más memoria de la necesaria.

### 3. **Registro**
   Configurar el registro personalizado de los datos de desempeño. Esto incluye la creación de logs detallados con información sobre el tiempo de ejecución, el uso de memoria y otros aspectos clave del rendimiento.

Este proyecto te ayudará a comprender los cuellos de botella en el código Python existente mediante la creación de perfiles y a explorar técnicas de optimización de desempeño.

## Tecnologías Utilizadas

- **time** / **timeit**: Para medir el tiempo de ejecución de las funciones.
- **tracemalloc** / **memory_profiler**: Para monitorear el uso de memoria.
- **logging**: Para generar logs detallados con la información de desempeño.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
