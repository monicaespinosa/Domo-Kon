## Contextualización

El proyecto cuenta con dos tarjetas de desarrollo; cada una tiene un SoC de referencia ESP8266 y ESP32 y 30 pines disponibles para los diferentes requerimientos del proyecto, ambas tarjetas de desarrollo cuentan con Micropython en su versión v1.11 para cada uno de los microcontroladores (la versión disponible actualmente es v1.12, sin embargo, no es estable para los microcontroladores a la fecha de realización del proyecto).
Para leer más acerca de las versiones de Micropython haga click en [Documentación Micropython](https://docs.micropython.org/en/latest/index.html)

## Funciones

El microcontrolador ESP8266 se eligió para ser una estación remota del microcontrolador ESP32. Esto se dispuso así, debido a la limitante de pines disponibles para la lectura de los sensores que en el caso del ESP32, tiene una capacidad suficiente para la lectura de las variables necesarias.
Teniendo en cuenta que ambas tarjetas cuentan con Micropython, la migración de las distintas funciones necesarias resultaba factible y fácil de realizar. Claro está, se requiere una adecuada asignación de pines en cada una de las tarjetas.
Actualmente ambas tarjetas cuentan con las siguientes funciones:

- ADC: cuenta con un conversor análogo-digital de resolución 12 bits con tensión máxima de 3.3v en los picos de cada señal. El ESP8266 cuenta con 1 puerto ADC, y el ESP32 cuenta con 5 canales dispuestos para tal fin.

- Comunicación UART: Cuenta con un puerto serial para comunicación asincrónica y 8 bits de transferencia de datos. En la tarjeta ESP8266 se tiene dispuesto 1 puerto UART completo y un puerto de transferencia (TX); mientras que en el ESP32 se cuenta con 1 solo puerto completo para comunicación serial.

- Comunicación SPI: Se agregó un puerto de comunicación SPI para cada uno de los microcontroladores, teniendo la posibilidad tanto de enviar, como de recibir datos de sensores, pantallas, memorias u otros dispositivos que puedan ser usados como esclavos. Existe un puerto de comunicación SPI completo en el ESP32 para comunicación con la FPGA.

- Comunicación I2C: La tarjeta ESP8266 cuenta con un puerto I2C para la comunicación con periféricos que puedan enviar información o recibirla, tal como una pantalla. Debido a la configuración posible en Micropython, este protocolo sólo puede ser configurado como Master en ambos microcontroladores.

- Digital Outputs: Tanto el ESP32, como el ESP8266 disponen de 25 pines que pueden ser utilizados como salidas digitales. No obstante, el uso de los distintos pines para cada una de las funciones anteriores reduce la cantidad de pines disponibles y por tanto se configuraron 8 salidas digitales para el ESP32 y 5 salidas digitales para el ESP8266. Cada una de ellas cuenta con tensión de 3.3v y una corriente máxima por pin de 40mA.

- Salida PWM: Se habilitó una salida PWM en ambos microcontroladores en caso tal que sea necesario una aplicación de Dimmer para el manejo de algún actuador y con miras a abrir la posibilidad tanto de escalabilidad, como de control sobre el manejo de las variables.

- Comunicación WiFi: Dado que la finalidad de ambos microcontroladores es su aplicabilidad en IoT, ambas tarjetas cuentan con la posibilidad de comunicación vía WiFi usando el protocolo TCP/IP de comunicación. Con esto se logra que cada uno de los microcontroladores pueda manejar dispositivos externos, usar otros protocolos y relegando así al WiFi la tarea de comunicación entre ambas tarjetas.

## Pinout

![alt text](https://github.com/monicaespinosa/Domo-Kon/blob/master/MicroControlador/Images/ESP32pinout.png)
**Figura 1**-Dispocisión de pines de la tarjeta de desarrollo ESP32.

![alt text](https://github.com/monicaespinosa/Domo-Kon/blob/master/MicroControlador/Images/ESP8266pinout.png)
**Figura 2**-Dispocisión de pines de la tarjeta de desarrollo ESP8266.

## Características

|Características|ESP8266|ESP32|
|--|--|--|
|Procesador|Tensilica LX 106 32-bit a 80MHz (hasta 160MHz)|Tensilica Xtensa LX6 32-bit Dual-Core a 160MHz (hasta 240MHz)|
|Memoria RAM|80kB (40kB disponibles)|520kB|
|Memoria Flash|Hasta 4MB|Hasta 16MB|
|ROM|No|448kB|
|Alimentación| 3.0 a 3.6 V|2.2 a 3.6 V|
|Rango de temperaturas|-40°C a 125°C|-40°C a 125°C|
|Consumo de corriente|80mA (promedio) 225mA máximo|80mA (promedio) 225mA máximo|
|Consumo en modo de sueño profundo|20uA (RTC+ memoria RTC)|2.5uA (10uA RTC+ memoria RTC)|
|WiFi|802.11b/g/n (hasta +20dBm) WEP, WPA|802.11b/g/n (hasta +20dBm) WEP, WPA|
|Soft-AP|Sí|Sí|
|Bluetooth|No|v4.2 BR/EDR y BLE|
|UART|2* (En una de ellas sólo puede usarse el pin Tx)|3|
|I2C|1|2|
|SPI|2|4|
|GPIO(utilizables)|32|11|
|PWM|8|16|
|ADC|1 (10 bit)|18 (12 bit)|
|ADC con preamplificador|No|Sí (Bajo Ruido) Hatas 60dB|
|DAC|No|2 (8 bit)|
|1-Wire|Implementado por software|Implementado por software|
|I2S|1|2|
|CAN bus|No|1x2.0|
|Ethernet|No|10/100 Mbps MAC|
|Sensor de temperatura|No|Sí|
|Sensor efecto Hall|No|Sí|
|IR|Sí|Sí|
|Temporizadores|3|4 (64 bits)|
|Encriptación por hardware|No (TLS 1.2 por software)|Sí (AES, SHA, RSA, ECC)|
|Gen. de núm. aleatorios|No|Sí|
|Encriptación de la flash|No|Sí|
|Arranque seguro|No|Sí|
