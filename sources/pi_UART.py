import serial

# Define el puerto serial y la velocidad de comunicación
puerto = '/dev/ttyS0'  # Puerto UART en Raspberry Pi 4
velocidad = 115200  # Velocidad en baudios, ajusta según sea necesario

# Inicializa el objeto Serial
ser = serial.Serial(puerto, velocidad)

try:
    while True:
        # Escritura por UART
        mensaje = input("Ingrese el mensaje a enviar (o 'exit' para salir): ")
        if mensaje.lower() == 'exit':
            break
        ser.write(mensaje.encode())

        # Lectura por UART
        datos_recibidos = ser.readline().decode().strip()

        # Imprime los datos recibidos
        print("Datos recibidos:", datos_recibidos)

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C)
    print("\nInterrupción del teclado. Cerrando la comunicación UART.")

finally:
    # Cierra el puerto serial al salir
    ser.close()
