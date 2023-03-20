import tkinter as tk

def primeiroAno():
    resultado.delete(0, tk.END) # apaga o texto anterior
    resultado.insert(0, float(num1.get()) * float(num2.get()) + float(num1.get())) # adiciona o resultado na caixa de texto

def segundoAno():
    resultado1.delete(0, tk.END) # apaga o texto anterior
    valor_resultado = float(resultado.get())  # pega o valor da caixa de texto resultado como um número
    resultado1.insert(0, valor_resultado * float(num2.get()) + valor_resultado)  # adiciona o resultado na caixa

def terceiroAno():
    resultado2.delete(0, tk.END) # apaga o texto anterior
    valor_resultado1 = float(resultado1.get())  # pega o valor da caixa de texto resultado como um número
    resultado2.insert(0, valor_resultado1 * float(num2.get()) + valor_resultado1)  # adiciona o resultado na caixa

def quartoAno():
    resultado3.delete(0, tk.END) # apaga o texto anterior
    valor_resultado2 = float(resultado2.get())  # pega o valor da caixa de texto resultado como um número
    resultado3.insert(0, valor_resultado2 * float(num2.get()) + valor_resultado2)  # adiciona o resultado na caixa

def quintoAno():
    resultado4.delete(0, tk.END) # apaga o texto anterior
    valor_resultado3 = float(resultado3.get())  # pega o valor da caixa de texto resultado como um número
    resultado4.insert(0, valor_resultado3 * float(num2.get()) + valor_resultado3)  # adiciona o resultado na caixa

def sextoAno():
    #resultado5.delete(0, tk.END)
    valor_resultado4 = float(resultado4.get())
    resultado5.insert(0, valor_resultado4 * float(num2.get()) + valor_resultado4)

def setimoAno():
    #resultado5.delete(0, tk.END)
    valor_resultado5 = float(resultado5.get())
    resultado6.insert(0, valor_resultado5 * float(num2.get()) + valor_resultado5)

def oitavoAno():
    #resultado5.delete(0, tk.END)
    valor_resultado6 = float(resultado6.get())
    resultado7.insert(0, valor_resultado6 * float(num2.get()) + valor_resultado6)

def nonoAno():
    #resultado5.delete(0, tk.END)
    valor_resultado7 = float(resultado7.get())
    resultado8.insert(0, valor_resultado7 * float(num2.get()) + valor_resultado7)

def decimoAno():
    #resultado5.delete(0, tk.END)
    valor_resultado8 = float(resultado8.get())
    resultado9.insert(0, valor_resultado8 * float(num2.get()) + valor_resultado8)

root = tk.Tk()
root.title("Calculadora LCI")

tk.Label(root, text="Valor da aplicação:").grid(row=1, column=0)
tk.Label(root, text="Taxa anualizada do juros composto:").grid(row=2, column=0)
tk.Label(root, text="Primeiro ano:").grid(row=5, column=0)
tk.Label(root, text="Segundo ano:").grid(row=6, column=0)
tk.Label(root, text="Terceiro ano:").grid(row=7, column=0)
tk.Label(root, text="Quarto ano:").grid(row=8, column=0)
tk.Label(root, text="Quinto ano:").grid(row=9, column=0)
tk.Label(root, text="Sexto ano:").grid(row=10, column=0)
tk.Label(root, text="Sétimo ano:").grid(row=11, column=0)
tk.Label(root, text="Oitavo ano:").grid(row=12, column=0)
tk.Label(root, text="Nono ano:").grid(row=13, column=0)
tk.Label(root, text="Décimo ano:").grid(row=14, column=0)

# Cria uma caixa de texto
tk.Label(root, text="Digite o valor que você deseja saber ano a ano o montante aplicado em LCI na taxa anual desejada:").grid(row=0, column=0)

# Cria campos de entrada
num1 = tk.Entry(root)
num2 = tk.Entry(root)


# Define a posição dos campos de entrada
num1.grid(row=1, column=1)
num2.grid(row=2, column=1)

# Cria botão
#tk.Button(root, text="Somar", command=somar).grid(row=4, column=0)
tk.Button(root, text="montante", command=lambda: [primeiroAno(), segundoAno(), terceiroAno(), quartoAno(), quintoAno(), sextoAno(), setimoAno(), oitavoAno(), nonoAno(), decimoAno()]).grid(row=4, column=1)

# Cria uma caixa de texto para exibir o resultado
resultado = tk.Entry(root)
resultado.grid(row=5, column=1)
resultado1 = tk.Entry(root)
resultado1.grid(row=6, column=1)
resultado2 = tk.Entry(root)
resultado2.grid(row=7, column=1)
resultado3 = tk.Entry(root)
resultado3.grid(row=8, column=1)
resultado4 = tk.Entry(root)
resultado4.grid(row=9, column=1)
resultado5 = tk.Entry(root)
resultado5.grid(row=10, column=1)
resultado6 = tk.Entry(root)
resultado6.grid(row=11, column=1)
resultado7 = tk.Entry(root)
resultado7.grid(row=12, column=1)
resultado8 = tk.Entry(root)
resultado8.grid(row=13, column=1)
resultado9 = tk.Entry(root)
resultado9.grid(row=14, column=1)


# Inicia a janela principal
root.mainloop()
