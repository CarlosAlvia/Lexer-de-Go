import datetime
import os

analizadores = ["lexico", "sintactico", "semantico"]

def crear_logs(data, usuarioGit, indexAnalizador):
    if not os.path.exists('logs'):
            os.makedirs('logs')
    now = datetime.datetime.now()
    fecha_hora = now.strftime("%d%m%Y-%Hh%M")

    nombre_archivo = f'{analizadores[indexAnalizador]}-{usuarioGit}-{fecha_hora}.txt'
    ruta_archivo = os.path.join('logs', nombre_archivo)

    with open(ruta_archivo, 'w', encoding='utf-8') as file:
          for tok in data:
                file.write(f'{tok}\n')
    print(f'Log creado: {ruta_archivo}')
