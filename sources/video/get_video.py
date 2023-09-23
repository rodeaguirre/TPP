import subprocess

# Comando que deseas ejecutar (por ejemplo, "ls" para listar archivos en el directorio actual)
comando_video = "libcamera-vid -o ../../media/Images/AVI/test.avi -t 5000 --width 680 --height 320 --framerate 60"
# comando_ls = "ls"
# Ejecuta el comando y captura la salida
subprocess.run(comando_video, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
'''
resultado = subprocess.run(comando_ls, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Verifica si el comando se ejecutó correctamente
if resultado.returncode == 0:
    print("Salida del comando:")
    print(resultado.stdout)
else:
    print("Error al ejecutar el comando:")
    print(resultado.stderr)
'''