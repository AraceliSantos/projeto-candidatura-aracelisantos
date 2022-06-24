Fatura_mensal = {'dia1':22174.1664, 'dia2':24537.6698, 'dia3':26139.6134, 'dia4': 0.0, 'dia5': 0.0, 'dia6':26742.6612, 
                 'dia7': 0.0, "dia8": 42889.2258, "dia9": 46251.174, "dia10": 11191.4722, "dia11": 0.0, "dia12": 0.0, 
                 "dia13": 3847.4823, "dia14": 373.7838, "dia15": 2659.7563, "dia16": 48924.2448, "dia17": 18419.2614,
                 "dia18": 0.0, "dia19": 0.0, "dia20": 35240.1826, "dia21": 43829.1667, "dia22": 18235.6852, "dia23": 4355.0662,
                 "dia24": 13327.1025, "dia25": 0.0, "dia26": 0.0, "dia27": 25681.8318, "dia28": 1718.1221,"dia29": 13220.495,
                 "dia30": 8414.61}


newFat_mensal = {key: Fatura_mensal[key]
                for key in Fatura_mensal
                if Fatura_mensal[key] != 0}


max_val= max(newFat_mensal.values())
print('O maior valor de faturamento no mês é:', max_val, '\n')

min_val= min(newFat_mensal.values())
print('o menor valor de faturamento no mês é:', min_val, '\n')

med_val= sum(newFat_mensal.values())/ len(newFat_mensal)

count = 0 
for k,v in newFat_mensal.items():
  
    if v > med_val:
        count = count + 1

print('Existe %s dias que tiveram faturamento acima da média no mês!' %(count))