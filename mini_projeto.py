import numpy as np
import matplotlib.pyplot as plt

def lancamento():
    primeiro_lancamento = np.random.choice([1,2,3,4,5,6])
    segundo_lancamento = np.random.choice([1,2,3,4,5,6])
    soma = primeiro_lancamento + segundo_lancamento
    return soma

def simulacoes(vezes):
    todas_simulacoes = []
    for i in range(vezes):
        resultado_obtido = lancamento()
        todas_simulacoes.append(resultado_obtido)
    return np.array(todas_simulacoes)

def media_dos_resultados(resultado_de_todas_simulacoes):
    return resultado_de_todas_simulacoes.mean()

def lancamento_maximo(resultado_de_todas_simulacoes):
    return resultado_de_todas_simulacoes.max()

def lancamento_minimo(resultado_de_todas_simulacoes):
    return resultado_de_todas_simulacoes.min()

def numero_de_ocorrencias(resultado_de_todas_simulacoes, numero):
    return np.count_nonzero(resultado_de_todas_simulacoes == numero)

n = int(input("Insira a quantidade de simulações: "))
dados_totais = simulacoes(n)
media = media_dos_resultados(dados_totais) 
print("A média dos resultados é: {fmedia}.".format(fmedia = media))
maior = lancamento_maximo(dados_totais)
print("O lançamento máximo foi: {fvalor}.".format(fvalor = maior))
menor = lancamento_minimo(dados_totais)
print("O lançamento mínimo foi: {fvalor}.".format(fvalor = menor))
ocorrencia_dois = numero_de_ocorrencias(dados_totais, 2)
ocorrencia_tres = numero_de_ocorrencias(dados_totais, 3)
ocorrencia_quatro = numero_de_ocorrencias(dados_totais, 4)
ocorrencia_cinco = numero_de_ocorrencias(dados_totais, 5)
ocorrencia_seis = numero_de_ocorrencias(dados_totais, 6)
ocorrencia_sete = numero_de_ocorrencias(dados_totais, 7)
ocorrencia_oito = numero_de_ocorrencias(dados_totais, 8)
ocorrencia_nove = numero_de_ocorrencias(dados_totais, 9)
ocorrencia_dez = numero_de_ocorrencias(dados_totais, 10)
ocorrencia_onze = numero_de_ocorrencias(dados_totais, 11)
ocorrencia_doze = numero_de_ocorrencias(dados_totais, 12)
print("O lançamento com valor igual a dois aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_dois))
print("O lançamento com valor igual a três aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_tres))
print("O lançamento com valor igual a quatro aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_quatro))
print("O lançamento com valor igual a cinco aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_cinco))
print("O lançamento com valor igual a seis aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_seis))
print("O lançamento com valor igual a sete aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_sete))
print("O lançamento com valor igual a oito aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_oito))
print("O lançamento com valor igual a nove aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_nove))
print("O lançamento com valor igual a dez aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_dez))
print("O lançamento com valor igual a onze aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_onze))
print("O lançamento com valor igual a doze aconteceu {fvezes} vezes.".format(fvezes = ocorrencia_doze))

def grafico():
    plt.hist(dados_totais,  color= "m", bins = 30, align = 'mid')
    plt.xlabel("Resultado da soma dos lançamentos dos dados") 
    plt.ylabel("Número de ocorrências") 
    plt.xticks(np.arange(0, 15, 1))
    plt.title("Histograma")
    plt.legend()
    plt.show()

grafico()

'''Teste de Hipótese: 
- Supondo um jogo justo (ou seja, todos os lançamentos são igualmente prováveis), o resultado da sua simulação coincide com essa suposição? Por que sim ou por que não?
- O que isso significa para um jogador do jogo de dados?

Observe que, na análise de dados, geramos a média e a quantidade de vezes que cada resultado (soma de dois lançamentos) aconteceu.
Se o jogo fosse realmente justo, a quantidade de ocorrências dos casos (2,3,4,5,6,7,8,9,10,11,12) seria a mesma, uma vez que um jogo justo implica resultados equiprováveis.
Mas, o código, da maneira que foi construído, mostra que há casos tendenciosos. Veja que, para 1000 simulações, por exemplo, a maior ocorrência de resultados são aqueles perto da média (por volta de 7).
Sendo ainda mais clara, para este caso, os resultados perto da média (ou mesmo iguais à média (parte inteira caso a média seja um float)) são mais prováveis de acontecer. Observe, ainda, no gráfico, para grandes quantidades de simulações, o histograma nos recorda uma distribuição normal para os resultados (soma dos lançamentos).
Como temos um jogo tendencioso, para um jogador, se estivermos no caso de um jogo de apostas, o mais proveitoso seria apostar num resultado próximo à media, ou naquele que mais ocorre, uma vez que a probabilidade de sucesso seria maior.
Para o caso em que há poucas simulações, fica mais difícil o jogador prever qual resultado possui uma probabilidade maior, uma vez que a média (ou valores perto da média) nem sempre vai representar o resultado que mais acontece.
'''
