# Batalla Naval Simplificada

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo C

Equipo: Los 404

Juego por turnos para dos jugadores, con un tablero de 4x4 y tres barcos por jugador. El objetivo es hundir los tres barcos del rival. El proyecto contará con un modo local y, posteriormente, un modo multijugador cliente-servidor en red LAN.

## Integrantes

- Ingrid Muzo
- Emilio orozco
- Luis Ñacata 

## Cómo ejecutarlo

Requiere Python 3. Desde la carpeta del repositorio, ejecutar: 
```bash
python juego.py
```

Permite acceder al menú principal del juego.

```bash
python game_logic.py
```

Permite comprobar la validación de la jugada y el fin de la partida.

## Estructura del repositorio

| Archivo | Qué hace | Estado |
|---|---|---|
| `juego.py` | Menú principal que se repite hasta seleccionar Salir. | Terminado |
| `game_logic.py` | Validación de coordenadas, disparos repetidos y determinación del ganador o empate. | Terminado |
| `server.py` | Comentario sobre las funciones que realizará el servidor (Jugador 1). | Pendiente para la Fase 4 |
| `client.py` | Comentario sobre las funciones que realizará el cliente (Jugador 2). | Pendiente para la Fase 4 |
| `diseno/` | Diagramas RAPTOR correspondientes a la Fase 2. | Agregados |

## Del diseño al código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió al traducirlo |
|---|---|---|
| DF1 Partida completa (solo el menú) | `juego.py`, líneas 1-18 | El Loop se convirtió en while y las selecciones en if, elif y else. |
| DF2 Validación de la jugada | `game_logic.py`, líneas 1-40 | Se utilizó len() para validar la longitud y while para repetir las jugadas inválidas o repetidas. Los índices comienzan desde 0 en Python. |
| DF3 Fin de la partida | `game_logic.py`, líneas 43-68 | Las selecciones se tradujeron a if, elif y else para determinar el ganador, empate o continuación de la partida. |

El bucle de turnos de la partida completa y la comunicación mediante sockets se implementarán en la Fase 4.

## Video explicativo

Enlace: https://drive.google.com/file/d/1d8ARI4lngzu4i1kTPfq4LzTcOSiKlguG/view?usp=drivesdk

En el video se demostrará el funcionamiento del menú, la validación de una jugada inválida, el fin de la partida y la traducción de los diagramas RAPTOR a Python.

## Licencia

Este proyecto se distribuye bajo la licencia MIT, una licencia de código abierto. El texto completo estará disponible en el archivo `LICENSE`.

## Declaración de autoría

Declaramos que el proyecto fue desarrollado por los integrantes del equipo Los 404, con el apoyo de las herramientas citadas en la sección Créditos. El equipo es responsable de revisar, comprender y comprobar el funcionamiento del código presentado.

## Créditos

| Recurso | Autor o fuente | Dónde se usa | Licencia |
|---|---|---|---|
| Python 3 | Python Software Foundation | Ejecución del código | PSF License |
| Plantilla README | Docente de Lógica de Programación - UIDE | Organización del README.md | Material académico, licencia no especificada |

### Uso de IA

| Herramienta | Para qué la usamos | Qué revisamos o cambiamos nosotros |
|---|---|---|
| ChatGPT (OpenAI) | Apoyo en la traducción de los diagramas a Python, generación de código y redacción del README. | Revisamos las condiciones, incorporamos el código al proyecto y realizamos pruebas de funcionamiento. |
| Claude (Anthropic) | Apoyo en el diseño inicial de los diagramas y documentación de la Fase 2. | Revisamos los diagramas y ajustamos algunas condiciones durante su elaboración en RAPTOR. |