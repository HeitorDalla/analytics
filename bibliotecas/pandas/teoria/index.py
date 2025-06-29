import pandas as pd

df = pd.read_csv('bibliotecas/pandas/teoria/relatorioAbril.csv')

print(df)

# Descrição geral do dados

print(df.dtypes)

print(df.columns)

print(df.values)

print(df.describe()) # Funciona somente em colunas numéricas


# Selecionar algumas linhas - Head, tail, loc, iloc

print(df.head(4))

print(df.tail(1))

serie = pd.Series(['Heitor', 'Gilmar', 'Marli', 'Nadir'], index=['nome1', 'nome2', 'nome3', 'nome4'])

print(serie)

# loc - seleciona pelo índice

print(serie.loc['nome1'])

print(serie.loc['nome4'])

# iloc - selecione pela posição

print(serie.iloc[2])

print(serie.iloc[-1])

# Selecionar alguma coluna

print(df['produto'])

print(df[df['quantidade'] > 10])


# Outras Funções


# Crosstab
dataframe = pd.read_csv('bibliotecas/pandas/teoria/vendas.csv')

tabelaComparativa = pd.crosstab(dataframe['data'], dataframe['produto'], margins=True) # Adiciona uma coluna e uma linha com a somatória geral

tabelaComparativa.to_csv('bibliotecas/pandas/teoria/tabelaComparativa.csv')


# Groupby
print('----------------------------------------')

mediaPreco = dataframe.groupby('produto')['preco'].mean()

print(mediaPreco)

print('----------------------------------------')


# Manipulação dos dados
dataframe2 = pd.read_csv("bibliotecas/pandas/teoria/car-sales.csv")

print(dataframe2)

print(dataframe2.describe())

print(dataframe2.info())

print('----------------------------------------')


# Transformar a coluna em inteiro

dataframe2['Price'] = (dataframe2['Price'].str.replace(r'[\$,\.]', '', regex=True).astype(int) / 100).astype(int)

print(dataframe2)

print('----------------------------------------')


# Trabalhar com dados faltantes

dataframe3 = pd.read_csv('bibliotecas/pandas/teoria/car-sales-missing-data.csv')

print(dataframe3)

print('----------------------------------------')


# SUBSTITUIR os valores ausentes

dataframe3['Doors'] = dataframe3['Doors'].fillna(1)

dataframe3['Price'] = dataframe3['Price'].fillna(10000)

dataframe3['Odometer'] = dataframe3['Odometer'].fillna(0)

dataframe3['Price'] = (dataframe3['Price']
                       .astype(str)
                       .str.replace(r'[\$,\.]', '', regex=True)
                       ).astype(int)

print(dataframe3)

print('----------------------------------------')


# # EXCLUIR os valores ausentes

# dataframe3 = dataframe3.dropna()

# print(dataframe3)

# print('----------------------------------------')

# # Colunas especificas

# dataframe3 = dataframe3.dropna(subset=['Price'])

# print(dataframe3)

# print('----------------------------------------')


# # Criação de colunas

# print(dataframe3.info())

# dataframe3['valor_porta'] = dataframe3['Price'] / dataframe3['Doors']

# dataframe3['valor_porta'] = dataframe3['valor_porta'].astype(int)

# print(dataframe3)


# # Excluir colunas

# dataframe3 = dataframe3.drop('Odometer', axis=1)


# # Embaralhar os dados

# dataframe3 = dataframe3.sample(frac=0.2) # Pegar apenas 20 porcento dos dados, importante para machine learning

# print(dataframe3)