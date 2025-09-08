import pandas as pd
import matplotlib.pyplot as plt

# Carrega CSV
df = pd.read_csv("vendas.csv")

# Estatísticas
resumo = df["Vendas"].describe()

# Gráfico
df.plot(x="Cliente", y="Vendas", kind="bar")
plt.title("Vendas por Cliente")
plt.savefig("grafico.png")
plt.close()

# Gera HTML
with open("relatorio.html", "w") as f:
    f.write("<h1>Relatório de Vendas</h1>")
    f.write(resumo.to_frame().to_html())
    f.write('<br><img src="grafico.png">')

print("Relatorio 'relatorio.html' gerado com sucesso!")
