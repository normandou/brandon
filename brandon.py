# Define las herramientas de la librería random a utilizar
from random import seed
from random import choice

# Crea una lista
tareas = ['Tomar agua']

# Primera interacción con el usuario
print('')
print('')
print(' /$$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$   /$$')
print('| $$__  $$| $$__  $$ /$$__  $$| $$$ | $$| $$__  $$ /$$__  $$| $$$ | $$')
print('| $$  \ $$| $$  \ $$| $$  \ $$| $$$$| $$| $$  \ $$| $$  \ $$| $$$$| $$')
print('| $$$$$$$ | $$$$$$$/| $$$$$$$$| $$ $$ $$| $$  | $$| $$  | $$| $$ $$ $$')
print('| $$__  $$| $$__  $$| $$__  $$| $$  $$$$| $$  | $$| $$  | $$| $$  $$$$')
print('| $$  \ $$| $$  \ $$| $$  | $$| $$\  $$$| $$  | $$| $$  | $$| $$\  $$$')
print('| $$$$$$$/| $$  | $$| $$  | $$| $$ \  $$| $$$$$$$/|  $$$$$$/| $$ \  $$')
print('|_______/ |__/  |__/|__/  |__/|__/  \__/|_______/  \______/ |__/  \__/')
print('')
print('')
print("BRANDON 0.1")
print('Bienvenide a la lista de quehacer más caótica del mundo.')
print('Sabemos que no quieres hacer nada, así que dile a Brandon todo lo que tienes que hacer y te dará una tarea al azar.')
print('')
print('DISCLAIMER:')
print('Este software no te asegura un aumento en la productividad. Sólo viene a decirte qué hacer.')
print('Por petición del autor, todas las listas agregan la opción de "tomar agua" porque le hace bien a tu cuerpo.')
print('')
print('Entonces, ¿Qué tienes que hacer ahora? Escribe lo que tengas que hacer y presiona ENTER.')
print('Cuando termines la lista, tipea "eso" y presiona ENTER para terminar.')
print('')

# Loop que define las tareas a ejecutar
while True:
    tareasInput = input()
    if tareasInput == 'eso':
        break
    else:
        tareas.append(tareasInput)
        print('Bacán. ¿Qué más?')
print('')

#Muestra la lista de tareas
print('Esto es todo lo que tienes que hacer ahora:')
print('')
print(*tareas, sep='\n')
print('')
print('')

# Establece el seed para el pseudorandomness
print('Ahora, ingresa un número entero para usar como seed, por favor.')
print('No es importante, pero idealmente nunca uses el mismo número dos veces.')
print('')
seed = input()
print('')

# Elegir la tarea y despedir a la gente. You did it!
print('Delicioso. Estamos eligiendo tu tarea...')
print('')
print('LA TAREA QUE DEBES HACER AHORA ES:')
print('»»-----------------------►')
print('  ' + choice(tareas))
print('»»-----------------------►')
print('')
print('Ahora anda y hazla. El resto de las tareas puede esperar.')
print('( •_•)>⌐■-■ (⌐■_■)')
print('')
print('¡Gracias por usar Brandon 0.1!')
print('Si quieres otra tarea, ejecuta Brandon nuevamente. ¡Nos vemos!')
print('')
