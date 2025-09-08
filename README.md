# 🚀 Portfólio Profissional Python - Automação & Analytics

> **Conjunto completo de projetos Python para automação empresarial, análise de dados e dashboards interativos. Pronto para apresentações profissionais e projetos freelance.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Visão Geral

Este portfólio demonstra soluções práticas e profissionais para problemas reais de negócio usando Python. Cada projeto inclui versões básicas e avançadas, documentação completa e está pronto para uso em ambiente corporativo.

### 🎯 Problemas Resolvidos
- **Automação de relatórios** manuais e repetitivos
- **Visualização de dados** complexos de forma intuitiva  
- **Distribuição automatizada** de insights por email
- **Dashboards interativos** para tomada de decisão
- **Processamento em lote** de grandes volumes de dados

## 🏗️ Projetos Incluídos

### 📊 [Projeto A - Relatório Automatizado de Vendas](./projeto-A_relatorio-vendas/)
**Sistema profissional de análise e filtragem de dados**

- ✅ **Versão Básica:** Filtro simples de vendas
- ⭐ **Versão Pro:** Logging, configuração JSON, validação robusta
- 🔧 **Tecnologias:** Pandas, JSON, Logging
- 💼 **Caso de Uso:** Filtrar vendas premium, relatórios executivos

```python
# Exemplo de uso
relatorio = RelatorioVendas()
relatorio.run()  # Gera CSV filtrado + estatísticas JSON
```

### 📧 [Projeto B - Sistema de Email Automático](./projeto-B_email-relatorio/)
**Geração e envio automatizado de relatórios por email**

- ✅ **Versão Básica:** Gráfico simples + envio Gmail
- ⭐ **Versão Pro:** Múltiplos gráficos, templates HTML, agendamento
- 🔧 **Tecnologias:** Matplotlib, Seaborn, Yagmail, Schedule
- 💼 **Caso de Uso:** Relatórios semanais, alertas automáticos

```python
# Exemplo de uso
email_system = EmailReportSender()
email_system.generate_and_send_report()  # Envia relatório completo
```

### 📈 [Projeto C - Dashboard Interativo](./projeto-C_dashboard/)
**Dashboard web profissional com análises avançadas**

- ✅ **Versão Básica:** HTML estático com gráfico
- ⭐ **Versão Pro:** Web app Streamlit com filtros dinâmicos
- 🔧 **Tecnologias:** Streamlit, Plotly, Pandas
- 💼 **Caso de Uso:** Dashboard executivo, análise self-service

```python
# Exemplo de uso
streamlit run dashboard_pro.py
# Acesse http://localhost:8501
```

## 🚀 Quick Start

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)

### Instalação Rápida
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/portfolio-python.git
cd portfolio-python

# Instale dependências de todos os projetos
pip install -r requirements.txt

# Ou instale por projeto individual
cd projeto-A_relatorio-vendas && pip install -r requirements.txt
```

### Teste Rápido
```bash
# Teste o Projeto A (Relatório)
cd projeto-A_relatorio-vendas
python relatorio_vendas_pro.py

# Teste o Projeto B (Email) - Configure .env primeiro
cd ../projeto-B_email-relatorio
cp .env.example .env  # Edite com suas credenciais
python enviar_relatorio_pro.py

# Teste o Projeto C (Dashboard)
cd ../projeto-C_dashboard
streamlit run dashboard_pro.py
```

## 📊 Demonstrações

### Projeto A - Relatórios Automatizados
![Relatório Output](./assets/relatorio-demo.png)
- Filtragem inteligente de dados
- Estatísticas executivas automáticas
- Logging completo de operações

### Projeto B - Emails Profissionais
![Email Template](./assets/email-demo.png)
- Templates HTML responsivos
- Múltiplas visualizações anexadas
- Agendamento automático

### Projeto C - Dashboard Interativo
![Dashboard Interface](./assets/dashboard-demo.png)
- Interface moderna e intuitiva
- Filtros dinâmicos em tempo real
- Análises avançadas interativas

## 🛠️ Stack Tecnológico

### Core Libraries
- **Pandas** - Manipulação e análise de dados
- **Matplotlib/Seaborn** - Visualizações estáticas
- **Plotly** - Gráficos interativos

### Web & Interface
- **Streamlit** - Dashboards web interativos
- **HTML/CSS** - Templates responsivos

### Automação & Comunicação
- **Yagmail** - Envio automatizado de emails
- **Schedule** - Agendamento de tarefas
- **Python-dotenv** - Gerenciamento seguro de configurações

### Qualidade & Logging
- **Logging** - Rastreamento de operações
- **JSON** - Configurações flexíveis
- **Pathlib** - Manipulação robusta de arquivos

## 💼 Casos de Uso Empresariais

### 🏢 Pequenas e Médias Empresas
- **Relatórios de vendas** automatizados
- **Dashboards executivos** sem custo de BI
- **Alertas por email** para métricas críticas

### 🏭 Empresas Corporativas
- **Integração com sistemas** existentes
- **Processamento em lote** de dados
- **Distribuição automatizada** de insights

### 👨‍💼 Freelancers e Consultores
- **Soluções rápidas** para clientes
- **Templates reutilizáveis** para projetos
- **Demonstrações profissionais** de capacidades

## 🔧 Personalização e Extensão

### Configurações Flexíveis
```json
// config.json exemplo
{
    "valor_minimo": 1000,
    "email_recipients": ["cliente@empresa.com"],
    "dashboard_theme": "corporate"
}
```

### Integração com APIs
```python
# Exemplo de extensão para CRM
def integrate_salesforce():
    # Sua integração aqui
    pass
```

### Customização Visual
```python
# Personalizar cores do dashboard
CORPORATE_COLORS = {
    'primary': '#667eea',
    'secondary': '#764ba2',
    'success': '#28a745'
}
```

## 📈 Roadmap e Melhorias

### Próximas Funcionalidades
- [ ] **Integração com bancos de dados** (PostgreSQL, MySQL)
- [ ] **APIs REST** para integração externa
- [ ] **Autenticação e controle de acesso**
- [ ] **Notificações Slack/Teams**
- [ ] **Exportação PDF/Excel** avançada
- [ ] **Cache Redis** para performance
- [ ] **Containerização Docker**

### Melhorias Planejadas
- [ ] **Testes automatizados** (pytest)
- [ ] **CI/CD Pipeline** (GitHub Actions)
- [ ] **Documentação interativa** (Sphinx)
- [ ] **Métricas de performance**

## 🎓 Valor Educacional

### Para Aprendizado
- **Código comentado** e bem estruturado
- **Padrões de desenvolvimento** profissionais
- **Arquitetura escalável** e manutenível
- **Boas práticas** de segurança

### Para Portfolio
- **Projetos completos** e funcionais
- **Documentação profissional**
- **Casos de uso reais** demonstrados
- **Código pronto para produção**

## 🤝 Contribuição e Suporte

### Como Contribuir
1. Fork o repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

### Suporte
- 📧 **Email:** [seu.email@exemplo.com]
- 💼 **LinkedIn:** [seu-linkedin]
- 🐙 **GitHub:** [seu-github]

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🏆 Reconhecimentos

Desenvolvido como portfólio profissional demonstrando:
- **Automação empresarial** com Python
- **Visualização de dados** moderna
- **Desenvolvimento web** interativo
- **Integração de sistemas** robusta

---

<div align="center">

**🚀 Pronto para transformar dados em insights acionáveis!**

[📧 Entre em Contato](mailto:seu.email@exemplo.com) | [💼 LinkedIn](https://linkedin.com/in/seu-perfil) | [🌐 Portfolio Online](https://seu-portfolio.com)

</div>
