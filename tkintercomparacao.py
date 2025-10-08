# Atividade 4
# Utilizando o PyCharm, crie um programa com interface gráfica em Python
# que receba dois números, compare-os e informe se o primeiro é
# maior, menor ou igual ao segundo.

import tkinter as tk
from tkinter import messagebox

def comp_numeros():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num1 > num2 :
        messagebox.showinfo("Resultado", f"O número {num1} é maior que {num2}")
    elif num1 == num2 :
        messagebox.showinfo("Resultado", f"O numero {num1} é igual a {num2}")
    else:
        messagebox.showinfo("Resultado", f"O numero {num1} e menor que {num2}")

# Criando a janela
janela=tk.Tk()
janela.title("Comparando Números")

# Criando os widgets
label_num1=tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1=tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2=tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2=tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_comp=tk.Button(janela, text="Comparar", command=comp_numeros)
botao_comp.grid(row=2, columnspan=2, padx=10, pady=5)

# Rodando o loop principal
janela.mainloop()
