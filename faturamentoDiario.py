import numpy as np
import pandas as pd

def faturamento(dadojson):
    df = pd.read_json(dadojson)
    soma, maiorFaturamento, menorFaturamento, media, cont, contZero = 0, 0, 0, 0, 0, 0
    acimaDaMedia = []
    for i in df['valor']:
        soma += i
        if i == 0.0:
            contZero += 1
        if cont == 0:
            maiorFaturamento, menorFaturamento = i, i
        else:
            if i > maiorFaturamento:
                maiorFaturamento = i
            if i < menorFaturamento and i != 0:
                menorFaturamento = i
        cont += 1
    media = soma / (len(df) - contZero)
    for i in df['valor']:
        if i > media:
            acimaDaMedia.append(i)
    print(f"O menor faturamento foi de {menorFaturamento}")
    print(f"O maior faturamento foi de {maiorFaturamento}")
    print(f"O faturamento médio foi de {media} e as vendas superaram a média {len(acimaDaMedia)} dias")

