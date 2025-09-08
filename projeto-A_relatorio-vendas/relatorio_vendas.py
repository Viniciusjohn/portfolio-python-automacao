import pandas as pd

# Carrega o CSV
df = pd.read_csv("vendas.csv")

print("📊 Dados Originais:")
print(df)

# Filtra vendas acima de 1000
df_filtrado = df[df["Vendas"] > 1000]
print("\n🔎 Vendas acima de 1000:")
print(df_filtrado)

# Salva novo arquivo
df_filtrado.to_csv("vendas_filtradas.csv", index=False)
print("\nArquivo 'vendas_filtradas.csv' gerado com sucesso!")
