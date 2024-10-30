import os
import pandas as pd
import matplotlib.pyplot as plt

# Defina o diretório onde estão os arquivos .csv
diretorio = 'C:\\desenvhome\\teste'

# Inicialize um dicionário para armazenar os gastos por descricao
gastos_por_descricao = {}

# Liste todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Itere sobre os arquivos .csv
for arquivo in arquivos:
    if arquivo.endswith('.csv'):
        # Leia o arquivo .csv
        dados = pd.read_csv(os.path.join(diretorio, arquivo), encoding='latin-1')
        
        # Calcule o total gasto por descricao
        for descricao, valor in zip(dados['Descricao'], dados['Valor']):
            gastos_por_descricao[descricao] = gastos_por_descricao.get(descricao, 0) + abs(valor)

# Crie o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(gastos_por_descricao.values(), labels=gastos_por_descricao.keys(), autopct='%1.1f%%', startangle=140)
print(gastos_por_descricao.values())

plt.axis('equal')

# Mostre o gráfico
plt.show()
