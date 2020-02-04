# Domo-Kon
Repositorio del proyecto de embebidos 2019-3, cuya temática principal es domótica; a continuación se ve el planteamiento de la temática específica del proyecto.

## Matriz de abstracción del proyecto
|  |Es|Hizo|Puede|Hará|Podría|Haría|
|--|--|--|--|--|--|--|
|Quién|consumidor promedio con acceso a Internet.| |Hogares familiares e industrias.| |Entidades gubernamentales, grandes empresas.|Personas o industrias que busquen disminuir riesgos por mal funcionamiento de infraestructura|
|Qué|Sistema contra fugas y fallas de los servicios públicos (agua, gas y electricidad)|Implementación de modos correctivos contra incendios provocados por fallas de servicios públicos. La utilización de interruptores termomagnéticos(tacos) para interrumpir el flujo eléctrico cuando existe un corto en la infraestructura eléctrica.|Sensar y mostrar el consumo e irregularidades en el mismo, en los servicios públicos. Controlar dichos servicios para dismunuir las perdidas y el consumo. |proteger conponente físico y humano en un espacio cerrado por medio de IOT.| | |
|Dónde|Hogares, inmobiliarias y empresas pequeñas.|En edificios inteligentes| | | | |
|Cuándo| |Desde 1995 se empezó la implementación de detectores de incendios.| | | | |
|Por qué|Buscar autonomia en labores automatizables con el acceso tecnológico moderno, disminuyendo posible riesgo principalmente a las personas que se hallen dentro de esos espacios, además de aumentar la comodidad de los usuarios en cuanto a la accesibilidad del servicio.| | |Buscar una constante me que salio la patente comercial para el dri que salio la patente c omerciale jora en la seguridad contra accidentes y disminuir el componente del error humano, en lo que se refiere a los servicios básicos de un hogar o una industria; esto debido a la densidad de componentes que requieren de estos servicios.| | |
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
<div style="text-align: right"> A causa del deficiente manejo humano, deterioro o mal uso de los materiales en donde haya intalaciones de servicios públicos básicos (agua, energía y gas); se pueden presentar fugas que se ven reflejadas en gastos adicionales, marcados en las facturas. De no ser atendidas pueden generar un mayor impacto sea en la infraestructura física (con incendios o inundaciones), y/o en el componente humano (con intoxicaciones por gas propano o electrocuciones).</div>

## Antecedentes
Desde 1924 que salió la patente comercial para el disruptor a nombre de un grupo suizo de compañía de ingeniería eléctrica llamada Brown, Boveri & Cie, se ha implementado alguna forma de romper el flujo eléctrico en caso que existan fallas en el mismo; esta idea fue concebida originalmente por Thomas Edison  en 1879, sin embargo, en esa epoca las protecciones funcionaban por fusibles (1). La ventaja de los disruptores a diferencia de los fusibles es que estos no eran desechable despues de que se activaran las protecciónes, lo que las hacía más economicas a largo plazo, mientras que los fusibles a pesar que interrumpen el flujo electrico, estos no pueden reconstruirse despues de que han superado su límite de uso. La idea del disruptor se da más que por la necesidad de proteger a las personas de fallas en la estructura eléctrica, estops se implementarón para proteger maquinária de esas posibles fallas, de forma que la capacidad de trabajo de industrias y después el capital de las casas estuviera protegido; ésto se da principalmente porqué no se puede lograr la sensibilidad necesaria del circuito para percibir un cambio que afectara únicamente a las personas y no a la maquinaria que se hallaba conectada a la red electrica, de manera que en las protecciones contra fallas electricas existen 2 grupo grandes de disruptores los interruptores termomagnéticos, los suales se encargan de sentir las fallas de alta potencia y abrir dicho circuito; y los interruptores diferenciales los cuales rompen el flujo eléctrico cuando sienten cambios considerables de baja y media potencia en un determinado tiempo, estos son los encargados de evitar daños permanentes en las personas (2), aunque debido a su alto costo éstos sólo se impliementan en las zonas humedas.

Según el periodico El Timepo para el año 2015 ocurrieron 869 incendios estructurales y presentan que "el 71% de los incendios estructurales es atendido en viviendas, seguido del 12% en edificaciones de uso industrial incluyendo bodegas y, en un tercer lugar, con un 7%, inmuebles de tipo comercial"; siendo las principales causas de incendios la saturacióin de tomas electricas en cuanto a conexiones, dejandolos como tendido eléctrico descubierto; otra principal causa son las llamas abiertas, fogones encendidos, velas/velones o el prolongado uso del calentador debido a que las personas dejan cosas acelerantes como ropa o trapos cerca de estas fuentes de calor y la radiación puede provocar un incendio; otro factor bastante frecuente de incendios son las planchas de cabello ya que generalmente se dejan sobre mueblería en madera o las dejan sobre las camas y como se mencionó la radiación constante puede generar estos incendios. Ésta noticia tambien dice que para los años 2015 y 2016  se tiene que "solo por esta causa se han presentado, entre el 2015 y el 2016, 3.761 incidentes y a esta estadística se le suman los causados por gas propano, que alcanzan los 326 para un total de 4.087 emergencias atendidas, una cifra nada despreciable"(3).
El informe de gestion del 2017 de la dirección nacional de Bomberos muestra que de los casos de emergencia que los bomberos atienden el 2,91% (2.760) corresponden a incendios estruturales,  el 1,02% (977) de las emergencias corresponden a fallas eléctricas y el 1,24% (1.186) de las emergencias corresponden a inundaciones (4), dichas inundaciones son causadas por uno de 2 factores, lluvias con precarios sistemas de desague o fugas en la estructuras interna de las edificaciones.

El Departamento de seguridad Nacional de los Estados Unidos cuenta con una serie de políticas de prevención y mitigación de incendios, entre la prevención está el uso e implementación de alarmas de humo en los hogares, ademas de eso

Múltiples sistemas de domótica implementan sensores de tensión, de corriente o de potencia para ver el consumo eléctrico de las cosas que usan en sus hogares, sistemas populares en colombia como ozom permiten tener estos datos a dispocisión y hacer una cuasnte de cuanto consumo se ha ahorrado, sin embargo, ninguno de estos implementa uns sistema de seguridad contra fallas de infraestructura de este tipo. de manera que éstos existen de tipo informativo. También se da debido a que estos sistemas son sistemas de automatización general en la vivienda, por ende, no profundizan en hacer mas robusta la protección de la infraestructura física de los hogares.

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

## Bibliografía
- (1) Robert Friedel and Paul Israel, Edison's Electric Light: Biography of an Invention, Rutgers University Press, New Brunswick New Jersey USA,1986 ISBN 0-8135-1118-6 pp.65-66
- (2) ""1920-1929 Stotz miniature circuit breaker and domestic appliances", ABB, 2006-01-09, accessed 15 December 2019".https://new.abb.com/de
- (3)Carol Malaver, El Tiempo "Descuidos hasta con planchas de pelo están causando incendios", 05 de abril 2016 https://www.eltiempo.com/archivo/documento/CMS-16555681
- (4) Dirección Nacional de Bomberos de Colombia, Informe de gestion del 2017 https://bomberos.mininterior.gov.co/sites/default/files/informe_de_gestion_dnbc_2017.pdf
- (5) Página oficial del departamiento de Seguridad Nacional de los Estados Unidos https://www.ready.gov/es/incendios-en-el-hogar

##
