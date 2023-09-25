import smbus

# Definir el número de bus I2C (puede ser 0 o 1 en Raspberry Pi)
i2c_bus = 1

# Definir la dirección del dispositivo I2C al que deseas enviar datos
device_address = 0x42  # Cambia esta dirección por la del dispositivo real

# Inicializar la conexión I2C
bus = smbus.SMBus(i2c_bus)

# Datos a enviar
data_to_send = "Hello, I2C!"

# Convertir la cadena en una lista de bytes
data_bytes = [ord(char) for char in data_to_send]

try:
    # Enviar datos al dispositivo I2C
    bus.write_i2c_block_data(device_address, 0, data_bytes)

    print("Datos enviados correctamente a la dirección", hex(device_address))
except Exception as e:
    print("Error al enviar datos:", str(e))
finally:
    # Cerrar la conexión I2C
    bus.close()
