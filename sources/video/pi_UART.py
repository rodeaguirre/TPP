import serial

puerto = '/dev/ttyS0'
velocidad = 11520
ser = None

def UART_init():
    global ser
    ser = serial.Serial(puerto, velocidad)
    print("UART inicializado.")

def UART_print(mensaje):
    global ser

    if ser is not None:
        ser.write(mensaje.encode())
        print("UART: Mensaje enviado: {}".format(mensaje))

def UART_close():
    global ser
    if ser is not None:
        ser.close()
