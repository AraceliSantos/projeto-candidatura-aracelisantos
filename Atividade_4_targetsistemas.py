#iniciando atividade 4: 

distr = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

fat_total = 0

for i in distr.values():
    fat_total += i

#print(fat_total, '\n')

distr['SP']= distr.get('SP') * 100 / fat_total
distr['RJ']= distr.get('RJ') * 100 / fat_total
distr['MG']= distr.get('MG') * 100 / fat_total
distr['ES']= distr.get('ES') * 100 / fat_total
distr['Outros']= distr.get('Outros') * 100 / fat_total

for k in distr:
    print(f"o percentutal da filial '{k}' representa {round(distr.get(k), 2)} % do faturamento total da distribuidora.", '\n')
    