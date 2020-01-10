# SenConDom
Repositorio del proyecto de embebidos 2019-3, cuya temática principal es domótica; a continuación se ve el planteamiento de la temática específica del proyecto.

## Matriz de abstracción del proyecto
|  |Es|Hizo|Puede|Hará|Podría|Haría|
|--|--|--|--|--|--|--|
|Quién|consumidor promedio con acceso a Internet.| |Hogares familiares e industrias.| |Entidades gubernamentales, grandes empresas.|Personas o industrias que busquen disminuir riesgos por mal funcionamiento de infraestructura|
|Qué|Sistema contra fugas y fallas de los servicios públicos (agua, gas y electricidad)|Implementación de modos correctivos contra incendios provocados por fallas de servicios públicos. La utilización de interruptores termomagnéticos(tacos) para interrumpir el flujo eléctrico cuando existe un corto en la infraestructura eléctrica.|Sensar y mostrar el consumo e irregularidades en el mismo, en los servicios públicos. Controlar dichos servicios para dismunuir las perdidas y el consumo. |proteger conponente físico y humano en un espacio cerrado por medio de IOT.| | |
|Dónde|Hogares, inmobiliarias y empresas pequeñas.|En edificios inteligentes| | | | |
|Cuándo| |Desde 1995 se empezó la implementación de detectores de incendios.| | | | |
|Por qué|Buscar autonomia en labores automatizables con el acceso tecnológico moderno, disminuyendo posible riesgo principalmente a las personas que se hallen dentro de estos espacios, además de aumentar la comodidad de los usuarios en cuanto a la accesibilidad del servicio.| | |Buscar una constante mejora en la seguridad contra accidentes y disminuir el componente del error humano, en lo que se refiere a los servicios básicos de un hogar o una industria; esto debido a la densidad de componentes que requieren de estos servicios.| | |
|Cómo| | | |por medio de sensores y actuadores distribuidos en los diferentes puntos de suminitro de dichos servicios públicos dentro del lugar| | |

## Variables a sensar 
|Variables|tipo de variable|
|--|--|
|Agua|Análoga / Digital|
|Gas|Análoga|
|Energía|Análoga|

## Asignación de procesos
|Procesos|Componente que lo realiza|
|--|--|
|Comunicación entre tecnologías| protocolos de comunicación física (UART y SPI)|
|Sensores y actuadores|Microcontrolador|
|Comunicación inhalambrica con sensores y actuadores|Microcontrolador|
|Recopilación de datos|Microcontrolador|
|Preprocesamiento de datos|FPGA|
|Almacenamiento de datos fuera de internet|FPGA|
|Procesamiento de datos|Raspberry Pi|
|Comunicación con la base de datos|Raspberry Pi|
|GUI|Cloud|
|Capacidad de control desde el usuario|Aplicativo web|

# Anteproyecto
**Sistemas embebidos
Universidad Nacional de Colombia**
## Titulo

## Planteamiento del problema
A causa del deficiente manejo humano, deterioro o mal uso de los materiales en donde haya intalaciones de servicios públicos básicos (agua, energía y gas); se pueden presentar fugas que se ven reflejadas en gastos adicionales, marcados en las facturas. De no ser atendidas pueden generar un mayor impacto sea en la infraestructura física (con incendios o inundaciones), y/o en el componente humano (con intoxicaciones por gas propano o electrocuciones).

## Antecedentes
Uso de tacos, alarmas, sensores

## Justificación
Debido a la concurrencia de fugas  en diferentes predios, se hace urgente crear un sistema que detecte a mayor prontitud la aparición de la fuga, la alerta sobre la misma y su desviación dada por el bloqueo inmediato del servicio local o globalmente, para prevenir impactos negativos. 

## Objetivos
### Objetivo General
Diseñar un sistema embebido usando IOT, que controle el estado del servicio por medio de sensores y actuadores, para solucionar en el menor tiempo posible la fuga existente.

### Objetivos específicos
- Sensar el flujo de cada uno de los servicios
- Controlar por medio de adactadores el estado de los servicios.
- Permitir la capacidad de control de manera remota acorde con el interes del usuario.
- Permitir la visualización del consumo del servicio para el usuario a través de gráficas.

## Alcances y límites
### Alcances
- Prototipo demostrativo funcional.
- Sensado sobre el consumo de un servicio.
- Control sobre el estado de un servicio (ON/OFF).
- Comunicación vía WiFi en 2,4 GHz.
- Almacenamiento de datos de sensado en la nube.
- Visualizacion representativa de datos, de sensado y estado del servicio, desde una aplicación web/movil.
- Almacenamineto local de datos preprocesados.
- Capacidad de control por parte del usuario desde el aplicativo.

### Límites
- Uso de sólo un sensor de cada tipo (sensor de flujo, sensor de tensión, sensor de gas y sensor de presencia), de manera que se pueda observar el funcionamiento del sistema.
- Uso de sólo un actuador por servicio (agua, luz y gas).
- Conexión permanente a internet.
- Dependencia a la estabilidad de la red electrica.
- Sólo un sensor se comunicará vía WiFi.
- La FPGA y el microcontrolador actuarán como esclavos de la Raspberry Pi.
- Únicamente la Raspberry Pi manejará la comunicación con la nube.
- Sensado NRT (near real time) con una latencia de alrededor de 15 segundos.
- La capacidad de control no es gradual.

## Vigilancia tecnológica 
### Aliados

### Competencia

## Cronograma

## Presupuesto

##
