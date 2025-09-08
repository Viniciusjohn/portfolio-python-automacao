# 📊 Projeto A — Relatório Automatizado de Vendas

> **Sistema profissional de análise e filtragem de dados de vendas com logging, configuração flexível e tratamento robusto de erros.**

## 🎯 Problema de Negócio

Empresas frequentemente precisam analisar grandes volumes de dados de vendas para:
- Identificar vendas acima de determinados valores
- Gerar relatórios executivos automatizados
- Filtrar dados relevantes para tomada de decisão
- Economizar tempo em processos manuais repetitivos

## 💡 Solução Implementada

### Versão Básica (`relatorio_vendas.py`)
- Script simples que filtra vendas acima de R$ 1.000
- Leitura direta de CSV
- Output básico no console

### Versão Profissional (`relatorio_vendas_pro.py`) ⭐
- **Configuração flexível** via arquivo JSON
- **Logging completo** de todas as operações
- **Validação robusta** de dados de entrada
- **Tratamento de erros** profissional
- **Estatísticas detalhadas** e relatórios executivos
- **Arquitetura orientada a objetos**

## 🚀 Como Usar

### Instalação
```bash
# Clone o repositório
git clone [seu-repositorio]
cd projeto-A_relatorio-vendas

# Instale as dependências
pip install -r requirements.txt
```

### Execução Rápida
```bash
# Versão básica
python relatorio_vendas.py

# Versão profissional
python relatorio_vendas_pro.py
```

### Configuração Personalizada

1. **Edite o arquivo `config.json`:**
```json
{
    "arquivo_entrada": "seus_dados.csv",
    "arquivo_saida": "resultado_filtrado.csv",
    "valor_minimo": 1500,
    "colunas_obrigatorias": ["Cliente", "Vendas"]
}
```

2. **Execute novamente:**
```bash
python relatorio_vendas_pro.py
```

## 📁 Estrutura de Arquivos

```
projeto-A_relatorio-vendas/
├── relatorio_vendas.py          # Versão básica
├── relatorio_vendas_pro.py      # Versão profissional ⭐
├── config.json                  # Configurações
├── requirements.txt             # Dependências
├── vendas.csv                   # Dados de exemplo
├── vendas_filtradas.csv         # Output gerado
├── relatorio_estatisticas.json  # Estatísticas detalhadas
├── relatorio_vendas.log         # Log de operações
└── README.md                    # Esta documentação
```

## 📊 Outputs Gerados

### 1. CSV Filtrado
- Dados que atendem aos critérios definidos
- Mantém estrutura original dos dados

### 2. Relatório de Estatísticas (JSON)
```json
{
    "timestamp": "2025-01-07 21:45:00",
    "total_registros_original": 4,
    "total_registros_filtrados": 2,
    "vendas_originais": {
        "total": 4100.00,
        "media": 1025.00,
        "maximo": 1500.00
    }
}
```

### 3. Log Detalhado
- Registro completo de todas as operações
- Timestamps precisos
- Identificação de erros e warnings

## 🛠️ Funcionalidades Técnicas

- ✅ **Validação de dados** - Verifica integridade e estrutura
- ✅ **Configuração flexível** - JSON editável
- ✅ **Logging profissional** - Arquivo + console
- ✅ **Tratamento de erros** - Mensagens claras e recovery
- ✅ **Estatísticas automáticas** - Métricas de negócio
- ✅ **Arquitetura limpa** - Código orientado a objetos

## 💼 Casos de Uso Reais

1. **Filtrar vendas premium** (> R$ 5.000)
2. **Identificar top performers** mensais
3. **Gerar relatórios executivos** automatizados
4. **Processar dados de CRM** em lote
5. **Análise de performance** de equipes

## 🔧 Personalização

### Alterar Critérios de Filtro
```python
# No config.json
"valor_minimo": 2000,  # Novo valor mínimo
```

### Adicionar Novas Validações
```python
# Edite o método validate_data() em relatorio_vendas_pro.py
def validate_data(self, df):
    # Suas validações customizadas
    pass
```

## 📈 Próximos Passos

- [ ] Interface web com Streamlit
- [ ] Integração com APIs de CRM
- [ ] Alertas automáticos por email
- [ ] Dashboard em tempo real
- [ ] Exportação para Excel com formatação

## 🤝 Contribuição

Este projeto foi desenvolvido como parte de um portfólio profissional de automação Python. Sugestões e melhorias são bem-vindas!

---

**Desenvolvido por:** [Seu Nome]  
**Contato:** [seu.email@exemplo.com]  
**LinkedIn:** [seu-linkedin]
