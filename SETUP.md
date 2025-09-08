# 🚀 Setup Rápido do Portfólio

## Instalação Completa

### 1. Instalar Dependências
```bash
# Instalar todas as dependências do portfólio
pip install -r requirements.txt

# Ou instalar por projeto individual:
cd projeto-A_relatorio-vendas && pip install -r requirements.txt
cd ../projeto-B_email-relatorio && pip install -r requirements.txt  
cd ../projeto-C_dashboard && pip install -r requirements.txt
```

### 2. Testar Projetos

#### Projeto A - Relatórios
```bash
cd projeto-A_relatorio-vendas
python relatorio_vendas_pro.py
# Verifica: vendas_filtradas.csv e relatorio_estatisticas.json
```

#### Projeto B - Email (Configurar primeiro)
```bash
cd projeto-B_email-relatorio
cp .env.example .env
# Edite .env com suas credenciais Gmail
python enviar_relatorio_pro.py
```

#### Projeto C - Dashboard
```bash
cd projeto-C_dashboard
python dashboard.py  # Versão básica
streamlit run dashboard_pro.py  # Versão web
```

## Configuração Gmail para Projeto B

1. **Ativar 2FA:** [Google Account Security](https://myaccount.google.com/security)
2. **Gerar Senha de App:** Segurança > Senhas de app > Selecionar app
3. **Configurar .env:**
```
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=senha_de_app_gerada
EMAIL_RECIPIENTS=destinatario@email.com
```

## Estrutura Final do Portfólio

```
Portfolio/
├── README.md                     # Apresentação principal
├── SETUP.md                      # Este arquivo
├── requirements.txt              # Dependências globais
├── projeto-A_relatorio-vendas/   # Automação de relatórios
├── projeto-B_email-relatorio/    # Sistema de email
├── projeto-C_dashboard/          # Dashboard interativo
└── assets/                       # Screenshots e demos (criar)
```

## Próximos Passos

1. **Testar todos os scripts** ✅
2. **Capturar screenshots** dos outputs
3. **Gravar vídeos** demonstrativos (30-60s cada)
4. **Publicar no GitHub** com README profissional
5. **Criar perfil LinkedIn** destacando os projetos
6. **Preparar apresentação** para clientes

## Comandos Úteis

```bash
# Instalar dependências específicas
pip install pandas matplotlib streamlit plotly

# Executar dashboard em porta específica
streamlit run dashboard_pro.py --server.port 8501

# Verificar versões instaladas
pip list | grep -E "(pandas|streamlit|matplotlib)"
```
