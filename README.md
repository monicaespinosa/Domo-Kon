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
|GUI||
