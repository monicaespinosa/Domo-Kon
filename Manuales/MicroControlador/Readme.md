## La previa

1. Independiente del tipo de microcontrolador (ESP8266 o ESP32), si tu tarjeta cuenta con el puerto USB y deseas cargar Micropython, lo primero a realizar es entrar en el siguiente enlace:

    http://micropython.org/download

2. Una vez allí, se encontrarán grandes cantidades de archivos posibles para descarga. Sin embargo, tan pronto como se identifique el tipo de placa a usar, se debe bajar el archivo correspondiente al firmware que se cargará a la placa y permitirá programar Micropython dentro de él.

 ![alt text](https://github.com/monicaespinosa/Domo-Kon/blob/master/Manuales/MicroControlador/Images/Link_Descarga.png)
 **Figura 1**- Archivo de descarga para la placa ESP8266.

Por recomendación se sugiere bajar la última versión estable que se disponga para la placa. A la fecha de realización la última versión estable es la v1.12, sin embargo todos las placas usadas están cargadas con la versión v.1.11.

3. El archivo descargado tiene extensión `.bin` y se recomienda tenerlo en una carpeta dispuesta para el proyecto. A partir de aquí debo mencionar que existen distintos métodos, editores y vías para cargar el archivo a la placa necesaria; no obstante recomendaré el siguiente editor para Micropython debido a la facilidad con la que se opera y a que integra varias funcionalidades útiles a la hora de programar.

    https://github.com/DFRobot/uPyCraft

## Cargando el Firmware:

1.	Una vez se tienen todos los elementos: uPyCraft, los archivos .bin correspondientes a  la placa y versión deseada y la placa con su respectiva conexión vía USB al computador, se procede a abrir el programa y abrir la pestaña Tools seguido de la opción BurnFirmware.

![alt text](https://github.com/monicaespinosa/Domo-Kon/blob/master/Manuales/MicroControlador/Images/Firmware_upload.png)

2. Dentro de la ventana abierta se seleccionan las opciones correspondientes a la placa de desarrollo que se requiere y se indica el firmware que se va a cargar en la placa.

![alt text](https://github.com/monicaespinosa/Domo-Kon/blob/master/Manuales/MicroControlador/Images/Firmware_update.png)

3.	Con el botón Choose se escoge el firmware que se va a subir, indicando la ruta donde este archivo se encuentra.

4.	Finalmente se debe mantener presionado el botón Flash o Boot del módulo correspondiente y dar click en ok. Una vez hecho esto, se debe soltar el botón Flash o Boot y el programa deberá mostrar una barra de estado en la que se muestra cómo formatea e instala el nuevo firmware en la placa.

5.	Si todo salió bien, el programa no debe mostrar algún error y la placa quedó cargada con micropython.

6.	Se puede usar el archivo `blink.py` para probar que la conexión quedó bien hecha. Sólo se debe abrir con el programa uPyCraft y dar click en el botón _Play_. Una aclaración: verifica que esté conectada la tarjeta y exista una comunicación adecuada.

![alt text](https://github.com/monicaespinosa/Domo-Kon/blob/master/Manuales/MicroControlador/Images/blink.png)
 
## Configurando las diferentes Funciones

Para empezar a configurar cada uno de los pines, lo primero que se debe hacer es conectar el microcontrolador y verificar que existe comunicación entre él y la IDE.

![alt text](https://github.com/monicaespinosa/Domo-Kon/blob/master/Manuales/MicroControlador/Images/Code_upload.png)

Ahora sí, ¡estamos listos!

### Digital Outputs:

 Tanto el ESP32 como el ESP8266 disponen de 30 pines, de éstos, 18 pueden ser pueden ser utilizados como salidas digitales en el ESP8266 y 25 en el ESP32. No obstante, el uso de los distintos pines para cada una de las funciones anteriores reduce la cantidad de pines disponibles y por tanto se configuraron 8 salidas digitales para el ESP32 y 5 salidas digitales para el ESP8266. Cada una de ellas cuenta con tensión de 3.3v y una corriente máxima por pin de 40mA.

Lo primero a realizar es importar la librería machine, la cual permite manejar las distintas funcionalidades del microcontrolador. De esta librería sólo importaremos la parte respectiva a los pines con la siguiente instrucción:

```bash    
from machine import Pin
```

Adicional a esta librería, se requerirá importar una librería dedicada al manejo del tiempo dentro del microcontrolador. 

```bash
import time
```

Una vez se tengan todas las librerías correctamente importadas, se procede a declarar como salidas los pines que se necesiten. En el caso de este ejemplo, se utilizará el pin que tiene como salida un led dentro de la misma placa (en el caso del ESP8266 y el ESP32 son el mismo pin).

```bash
led = Pin(2, Pin.OUT)
```

Finalmente, para hacer la función más básica en cualquier microcontrolador (aunque no menos importante), se deberá declarar un ciclo en el que se prende y se apaga con igual periodo el led. ¡En efecto! Es una función _Blink_, con un periodo definido por el usuario.

```bash
from machine import Pin import time led = Pin(2, Pin.OUT)

def blink(period):
led.on()
time.sleep_ms(period)
led.off()
time.sleep_ms(period)

while True:
blink(period)
```

### ADC: 

Cuenta con un conversor análogo-digital de resolución 12 bits con tensión máxima de 3.3v en los picos de cada señal. El ESP8266 cuenta con 1 puerto ADC, y el ESP32 cuenta con 5 canales dispuestos para tal fin.

El procedimiento es muy similar al anterior: simplemente es necesario importar la librería correspondiente al conversor análogo-digital del microcontrolador.

```bash
from machine import Pin, PWM, ADC
```

Una vez hecho esto, se pueden disponer de las entradas ADC del microcontrolador. Hasta 15 en el ESP32 y 1 en el ESP8266. En el caso específico, se tienen 4 entradas de cada uno de los sensores requeridos.

```bash
entrada_Adc = ADC(Pin(34)) entrada_Adc1 = ADC(Pin(36)) entrada_Adc2 = ADC(Pin(39)) entrada_Adc3 = ADC(Pin(35))
```

### Comunicación UART: 

Cuenta con un puerto serial para comunicación asincrónica y 8 bits de transferencia de datos. En la tarjeta ESP8266 se tiene dispuesto 1 puerto UART completo (dúplex) y un puerto de transferencia (TX); mientras que en el ESP32 se cuenta con 1 solo puerto completo (dúplex) para comunicación serial. 

En este caso, se requiere importar la librería UART disponible en Machine

```bash
from machine import Pin, UART
```

Una vez hecho esto, se procede a configurar los pines por los cuales se va a realizar la comunicación serial. En el caso del ESP32, sólo se cuenta con una única conexión disponible para el usuario.

```bash
u = UART(2) u.init(baudrate=115200, bits=8, parity=0, stop=1, tx=17, rx=16)
```

Finalmente, con el comando la siguiente línea podemos leer y recibir

```bash
Incoming_msn=u.read()
```

### Comunicación SPI:

Se agregó un puerto de comunicación SPI para cada uno de los microcontroladores, teniendo la posibilidad tanto de enviar, como de recibir datos de sensores, pantallas, memorias u otros dispositivos que puedan ser usados como esclavos. Existe un puerto de comunicación SPI completo en el ESP32 para comunicación con la FPGA.

Primero se debe importar la librería SPI desde machine
from machine import Pin, SPI
Luego, se debe configurar la comunicación SPI indicando qué pines se requieren para ello e indicando otros valores correspondientes a la comunicación.

```bash
spi = SPI(-1, baudrate=100000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
```

Una vez configurado, se procede a iniciar la comunicación

```bash
spi.init(baudrate=100000)
```

Finalmente, ya queda habilitado el puerto de comunicación SPI para enviar y recibir información de un dispositivo esclavo.

```bash
spi.write(0x32,'hi')
spi.read(0x32, buff)
```

Una aclaración más. El ESP32 y el ESP8266 sólo funcionan como máster tanto en I2C, como en SPI así que por lo que más quieras: ¡NO GASTES TIEMPO INTENTANDO ENVIAR INFORMACIÓN DE UNA PLACA A LA OTRA CON ESTE PROTOCOLO! ¡EN VERDAD!

### Comunicación I2C:

La tarjeta ESP8266 cuenta con un puerto I2C para la comunicación con periféricos que puedan enviar información o recibirla, tal como una pantalla. Debido a la configuración posible en Micropython, este protocolo sólo puede ser configurado como Master en ambos microcontroladores.
¡Ya lo tienes! Primero, la importación

```bash
from machine import Pin, I2C
```

Luego la *configuración*:

```bash
i2c = I2C(-1, scl=Pin(18),sda=Pin(21))
```

Por supuesto, la *iniciación*:

```bash
i2c.init(scl=Pin(18),sda=Pin(21))
```

Finalmente, la *usación*... Está bien, corrijo, la *implementación*:

```bash
i2c.writeto(0x32, 'hi') #Comando para Enviar
msg=i2c.readfrom(0x08,1) #Comando para recibir
```

### Salida PWM:

Se habilitó una salida PWM en ambos microcontroladores en caso tal que sea necesario una aplicación de Dimmer para el manejo de algún actuador y con miras a abrir la posibilidad tanto de escalabilidad, como de control sobre el manejo de las variables.

Lo sé, hasta aquí ya debe parecer metódico: primero se importa, luego se configura y luego se usa. ¡ya lo tienes!

```bash
from machine import Pin, PWM #Importar librerías
import time led = Pin(2, Pin.OUT) #Configuración de pines led2= PWM(Pin(5), freq(90)) #Uso de Pines PWM
```

### Interrupciones:

Claramente se deben manejar interrupciones. Bien sea que entre un mensaje nuevo o que exista algún sensor que deba tener mayor prioridad o algún encoder; se debe recurrir al uso de interrupciones. Y como todo, en este documento, se debe seguir el mismo proceso: importar, configurar y uso.

```bash
from machine import Pin #Importar
button = Pin(4, Pin.IN)#Configurar 
button.irq(trigger=Pin.IRQ_RISING, handler=func) #Configurar
```

En el caso del uso, se debe entender que en el código anterior se declara una función func, ésta se encarga de definir qué se hará cada vez que exista una interrupción y es ahí donde se ve el efecto de la misma. Para este ejemplo se encenderá un LED.

```bash
def func(v):   global value,counter   time.sleep_ms(50)   if(button.value() == 0):     return   while(button.value() == 1):     time.sleep_ms(100)   time.sleep_ms(100)   counter+=1   led.value(value)   value = 0 if value else 1   print("IRQ ",counter)
```

### Comunicación WiFi:
Dado que la finalidad de ambos microcontroladores es su aplicabilidad en IoT, ambas tarjetas cuentan con la posibilidad de comunicación vía WiFi usando el protocolo TCP/IP de comunicación. Con esto se logra que cada uno de los microcontroladores pueda manejar dispositivos externos, usar otros protocolos y relegando así al WiFi la tarea de comunicación entre ambas tarjetas.

**Importar**

```bash
import network
```

Para el uso de la red WiFi, se debe tener claro qué papel hará cada microcontrolador. ¿Será un cliente (station client)? ¿un servidor (Access point)?

**Configuración**

```bash
sta_if = network.WLAN(network.STA_IF) #uC se conecta a la red wifi 
ap_if= network.WLAN(network.AP_IF) #uC create a WiFi network 
```

**Uso y Prueba**

```bash
def do_connect(): #Función para conectarse a una red creada desde un teléfono móvil
    import network     sta_if = network.WLAN(network.STA_IF)     if not sta_if.isconnected():         print('connecting to network...')         sta_if.active(True)         sta_if.connect('DavidWifi', 'davideslaluz')         while not sta_if.isconnected():             pass     print('network config:', sta_if.ifconfig())
while True:     do_connect()   led.on()   time.sleep_ms(250)   led.off()   time.sleep_ms(250)
```

Finalmente ahora se debe decidir mediante qué protocolo se van a comunicar los microcontroladores. En nuestro caso será TCP/IP, sin embargo, eso queda para otro capítulo.
