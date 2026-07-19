import tkinter as tk
from tkinter.font import Font

janela = tk.Tk()
janela.title("CALCULADORA")
janela.geometry("320x450")

minha_fonte = Font(family="Arial", size=18, weight="bold")
#visor para ver a conta
#justify="right" faz o texto aparecer da direita pra esquerda, como numa calculadora real
visor = tk.Entry(janela, font=minha_fonte, justify="right")
#columnspan=4 significa que o visor vai ocupar o espaço de 4 colunas!
visor.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

#criarei a logica por tras nessa parte do código
def adiciona_valor(valor):
   
    visor.insert(tk.END, valor)#esse tk.END vai garantir para nós que o próximo caractere vai ser colocado na direita
def limpar():
    #apaga do início (0) até o final (tk.END)
    visor.delete(0, tk.END)
def calcular():
    #primeiro vamos pegar o que está no visor:

    conta=visor.get()
    try:
        resultado=eval(conta)

        limpar()
        visor.insert(tk.END, str(resultado))
    except:
        limpar()
        visor.insert(tk.END, "ERRO")

# criação de botões
botao_0 = tk.Button(janela, text="0", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("0"))
botao_1 = tk.Button(janela, text="1", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("1"))
botao_2 = tk.Button(janela, text="2", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("2"))
botao_3 = tk.Button(janela, text="3", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("3"))
botao_4 = tk.Button(janela, text="4", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("4"))
botao_5 = tk.Button(janela, text="5", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("5"))
botao_6 = tk.Button(janela, text="6", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("6"))
botao_7 = tk.Button(janela, text="7", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("7"))
botao_8 = tk.Button(janela, text="8", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("8"))
botao_9 = tk.Button(janela, text="9", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("9"))
botao_div = tk.Button(janela, text="/", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("/"))
botao_mult = tk.Button(janela, text="*", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("*"))
botao_soma = tk.Button(janela, text="+", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("+"))
botao_sub = tk.Button(janela, text="-", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("-"))
botao_ponto=tk.Button(janela, text=".", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("."))
botao_apaga=tk.Button(janela, text="CE", font=minha_fonte, width=4, height=2, command=lambda: limpar())
botao_result=tk.Button(janela, text="=", font=minha_fonte, width=4, height=2,command=calcular)
botao_parent1=tk.Button(janela, text="(", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("("))
botao_parent2=tk.Button(janela, text=")", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor(")"))
botao_surpresa=tk.Button(janela, text="DEVS", font=minha_fonte, width=4, height=2, command=lambda: adiciona_valor("I just want to learn and learn"))


#basicamente aqui vamos desenhar os botoes, a lógica e os numeros ficaram faceis por conta do GRID
botao_7.grid(row=1, column=0)
botao_8.grid(row=1, column=1)
botao_9.grid(row=1, column=2)
botao_6.grid(row=2, column=0)
botao_5.grid(row=2, column=1)
botao_4.grid(row=2, column=2)
botao_3.grid(row=3, column=0)
botao_2.grid(row=3, column=1)
botao_1.grid(row=3, column=2)
botao_0.grid(row=4, column=1)
botao_mult.grid(row=2, column=3)
botao_div.grid(row=1, column=3)
botao_soma.grid(row=3, column=3)
botao_sub.grid(row=4,column=3)
botao_ponto.grid(row=4, column=0)
botao_apaga.grid(row=4, column=2)
botao_result.grid(row=5, column=2)
botao_parent1.grid(row=5, column=0)
botao_parent2.grid(row=5, column=1)
botao_surpresa.grid(row=5, column=3)
janela.mainloop()