# 📧 Projeto B — Sistema de Envio Automático de Relatórios

> **Sistema profissional de geração e envio automatizado de relatórios por email com múltiplas visualizações, templates HTML e agendamento inteligente.**

## 🎯 Problema de Negócio

Empresas enfrentam desafios na distribuição de relatórios:
- **Envios manuais** causam atrasos e inconsistências
- **Risco de esquecimento** de relatórios importantes
- **Falta de padronização** visual nos relatórios
- **Ausência de automação** para relatórios periódicos
- **Dificuldade de acompanhamento** de métricas em tempo hábil

## 💡 Solução Implementada

### Versão Básica (`enviar_relatorio.py`)
- Gráfico simples de barras
- Envio básico por Gmail
- Configuração hardcoded

### Versão Profissional (`enviar_relatorio_pro.py`) ⭐
- **Múltiplos gráficos** profissionais (barras, pizza, tendência)
- **Templates HTML** responsivos e modernos
- **Configuração segura** via variáveis de ambiente
- **Agendamento automático** (semanal/mensal)
- **Logging completo** e tratamento de erros
- **Estatísticas avançadas** e análises

## 🚀 Como Usar

### Instalação
```bash
# Clone o repositório
git clone [seu-repositorio]
cd projeto-B_email-relatorio

# Instale as dependências
pip install -r requirements.txt
```

### Configuração Inicial

1. **Configure as credenciais de email:**
```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env com suas credenciais
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app_do_gmail
EMAIL_RECIPIENTS=destinatario1@email.com,destinatario2@email.com
```

2. **Configure senha de app do Gmail:**
   - Acesse [Configurações do Google](https://myaccount.google.com/security)
   - Ative a verificação em 2 etapas
   - Gere uma "Senha de app" específica
   - Use essa senha no arquivo `.env`

### Execução

```bash
# Envio único (versão básica)
python enviar_relatorio.py

# Envio único (versão profissional)
python enviar_relatorio_pro.py

# Modo agendamento automático
python enviar_relatorio_pro.py --schedule
```

## 📁 Estrutura de Arquivos

```
projeto-B_email-relatorio/
├── enviar_relatorio.py          # Versão básica
├── enviar_relatorio_pro.py      # Versão profissional ⭐
├── requirements.txt             # Dependências
├── .env.example                 # Template de configuração
├── .env                         # Suas credenciais (não versionar!)
├── vendas.csv                   # Dados de exemplo
├── grafico_vendas_barras.png    # Gráfico de barras gerado
├── grafico_vendas_pizza.png     # Gráfico de pizza gerado
├── grafico_vendas_linha.png     # Gráfico de tendência gerado
├── email_reports.log            # Log de operações
└── README.md                    # Esta documentação
```

## 📊 Funcionalidades Avançadas

### 1. Múltiplas Visualizações
- **Gráfico de Barras:** Vendas por cliente com valores
- **Gráfico de Pizza:** Distribuição percentual
- **Gráfico de Linha:** Evolução temporal (simulada)
- **Estilo profissional:** Seaborn + cores personalizadas

### 2. Template HTML Responsivo
```html
<!-- Exemplo do template gerado -->
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-value">R$ 15.250,00</div>
        <div class="stat-label">Total de Vendas</div>
    </div>
</div>
```

### 3. Agendamento Inteligente
- **Relatórios semanais:** Toda segunda-feira às 9h
- **Relatórios mensais:** Todo dia 1º às 8h
- **Execução contínua:** Sistema roda em background

### 4. Estatísticas Automáticas
```python
{
    'total_vendas': 15250.00,
    'media_vendas': 2541.67,
    'cliente_top': 'Helena',
    'percentual_top_cliente': 20.3
}
```

## 🛠️ Funcionalidades Técnicas

- ✅ **Configuração segura** - Variáveis de ambiente
- ✅ **Templates HTML** - Design profissional responsivo
- ✅ **Múltiplos gráficos** - Visualizações diversificadas
- ✅ **Agendamento automático** - Relatórios periódicos
- ✅ **Logging detalhado** - Rastreamento completo
- ✅ **Tratamento de erros** - Recovery automático
- ✅ **Múltiplos destinatários** - Lista configurável

## 💼 Casos de Uso Reais

1. **Relatórios executivos** semanais para diretoria
2. **Acompanhamento de metas** mensais
3. **Alertas de performance** automáticos
4. **Distribuição de KPIs** para equipes
5. **Relatórios de vendas** para stakeholders

## 🔧 Personalização

### Alterar Frequência de Envio
```python
# Em enviar_relatorio_pro.py
schedule.every().tuesday.at("10:00").do(self.generate_and_send_report)
schedule.every(15).days.at("08:00").do(self.generate_and_send_report)
```

### Customizar Template HTML
```python
# Edite o método create_html_template()
def create_html_template(self, stats):
    # Seu template personalizado
    return custom_html
```

### Adicionar Novos Gráficos
```python
# No método generate_charts()
# Adicione seus gráficos personalizados
fig = px.scatter(df, x='Cliente', y='Vendas')
```

## 🔒 Segurança

- **Nunca** commite o arquivo `.env`
- Use **senhas de app** específicas do Gmail
- **Valide** destinatários antes do envio
- **Log** todas as operações para auditoria

## 📈 Próximos Passos

- [ ] Integração com APIs de CRM (Salesforce, HubSpot)
- [ ] Dashboard web para configuração
- [ ] Suporte a anexos Excel/PDF
- [ ] Notificações via Slack/Teams
- [ ] Análise de engajamento dos emails

## 🚨 Troubleshooting

### Erro de Autenticação Gmail
```
Solução: Verifique se a verificação em 2 etapas está ativa
e se você está usando uma senha de app específica.
```

### Gráficos não são gerados
```
Solução: Verifique se o arquivo vendas.csv existe
e tem as colunas 'Cliente' e 'Vendas'.
```

### Agendamento não funciona
```
Solução: Execute com --schedule e mantenha o terminal aberto
ou configure como serviço do sistema.
```

## 🤝 Contribuição

Este projeto demonstra automação profissional de relatórios com Python. Ideal para portfolios e projetos reais de empresas.

---

**Desenvolvido por:** [Seu Nome]  
**Contato:** [seu.email@exemplo.com]  
**LinkedIn:** [seu-linkedin]
