import tkinter as tk
import datetime

valor_aplicado = None

def calcularMontanteAno(valor_aplicado, data_inicial, taxa):
    montante = valor_aplicado * (1 + taxa)
    data_inicial = datetime.datetime.combine(data_inicial, datetime.datetime.min.time())
    data_inicial += datetime.timedelta(days=365)  # Incrementa a data em um ano
    return montante, data_inicial

def calcularMontanteTotal():
    global valor_aplicado
    valor_input = num1.get()
    taxa_input = num2.get()

    #Verifica se os campos de entrada estão vazios
    if not valor_input or not taxa_input:
        resultado.delete("1.0", tk.END)
        resultado.insert(tk.END, "Por favor, preencha todos os campos.")
        return

    try:
        valor_aplicado = float(valor_input)
        taxa_anual = float(taxa_input)

        #Verifica se os valores estão dentro das faixas desejadas
        if valor_aplicado <= 0 or taxa_anual <= 0:
            resultado.delete("1.0", tk.END)
            resultado.insert(tk.END, "Valor da aplicação e taxa devem ser maiores que zero.")
            return

        data_atual = datetime.date.today()
        resultado.delete("1.0", tk.END)

        for i in range(1, 11):
            montante, data_atual = calcularMontanteAno(valor_aplicado, data_atual, taxa_anual)
            resultado_ano = f"{data_atual.strftime('%d/%m/%Y')}: R$ {montante:.2f}"
            resultado.insert(tk.END, resultado_ano + "\n")
            valor_aplicado = montante

            #Converte a data_atual para um objeto datetime.date
            data_atual = datetime.datetime.combine(data_atual, datetime.datetime.min.time()).date()
    except ValueError:
        resultado.delete("1.0", tk.END)
        resultado.insert(tk.END, "Valores inseridos são inválidos. Por favor, insira números válidos.")

root = tk.Tk()
root.title("Calculadora LCI")

tk.Label(root, text="Valor da aplicação:").grid(row=1, column=0)
tk.Label(root, text="Taxa anualizada do juros composto:").grid(row=2, column=0)
tk.Label(root, text="Montantes anuais:").grid(row=5, column=0)

tk.Label(root, text="Digite o valor que você deseja saber ano a ano o montante aplicado em LCI na taxa anual desejada:").grid(row=0, column=0)

num1 = tk.Entry(root)
num2 = tk.Entry(root)

num1.grid(row=1, column=1)
num2.grid(row=2, column=1)

tk.Button(root, text="Calcular montantes", command=calcularMontanteTotal).grid(row=4, column=1)

resultado = tk.Text(root, height=10, width=30)
resultado.grid(row=5, column=1)

root.mainloop()
