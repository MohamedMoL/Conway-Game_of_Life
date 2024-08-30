# Conway's Game of Life

Este proyecto implementa el famoso "Game of Life" de Conway utilizando Django para el backend y HTML, CSS y JavaScript para el frontend. El objetivo es proporcionar una simulación interactiva y visual del juego, que puede ser modificada y observada a través de una interfaz web.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Características](#características)
- [Instalación](#instalación)
- [Clonar repositorio](#clonar-el-repositorio)
- [Uso](#uso)

## Introducción

El "Game of Life" es un autómata celular diseñado por el matemático británico John Horton Conway en 1970. Es un juego de cero jugadores, lo que significa que su evolución está determinada por su estado inicial, sin necesidad de interacción posterior del usuario. El juego se desarrolla en una cuadrícula de celdas, donde cada celda tiene dos estados posibles: viva o muerta. El estado de las celdas evoluciona a través de iteraciones basadas en un conjunto de reglas simples.

## Características

- Interfaz de usuario amigable para visualizar y modificar el estado de la cuadrícula.
- Simulación en tiempo real de las iteraciones del juego.
- Configuración personalizada de la cuadrícula inicial.

## Instalación

Para ejecutar este proyecto, es necesario configurar el entorno con las dependencias correctas.

#### 1. Instalar Python y pip

La versión requerida de Python es la 3.11 en adelante, que se puede instalar desde su [sitio oficial](https://www.python.org/downloads/). pip se instala junto con Python automáticamente.

Para verificar que ambos se hayan instalado correctamente, ejecuta el siguiente comando en tu terminal:

```bash
python --version
pip --version
```

#### 2. Instalar Django

Una vez instalados Python y pip, ejecutar el siguiente comando para instalar Django:

```bash
pip install django
```

#### 3. Instalar Django-cors-headers

Por último, es necesario que se instale la dependencia de django "django-cors-headers" mediante el siguiente comando:

```bash
pip install django-cors-headers
```

### Clonar el repositorio

Si cumple con los requerimiento necesarios para ejecutar este proyecto, ya puede proceder a clonar el repositorio con el próximo comando:

```bash
git clone https://github.com/MohamedMoL/Conway-Game_of_Life.git
cd Conway-Game_of_Life
```

### Uso

Para finalmente hacer uso de este proyecto, debe levantar dos servidores localmente, una para la "api" y otra para la "app". Para la api, deberá ejecutar el siguiente comando, asumiendo que se encuentra en la carpeta "Conway-Game_of_Life":

Para Windows 11:

```bash
py ./api/Conway_Game_of_Life/manage.py runserver
```

Y para levantar el servidor de la "app", puede utilizar la extensión Live Server de Visual Studio Code, o similares según el IDE que utilice.
