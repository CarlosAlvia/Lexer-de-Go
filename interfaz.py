import tkinter as tk
from tkinter import filedialog, scrolledtext
import lexer 
import parserGo

def analisis_lexico(data):
    lexer.lexer.input(data)
    resultado = []
    while True:
        tok = lexer.lexer.token()
        if not tok:
            break
        resultado.append(f"{tok.type}: {tok.value} (linea {tok.lineno}, posicion {tok.lexpos})")
    return '\n'.join(resultado)

def analisis_semantico(data):
    resultado = parserGo.parse_semantic(data)
    return resultado

def analisis_sintactico(data):
    resultado = parserGo.parse_input(data)
    return resultado


def importar_archivo():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Go Files", "*.go*")])
    if filepath:
        with open(filepath, 'r', encoding="utf-8") as file:
            codigo_fuente.delete('1.0', tk.END)
            codigo_fuente.insert(tk.END, file.read())

def ejecutar_analisis(tipo):
    codigo = codigo_fuente.get('1.0', tk.END)
    if tipo == "lexico":
        resultado = analisis_lexico(codigo)
    elif tipo == "semantico":
        resultado = analisis_semantico(codigo)
    elif tipo == "sintactico":
        resultado = analisis_sintactico(codigo)
    output.delete('1.0', tk.END)
    if resultado:  
        output.insert(tk.END, resultado)

ventana = tk.Tk()
ventana.title("Analizador de Código")
ventana.configure(bg='grey10')
ventana.resizable(False, False) 

frame_botones = tk.Frame(ventana, bg='grey10')
frame_botones.grid(row=0, column=0, columnspan=3, pady=10)


boton_lexico = tk.Button(frame_botones, text="Análisis léxico", command=lambda: ejecutar_analisis("lexico"), bg='royalblue3', fg='white')
boton_lexico.pack(side=tk.LEFT, padx=10)

boton_semantico = tk.Button(frame_botones, text="Análisis semántico", command=lambda: ejecutar_analisis("semantico"), bg='royalblue3', fg='white')
boton_semantico.pack(side=tk.LEFT, padx=10)

boton_sintactico = tk.Button(frame_botones, text="Análisis sintáctico", command=lambda: ejecutar_analisis("sintactico"), bg='royalblue3', fg='white')
boton_sintactico.pack(side=tk.LEFT, padx=10)


boton_importar = tk.Button(ventana, text="Importar archivo", command=importar_archivo, bg='royalblue3', fg='white')
boton_importar.grid(row=1, column=2, columnspan=3, pady=5)


label_codigo_fuente = tk.Label(ventana, text="Código fuente", bg='grey10', fg='white', anchor='w')
label_codigo_fuente.grid(row=1, column=0, columnspan=3, padx=10 ,pady=5, sticky='w')


codigo_fuente = scrolledtext.ScrolledText(ventana, width=80, height=20, bg='white', fg='black')
codigo_fuente.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

label_output = tk.Label(ventana, text="Output", bg='grey10', fg='white', anchor='w')
label_output.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky='w')

output = scrolledtext.ScrolledText(ventana, width=80, height=10, bg='white', fg='black')
output.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

ventana.mainloop()