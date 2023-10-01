import spidev
import time

# Configuración del bus SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus SPI 0, Dispositivo SPI 0 (CS0)
spi.max_speed_hz = 1000000  # Velocidad máxima del bus SPI en Hz (1 MHz en este caso)

try:
    while True:
        # Lectura de datos desde un dispositivo SPI (por ejemplo, un sensor)
        adc_channel = 0  # Canal del convertidor analógico a digital (ADC) que deseas leer
        adc_data = spi.xfer2([1, (8 + adc_channel) << 4, 0])
        adc_value = ((adc_data[1] & 3) << 8) + adc_data[2]

        print(f"Valor del ADC en el canal {adc_channel}: {adc_value}")

        time.sleep(1)  # Espera 1 segundo antes de la siguiente lectura

except KeyboardInterrupt:
    pass

finally:
    spi.close()  # Cierra la conexión SPI al salir del programa
