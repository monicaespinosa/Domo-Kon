
##Pre Main
#Libraries 
from machine import Pin, PWM, ADC, UART, SPI
import time
import network
import socket
  # Setup Routine
#Outputs 
led = Pin(2, Pin.OUT)
valvula_gas= Pin(3, Pin.OUT)
bomba_agua= Pin(5, Pin.OUT)
luz = Pin(6, Pin.OUT)
#UART Communication
u = UART(2)
u.init(baudrate=115200, bits=8, parity=0, stop=1, tx=17, rx=16)
#UART.irq(trigger, priority=1, handler=None, wake=machine.IDLE)
#SPI Communication
spi = SPI(-1, baudrate=100000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
spi.init(baudrate=100000)
#ADC Sensors
Luz_Adc = ADC(Pin(36))
Gas_Adc = ADC(Pin(39))
Presencia_Adc = ADC(Pin(35))
#IRQ
button = Pin(4, Pin.IN)
button.irq(trigger=Pin.IRQ_RISING, handler=flow_read)
def flow_read():
  global value,counter
  time.sleep_ms(50)
  if(button.value() == 0):
    return
  while(button.value() == 1):
    time.sleep_ms(100)
  time.sleep_ms(100)
  counter+=1
  led.value(value)
  value = 0 if value else 1
  return flow
 #Variables Actuadores
 actuador_id=0
 valvula_state=0
 bomba_state=0
 luz_state=0
 #Variables Sensores
 luz_id=1
 agua_id=2
 gas_id=3
 #Leer Sensores
 def leerSensores():
   luz_value=Luz_Adc.read()
   u.send(luz_id)
   time.sleep_ms(1)
   u.send(luz_value)
   time.sleep_ms(5)
   presencia_value=Presencia_Adc.read()
   time.sleep_ms(5)
   gas_value=Gas_Adc.read()
   u.send(gas_id)
   time.sleep_ms(1)
   u.send(gas_value)
   time.sleep_ms(5)
   agua_value=flow_read()
   u.send(agua_id)
   time.sleep_ms(1)
   u.send(agua_value)
 
 #LOOP
 while True:
      if u.any(): #There's something in UART bus?
        actuador_id=u.read()
        if actuador_id==1:
            #//verificar el estado ;)
          #valvula_gas.on() #Qué es mejor? .on o .value?
          valvula_gas.value(valvula_state)
          #u.send(valvula_state) #Enviar estado actual
          actuador_id=0
        elif actuador_id==2:
          bomba_agua.value(bomba_state)
          actuador_id=0
        elif actuador_id==3:
          luz.value(luz_state)
          actuador_id=0
        else:
          pass
      elif not u.any()
        #automatic_mode()
        leerSensores()
        time.sleep_ms(10)
        if luz_value <2000: #Verificar valor
          luz.off()
        else:
          pass
        if presencia_value>0:
          bomba_agua.value(not bomba_state)
        else:
          if agua_value>0:
            bomba_agua.value(not bomba_state)
          else:
            bomba_agua.off()
        if gas_value>500: #Verificar valor
            for i in range(3): #Si sos Pro, prendes la Tele con una calavera xD
             luz.on()
             time.sleep_ms(1000)
             luz.off()
             time.sleep_ms(1000)
        else: 
          pass
          
        


