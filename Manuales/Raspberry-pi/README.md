# Configuración del Ambiente

se ha demostrado que el conocimiento es sencillo, así que la aplicación de este 
debería serlo aún más ¿no?, siendo así, para cumplir con esta idea, el
objetivo de esta guía no es solo poder configurar la **Raspberry Pi**, además 
que no sea algo ladrilludo hacerlo. Así que empecemos.

## Cómo se hace

Como un buen chef, para vender la receta hay que tener una salsa secreta. ¿Cuál
es la salsa secreta, se preguntan? La respuesta es amor... Por un momento la
creyeron, ¿no?. En realidad se logra mediante **Virtualización y orquestación de
servicios.** Abstrayendo la capa de desarrollo es posible automatizar gran parte
del proceso acelerando la velocidad de desarrollo y disminuyendo el overhead
operativo al momento de prototipar y aprender herramientas.

### Qué es la Virtualización

En computación (nuestro área de interés, afortunadamente), se refiere al acto de
crear un representación absatracta de algo, incluyendo Hardware, dispositivos de
almacenamiento, recursos de red y otros. Por ejemplo, los emuladores de consolas
retro (seguro se han pasado todos los Castlevania en uno de esos) son una
virtualización de todo el dispositivo con intterfaces de interacción en el
hardware moderno.

Debido a que la Raspberry pi cuenta con recursos limitados no se puede usar
virtualización de hardware, que es la más sencilla. Así que toca ser cool y
utilizar tecnología de contenedores.

#### Qué cangrejos son los contenedores

Me alegra que preguntes posible lector. La tecnología de contenedores, también
conocida como **virtualización a nivel de Sistema Operativo**, se refiere a una
capacidad del sistema operativo en la que el _kernel_ permite la existencia de
multiples instancias en aislamiento (tal cuál como te hacía sentir tu ex). Estas
instancias pueden verse como máquinas completas desde cierto punto de vista;
¿cierto punto de vista? Efectivamente, desde el punto de vista de los procesos en
ellas, estos "contenedores" so máquinas completas, ya que solo tienen acceso a los
recursos y dispositivos asignados al contenedor.

### Pero cómete ya la maldita naranja

Con paciencia, a eso vamos. Para el desarrollo de contenedores se usa
[Docker](https://www.docker.com/). Este es el éstandar de industria para la
creación de contenedores. A continuación se explica como usarlo en una
Raspberry pi

1. En primer lugar, hay que instalar el motor de Docker en la Raspberry pi, para ello
se ejecuta el siguiente comando:  

``` bash
curl -sSL https://get.docker.com | sh
```

2. Una vez terminada la instalación de Docker hay que proceder a darle permisos
especiales al usuario.

```bash
sudo usermod -aG docker pi
```

3. Por último hay que asegurarse que el servicio de Docker se va a iniciar de forma
automática con el boot de la raspberry. Para eso se usa la aplicación `systemctl`.

```bash
sudo systemctl enable docker
```

5. Ahora es un buen momento para reiniciar la Raspberry pi y felicitarnos por
llegar
hasta acá.

6. Una vez ha reiniciado la Raspberry hay que probar la instalación. Para probarlo
vamos a usar una imagén provista por Docker.

```bash
docker run hello-world
```

### OK, ya salimos de la virtualización

Efectivamente, Con esto ya cubrimos la parte de la virtualización. Aún así queda la
mitad del camino por recorrer. Hay que tener herramientas para poder automatizar el
proceso de abastecimiento y control de los contenedores.

>_Se necesita un servicio para dominarlos a todos, un servicio para hallarlos, un_
>_servicio para traerlos a todos y en subprocesos atarlos._

Para lograr esto Docker ofrece una herramienta perfecta para el trabajo:
**docker Compose**. Ahora se explica como instalarlo.

1. Primero que nada Docker Compose tiene varias dependencias, así que toca
instalarlas.

```bash
sudo apt-get install libffi-dev libssl-dev
sudo apt-get install -y python python-pip
sudo apt-get remove python-configparser
```

2. Ya con las dependencias instaladas se procede a instalar Docker Compose.

```bash
sudo pip install docker-compose
```

## Pero antes de irme, no me gusta desarrollar sobre la Raspberry

Creeme, no eres el único. Pero no desespereís posible lector. Hay una forma de
desarrollar remotamente en tu Raspberry pi desde la comodidad de tu máquina
principal.

### Contadme más, Oh sabio escritor

De acuerdo, para esto solo es necesario habilitar la interfaz `SSH` de la
Raspberry, es tan fácil como

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

### ¿Eso es todo?

Si, eso es todo, ya solo queda conectar tu dispositivo principal a la misma red
que la Raspberry(por tu salud mental conecta la Raspberry de forma fisica a la red)
y usar tu IDE favorito (el mío es VScode). Para conectarte usa el nombre
`raspberrypi` con el nombre y contraseña que hayas asignado. En caso de que eso no
funcione, simplemente conectate usando la ip asignada por tu DHCP. Para conocer
esta IP solo tienes que ejecutar `nslookup raspberrypi`.

## Ahora, eso es todo

Con estos pasos ya es posible desarrollar de forma cómoda y completamente
transparente en tu Raspberrypi y no te tienes que preocupar con instalaciones y
otras cosas, ya que Docker se encarga de todo por ti.

## TL;DR: Te pareció muy largo

Si te quieres saltar toda la explicación porque la pereza rige tus decisiones y
llegas justo al final para ver la implementación rápida, simplemente ejecuta los
`.sh` adjuntos.
