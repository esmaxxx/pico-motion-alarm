from machine import Pin, PWM
from time import sleep

pir = Pin(28, Pin.IN)
led = Pin(15, Pin.OUT)

buzzer = PWM(Pin(16))
buzzer.duty_u16(0)  # Start stil

while True:
    beweging = pir.value()

    if beweging:
        led.on()

        buzzer.freq(1000)
        buzzer.duty_u16(30000)

    else:
        led.off()
        buzzer.duty_u16(0)

    sleep(0.05)
