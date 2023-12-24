import serial

puerto = '/dev/ttyS0'
velocidad = 11520
ser = None

def UART_init():
    global ser
    ser = serial.Serial(puerto, velocidad)
    print("UART inicializado.")

def UART_print(mensajes):
    global ser

    if ser is not None:

        print("UART: Mensaje enviado:")
        for mensaje in mensajes:
            mensaje = str(mensaje)
            ser.write(mensaje.encode())
            print(mensaje)

def UART_close():
    global ser
    if ser is not None:
        ser.close()
