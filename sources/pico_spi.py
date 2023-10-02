import spidev
import time

# Configura la comunicación SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, dispositivo 0

# Define el baudrate deseado en Hz (por ejemplo, 5 MHz)
baudrate = 5000000
spi.max_speed_hz = baudrate

try:
    while True:
        mensaje = input("Mensaje para la Raspberry Pi Pico: ")

        # Envía el mensaje a través de SPI
        respuesta = spi.xfer2(list(map(ord, mensaje)))
        respuesta = ''.join(map(chr, respuesta))
        print(f"Respuesta de la Raspberry Pi Pico: {respuesta}")
except KeyboardInterrupt:
    spi.close()
