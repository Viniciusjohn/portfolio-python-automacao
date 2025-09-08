# 📊 Projeto C — Dashboard Interativo de Vendas

> **Dashboard web profissional com interface moderna, múltiplas visualizações interativas, filtros dinâmicos e análises avançadas em tempo real.**

## 🎯 Problema de Negócio

Gestores e analistas enfrentam dificuldades para:
- **Visualizar métricas** de vendas de forma rápida e intuitiva
- **Analisar tendências** sem conhecimento técnico
- **Filtrar dados** dinamicamente por diferentes critérios
- **Acessar insights** em tempo real sem depender de TI
- **Compartilhar análises** de forma interativa

## 💡 Solução Implementada

### Versão Básica (`dashboard.py`)
- Relatório HTML estático simples
- Gráfico básico de barras
- Estatísticas descritivas
- Visualização offline

### Versão Profissional (`dashboard_pro.py`) ⭐
- **Interface web interativa** com Streamlit
- **Múltiplas visualizações** (barras, pizza, tendência, scatter)
- **Filtros dinâmicos** por região, categoria e valor
- **Métricas em tempo real** com comparações
- **Análises avançadas** (performance vs meta, regional)
- **Exportação de relatórios** em JSON
- **Design responsivo** e profissional

## 🚀 Como Usar

### Instalação
```bash
# Clone o repositório
git clone [seu-repositorio]
cd projeto-C_dashboard

# Instale as dependências
pip install -r requirements.txt
```

### Execução

```bash
# Versão básica (HTML estático)
python dashboard.py
# Abra relatorio.html no navegador

# Versão profissional (Web App)
streamlit run dashboard_pro.py
# Acesse http://localhost:8501
```

## 📁 Estrutura de Arquivos

```
projeto-C_dashboard/
├── dashboard.py                 # Versão básica (HTML)
├── dashboard_pro.py             # Versão profissional (Streamlit) ⭐
├── requirements.txt             # Dependências
├── vendas.csv                   # Dados de exemplo
├── relatorio.html               # Output HTML básico
├── grafico.png                  # Gráfico estático gerado
└── README.md                    # Esta documentação
```

## 🎨 Interface e Funcionalidades

### 1. Painel Principal
- **Header moderno** com gradiente e informações contextuais
- **Cards de métricas** com valores destacados e deltas
- **Layout responsivo** adaptável a diferentes telas

### 2. Filtros Interativos (Sidebar)
- **Filtro por Região:** Norte, Sul, Leste, Oeste
- **Filtro por Categoria:** Premium, Standard, Basic
- **Slider de Valor:** Valor mínimo de vendas
- **Aplicação em tempo real** em todos os gráficos

### 3. Visualizações Avançadas

#### Gráfico Principal de Vendas
- Barras coloridas por categoria
- Valores exibidos nas barras
- Interatividade com hover
- Responsivo e profissional

#### Análise Regional
- **Gráfico de barras:** Total de vendas por região
- **Gráfico de pizza:** Distribuição de clientes
- **Layout lado a lado** para comparação

#### Tendência Temporal
- **Linha de vendas reais** com markers
- **Linha de tendência** calculada automaticamente
- **Projeção visual** de crescimento/declínio

#### Performance vs Meta
- **Scatter plot** interativo
- **Códigos de cores** por status (acima/próximo/abaixo da meta)
- **Tamanho dos pontos** proporcional à performance
- **Linha de referência** para meta ideal

### 4. Análises em Tabs
- **Tab 1:** Tendência Temporal
- **Tab 2:** Performance vs Meta
- **Tab 3:** Dados Detalhados com exportação

## 📊 Métricas Calculadas

```python
# Métricas principais exibidas
{
    "Total de Vendas": "R$ 15.250,00",
    "Média por Cliente": "R$ 2.541,67",
    "Total de Clientes": 6,
    "Top Cliente": "Helena (R$ 3.100,00)"
}
```

## 🛠️ Funcionalidades Técnicas

- ✅ **Interface web moderna** - Streamlit com CSS customizado
- ✅ **Visualizações interativas** - Plotly com hover e zoom
- ✅ **Filtros dinâmicos** - Atualização em tempo real
- ✅ **Dados simulados** - Dataset expandido para demonstração
- ✅ **Métricas comparativas** - Deltas e indicadores
- ✅ **Exportação de dados** - Download em JSON
- ✅ **Design responsivo** - Adaptável a mobile/desktop
- ✅ **Performance otimizada** - Cache de dados

## 💼 Casos de Uso Reais

1. **Dashboard executivo** para CEO/diretores
2. **Análise de vendas** para gerentes comerciais
3. **Monitoramento de KPIs** em tempo real
4. **Apresentações interativas** para clientes
5. **Relatórios self-service** para analistas
6. **Acompanhamento de metas** por equipe

## 🔧 Personalização

### Adicionar Novos Filtros
```python
# Em dashboard_pro.py
idade_filter = st.sidebar.slider(
    "Faixa Etária:",
    min_value=18,
    max_value=65,
    value=(18, 65)
)
```

### Customizar Cores e Estilo
```python
# Edite a seção load_custom_css()
st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg, #your-color1, #your-color2);
}
</style>
""", unsafe_allow_html=True)
```

### Adicionar Novas Visualizações
```python
# Crie novos métodos de gráfico
def create_heatmap_analysis(self, df):
    fig = px.density_heatmap(df, x='Regiao', y='Categoria', z='Vendas')
    return fig
```

## 🌐 Deploy e Compartilhamento

### Deploy Local
```bash
streamlit run dashboard_pro.py --server.port 8501
```

### Deploy na Nuvem
```bash
# Streamlit Cloud (gratuito)
# 1. Faça push para GitHub
# 2. Conecte no https://share.streamlit.io
# 3. Deploy automático
```

### Compartilhamento
- **URL direta** para acesso web
- **Embed em sites** via iframe
- **Screenshots automáticos** para relatórios

## 📈 Próximos Passos

- [ ] Integração com banco de dados (PostgreSQL/MySQL)
- [ ] Autenticação e controle de acesso
- [ ] Cache Redis para performance
- [ ] API REST para dados externos
- [ ] Alertas automáticos por email/Slack
- [ ] Versão mobile nativa
- [ ] Exportação para PDF/Excel

## 🚨 Troubleshooting

### Dashboard não carrega
```
Solução: Verifique se o arquivo vendas.csv existe
e se todas as dependências estão instaladas.
```

### Gráficos não aparecem
```
Solução: Atualize o Plotly para versão mais recente:
pip install --upgrade plotly
```

### Filtros não funcionam
```
Solução: Verifique se os dados têm as colunas
'Regiao', 'Categoria' e 'Vendas'.
```

## 🎯 Demonstração

### Screenshots
1. **Tela Principal:** Cards de métricas + gráfico principal
2. **Análise Regional:** Gráficos lado a lado
3. **Filtros Ativos:** Sidebar com controles
4. **Dados Detalhados:** Tabela interativa

### Vídeo Demo
- Navegação completa pela interface
- Demonstração de filtros em ação
- Exportação de relatórios
- Responsividade mobile

## 🤝 Contribuição

Este dashboard demonstra capacidades avançadas de visualização de dados e desenvolvimento web com Python. Ideal para impressionar clientes e empregadores.

---

**Desenvolvido por:** [Seu Nome]  
**Contato:** [seu.email@exemplo.com]  
**LinkedIn:** [seu-linkedin]  
**Demo Online:** [link-do-deploy]
