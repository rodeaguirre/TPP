import serial

# Define el puerto serial y la velocidad de comunicación
puerto = '/dev/ttyS0'  # Puerto UART en Raspberry Pi 4
velocidad = 9600  # Velocidad en baudios, ajusta según sea necesario

# Inicializa el objeto Serial
ser = serial.Serial(puerto, velocidad)

try:
    while True:
        # Escritura por UART
        mensaje = input("Ingrese el mensaje a enviar (o 'exit' para salir): ")
        print("Hola")
        if mensaje.lower() == 'exit':
            break
        ser.write(mensaje.encode())

        mensaje = input("Mansaje enviado.")
        # Lectura por UART
        datos_recibidos = ser.readline().decode().strip()
        if datos_recibidos:
            input("Mansaje enviado.")
            # Imprime los datos recibidos
            input("Datos recibidos:{datos_recibidos}")

            # Envía los datos recibidos de vuelta
            ser.write(datos_recibidos.encode())
        else:
            print("No se recibió nada")

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C)
    print("\nInterrupción del teclado. Cerrando la comunicación UART.")

finally:
    # Cierra el puerto serial al salir
    ser.close()
