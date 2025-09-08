import pandas as pd
import matplotlib.pyplot as plt
import yagmail

# Lê vendas
df = pd.read_csv("vendas.csv")

# Gera gráfico
df.plot(x="Cliente", y="Vendas", kind="bar")
plt.title("Relatório de Vendas")
plt.savefig("grafico_vendas.png")
plt.close()

# Envia e-mail
EMAIL = "seu_email@gmail.com"
APP_PASSWORD = "sua_senha_app"
DESTINATARIO = "destinatario@gmail.com"

yag = yagmail.SMTP(EMAIL, APP_PASSWORD)
yag.send(
    to=DESTINATARIO,
    subject="Relatório Automático",
    contents="Segue o relatório em anexo.",
    attachments="grafico_vendas.png"
)
print("✅ E-mail enviado com sucesso!")
